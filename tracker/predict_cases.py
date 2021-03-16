#!/usr/bin/env python
# coding: utf-8

# In[1]:


# exec(%matplotlib inline)


# In[2]:

def main(country) :
    
    import pandas as pd
    import os

    # In[3]:


    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
    from scipy.optimize import curve_fit
    from IPython.display import display, Markdown
    import collections
    import datetime

    # In[4]:


    import warnings
    warnings.filterwarnings('ignore')


    # In[5]:


    ccpw = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    cdpw = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    df_confirmed_all = pd.read_csv(ccpw).dropna(axis=1, how='all')
    df_deaths_all = pd.read_csv(cdpw).dropna(axis=1, how='all')

    
    # In[6]:


    df_confirmed_all['Country/Region'].unique()

    # In[7]:


    LocationColumns = ['Province/State', 'Country/Region', 'Lat', 'Long']
    DataColumns = list(df_confirmed_all.columns[4:])
    DataColumnsDT = pd.to_datetime(DataColumns)
    DataColumnsDT[:2], DataColumnsDT[-2:]

    # In[8]:


    countries = df_confirmed_all['Country/Region'].unique()
    countries.sort()
    # display(Markdown('*List of Countries*'))
    selectors = ['Country']
    # print(countries)


    # In[9]:


    def compute_series(df_metric):
        m_series = {}
        # count
        count = df_metric[DataColumns].sum(axis=0)
        count = df_metric[DataColumns].sum(axis=0)
        count.index = DataColumnsDT
        count = count[count > 0]
        m_series['count'] = count
        m_series['log(count)'] = np.log(count)
        m_series['d(count)/dt'] = count.diff()
        m_series['d(log(count))/dt'] = count.diff() / count
        return m_series


    def display_series(m_series, series_label, selection_location, save_fig_dir='.', display_days_back=None , name=None):
        plt.figure(figsize=(16, 10))
        stitle = '{0} charts for {1} as of {2}'.format(series_label, selection_location, last_update)
        plt.suptitle(stitle, fontsize=16)
        plot_index = 220
        for key in m_series.keys():
            series = m_series[key].copy()
            if not display_days_back is None:
                series = series[-display_days_back:]
            plot_index += 1
            plt.subplot(plot_index)
            title = '{0} {1}'.format(series_label, key)
            series.plot(grid=True, title=title)
            if 'd(log' in key:
                plt.ylim(-0.5, 0.5)
        fpath = os.path.join(save_fig_dir, '{0}.png'.format(name))
        print(fpath)
        fig1 = plt.gcf()
        fig1.tight_layout(pad=1)
        fig1.subplots_adjust(top=0.9)
        fig1.savefig(fpath)
        v, t = m_series['count'][-1], m_series['count'].index[-1]
        s = 'Latest number of {0} in {1} is ** {2} ** as of {3}'.format(series_label, location_label, v, t)
        # display(Markdown(s))
        return s 


    def display_percentage_chart(df_numerator, df_denominator, metric, selection_location, save_fig_dir='.'):
        numerator = df_numerator[DataColumns].sum(axis=0)
        denominator = df_denominator[DataColumns].sum(axis=0)
        (numerator // denominator * 100).plot()
        stitle = '{0} rate % in {1}'.format(metric, selection_location)
        plt.title(stitle)
        plt.grid()
        fpath1 = os.path.join(save_fig_dir, '4.png')
        plt.savefig(fpath1)
        # return fpath1


    # In[10]:


    def model_func(x, a):
        return np.exp(a * x)


    # In[11]:


    def coeff_evaluate_mean(m_series, days_back):
        av_alpha = m_series['d(log(count))/dt'][-days_back:].mean()
        return av_alpha, None


    def multi_factors(m_series, coeff_evaluate, days_back=None):
        av_alpha, _ = coeff_evaluate(m_series, days_back)
        count = m_series['count']
        day_factor = np.exp(av_alpha)
        week_factor = np.exp(av_alpha) ** 7
        projected_week = count[-1] * week_factor
        return day_factor, week_factor, projected_week


    def multi_factors1(m_series, days_back=1):
        av_alpha = m_series['d(log(count))/dt'][-days_back:].mean()
        count = m_series['count']
        day_factor = np.exp(av_alpha)
        week_factor = np.exp(av_alpha) ** 7
        projected_week = count[-1] * week_factor
        return day_factor, week_factor, projected_week


    def display_factors(day_factor, week_factor, projected_week, series_label, location_label):
        return 'Every week the number of {2} increases roughly by a factor of {0:.1f} in {1}'.format(week_factor, location_label, series_label)


    def show_prediction(m_series, series_label, location_label, days_back, days_forward , name=None):
        def compute_prediction(m_series, days_forward, days_back):
            coeff, params = coeff_evaluate_bestfit(m_series, days_back)
            days_back = params['days_back']

            total_days = days_forward + days_back
            count = m_series['count']
            t0, v0 = count.index[-days_back], count[-days_back]
            t_predict = pd.date_range(t0, periods=total_days)
            tmp = np.arange(0, total_days)
            val_predict = v0 * model_func(tmp, coeff)
            sigma_n = 3 * np.sqrt(np.diag(params['pcov']))
            s_predict_below = pd.Series(v0 * model_func(tmp, coeff - sigma_n), t_predict)
            s_predict_above = pd.Series(v0 * model_func(tmp, coeff + sigma_n), t_predict)

            s_predict = pd.Series(val_predict, t_predict)
            return count[-days_back:], s_predict, s_predict_below, s_predict_above

        data, predicted, below, above = compute_prediction(m_series, days_forward, days_back)
        s = 'Predicted {0} in {1} days is {2:.0f} in {3}'.format(series_label, days_forward, predicted[-1], location_label)

        #display(Markdown(s))
        plt.figure(figsize=(12, 6))
        data.plot(label='data', marker='o', markersize=8)
        predicted.plot(label='predicted', linewidth=2)
        plt.fill_between(predicted.index, below.values, above.values, alpha=0.3)
        ax = plt.gca()
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))
        ax.yaxis.grid(True, which='both')
        ax.xaxis.grid(True, which='both')
        title = 'best fit prediction {0} days forward for {1} in {2} as of {3}'.format(days_forward,
                                                                                    series_label, location_label,
                                                                                    last_update)
        plt.title(title)
        plt.legend()
        plt.savefig(os.path.join(fig_dir, name))
        return s #, os.path.join(fig_dir, title) + '.png'

    # In[12]:


    def coeff_evaluate_bestfit(m_series, days_back=None):
        if days_back is None:
            days = [10, 9, 8, 7, 6, 5, 4]
            perr_min = 1e10
            dbmin = -1
            for db in days:
                if db > len(m_series['count']):
                    continue
                _, params = evaluate_bestfit(m_series, db)
                perr = np.sqrt(np.diag(params['pcov']))
                #             perr = params['r2']
                if perr < perr_min:
                    perr_min = perr
                    dbmin = db
            _, params = evaluate_bestfit(m_series, dbmin)
            params['days_back'] = dbmin
        else:
            _, params = evaluate_bestfit(m_series, days_back)
            params['days_back'] = days_back
        return params['popt'][0], params


    def evaluate_bestfit(m_series, days_back):
        x = np.arange(0, days_back, 1)
        y = m_series['count'][-days_back:].values
        y = y / y[0]
        approx, _ = coeff_evaluate_mean(m_series, days_back)
        popt, pcov = curve_fit(model_func, x, y, p0=(approx))
        fitted = model_func(x, popt[0])
        r2 = np.sum((y - fitted) ** 2) / (np.sqrt(np.sum(y ** 2)) * np.sqrt(np.sum(fitted ** 2)))

        params = collections.OrderedDict()
        params['days'] = x
        params['data'] = y
        params['fitted'] = fitted
        params['popt'] = popt
        params['pcov'] = pcov
        params['approx'] = approx
        params['r2'] = r2
        return popt[0], params


    # In[13]:

    work_dir = os.path.join(os.getcwd() , "static")
    days_forward = 7
    display_days_back = 21

    # In[14]:


    last_update = DataColumnsDT[-1]
    last_update = str(pd.Timestamp(last_update)).split(' ')[0]
    last_update_dir = os.path.join(work_dir, 'covid19', last_update)
    os.makedirs(last_update_dir, exist_ok=True)
    print(last_update_dir)
    # In[15]:


    df_confirmed_all.to_csv(os.path.join(last_update_dir, 'confirmed_{0}.csv'.format(last_update)), index=False)
    df_deaths_all.to_csv(os.path.join(last_update_dir, 'deaths_{0}.csv'.format(last_update)), index=False)

    # In[16]:


    # country = input()

    location_label = country
    location_dir = location_label.replace(',', '').replace("'", '')
    fig_dir = os.path.join(last_update_dir, location_dir)
    os.makedirs(fig_dir, exist_ok=True)
    print(fig_dir)
    # os.mknod(os.path.join(fig_dir, country+'.txt' ))
    file = open(os.path.join(fig_dir, country+'.txt' ) , 'w') 


    # In[17]:


    selection = df_confirmed_all['Country/Region'] == country
    df_confirmed = df_confirmed_all[selection]
    df_deaths = df_deaths_all[selection]

    # In[18]:


    series_label = 'confirmed cases'
    m_series = compute_series(df_confirmed)

    # result["item1"] = 
    dis = display_series(m_series, series_label, location_label, fig_dir, display_days_back, name="1")
    file.write(dis + "\n")
    # In[19]:


    day_factor, week_factor, projected_week = multi_factors(m_series, coeff_evaluate_bestfit)
    factor = display_factors(day_factor, week_factor, projected_week, series_label, location_label)
    file.write(factor + "\n")

    # print(factor)

    # In[20]:


    coeff, params = coeff_evaluate_bestfit(m_series, None)
    file.write(str(params['r2']) + "\n" )
    file.write(str(params['days_back']) + "\n")
    # print('r2  = {0}, days_back = {1}'.format(params['r2'], params['days_back']))
    pd.DataFrame({'raw data': params['data'], 'fitted': params['fitted']}).plot(grid=True, title='best fit')

    # In[21]:


    # result["item2"] =  
    predict = show_prediction(m_series, series_label, location_label, params['days_back'], days_forward , name="2")
    # print(a)
    file.write(predict + "\n")

    # In[22]:


    series_label = 'deaths'
    m_series = compute_series(df_deaths)
    # result["item3"] = 
    dis = display_series(m_series, series_label, location_label, fig_dir, display_days_back , name="3")
    file.write(dis + "\n")

    # In[23]:

    try : 
        display_percentage_chart(df_deaths, df_confirmed, "Death", location_label, fig_dir)
    except Exception as e  :
        print("\n\n\n\n ERROR ",e , "\n\n\n\n")
        pass 


    # In[24]:


    day_factor, week_factor, projected_week = multi_factors(m_series, coeff_evaluate_bestfit)
    # result["item5"] =
    factor = display_factors(day_factor, week_factor, projected_week, series_label, location_label)
    # print(factor)
    file.write(factor + "\n")

    # In[25]:


    # result["item6"] = 
    predict = show_prediction(m_series, series_label, location_label, None, days_forward , name="5")
    print(predict + "\n")

    # In[26]:


    total_confirmed = df_confirmed_all.sum()[2:]
    total_confirmed = total_confirmed[total_confirmed > 1]
    total_deaths = df_deaths_all.sum()[2:]
    total_deaths = total_deaths[total_deaths > 1]

    # In[27]:


    plt.figure(figsize=(12, 12))
    plt.subplot(311)
    total_confirmed.plot()
    title = 'total confirmed'
    plt.title(title)
    plt.grid()
    plt.subplot(312)
    total_deaths.plot()
    title = 'total deaths'
    plt.title(title)
    plt.grid()
    plt.subplot(313)

    (total_deaths / total_confirmed * 100).plot()
    title = 'total death rate %'.format(country)
    plt.title(title)
    plt.grid()

    stitle = 'Total Case charts for Worldwide as of {0}'.format(last_update)
    plt.suptitle(stitle, fontsize=16)
    fpath1 = os.path.join(last_update_dir, '{0}.png'.format(stitle))
    
    plt.savefig(fpath1)

    file.close()
    # In[ ]:

    # return result
    # In[ ]:
