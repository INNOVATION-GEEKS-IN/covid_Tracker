from django.shortcuts import render, redirect
from django.http import HttpResponse 
from pandas import read_csv

# from .models import Program_Questions, INPUTS_AND_OUTPUTS

from datetime import date 
from datetime import timedelta 
import os


yesterday = date.today() - timedelta(days=1)
yesterday = '{}-{}-{}'.format(str(yesterday.year).zfill(4) , str(yesterday.month).zfill(2), str(yesterday.day).zfill(2))

def contact_us(request):
    return render(request, "Home/contact_us.html", {})

def home(request) :
    return render(request, "Home/home.html" , {})


def tracker(request) :

    file_path = os.path.join("static/covid19" , yesterday, "confirmed_" + yesterday + '.csv' )
    if os.path.isfile(file_path) :
        link = file_path
    else :
        link = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    countries_list = list(read_csv(link, usecols= ["Country/Region"], dtype={"Country/Region":"category"} ).dropna(axis = 1, how = 'all')["Country/Region"].unique())
    return render(request, "Home/covid_predections.html", {"countries_list" : countries_list})

def predict_Country(request):

    if not request.GET["country"]:
        return redirect("/tacker/")
    
    file_dir  = os.path.join(  'static', 'covid19' , yesterday , )
    img_dir   = os.path.join(  'covid19' , yesterday , )
    # os.mknod(os.path.join(img_dir, request.GET["country"], request.GET["country"]+'.txt' ))
    
    if  os.path.isdir( os.path.join(file_dir, request.GET["country"])) : 
        info_file = open(os.path.join(file_dir,request.GET["country"], request.GET["country"] +".txt").replace('\\', "/") , 'r')
        result = {
            "country"           : request.GET["country"],
            "yesterday"         : yesterday,
            "main_dir_path"     : file_dir , 
            "country_dir_path"  : os.path.join(file_dir ,request.GET["country"] ),
            "main_dir_content"  : os.listdir(file_dir), 
            "img_1"             : os.path.join(img_dir, request.GET["country"] ,"1.png" ).replace('\\', '/') ,
            "img_2"             : os.path.join(img_dir, request.GET["country"] ,"2.png" ).replace('\\', '/') ,
            "img_3"             : os.path.join(img_dir, request.GET["country"] ,"3.png" ).replace('\\', '/') ,
            "img_4"            : os.path.join(img_dir, request.GET["country"] ,"5.png" ).replace('\\', '/') ,
            "img_5"             : os.path.join(img_dir, "Total Case charts for Worldwide as of {}.png".format(yesterday)),
        
            "confirmed_cases_number"   : info_file.readline(),
            "confirmed_cases_factor"   : info_file.readline(),
            "r2"                       : info_file.readline(),
            "days_back"                : info_file.readline(),
            "confirmed_death_number"   : info_file.readline(),
            "confirmed_death_factor"   : info_file.readline(),                      
        }

        result["country_dir_content"] = [ os.path.join('covid19',yesterday,request.GET["country"] , link) for link in sorted(os.listdir( os.path.join(file_dir ,request.GET["country"]))) ]
        info_file.close()
        return render(request , "result/result.html" ,result )
    
    from tracker.predict_cases import main
    main(request.GET["country"] )
    info_file = open(os.path.join(file_dir,request.GET["country"], request.GET["country"] +".txt").replace('\\', "/") , 'r')

    # print(""" \n\n\n Finished \n\n\n """)
    result = {
            "country"           : request.GET["country"],
            "yesterday"         : yesterday,
            "main_dir_path"     : file_dir , 
            "country_dir_path"  : os.path.join(file_dir ,request.GET["country"] ),
            "main_dir_content"  : os.listdir(file_dir) , 
            "img_1"             : os.path.join(img_dir, request.GET["country"] ,"1.png" ).replace('\\', '/')  ,
            "img_2"             : os.path.join(img_dir, request.GET["country"] ,"2.png" ).replace('\\', '/')  ,
            "img_3"             : os.path.join(img_dir, request.GET["country"] ,"3.png" ).replace('\\', '/')  ,
            "img_4"             : os.path.join(img_dir, request.GET["country"] ,"5.png" ).replace('\\', '/')  ,
            "img_5"             : os.path.join(img_dir, "Total Case charts for Worldwide as of {}.png".format(yesterday)),
        
            "confirmed_cases_number"   : info_file.readline(),
            "confirmed_cases_factor"   : info_file.readline(),
            "r2"                       : info_file.readline(),
            "days_back"                : info_file.readline(),
            "confirmed_death_number"   : info_file.readline(),
            "confirmed_death_factor"   : info_file.readline(),                      
        }
    # print(result["img_5"] , "\n\n")
    result["country_dir_content"] =[ os.path.join('covid19',yesterday,request.GET["country"] , link) for link in sorted(os.listdir( os.path.join(file_dir ,request.GET["country"]))) ]
    return render(request , "result/result.html" ,result )
    
def compare(request):
    return render(request,'Home/compare.html' , {}) 

def vaccinations(request, id=1):
    from .vaccination import sort_values_by 
    # if request.POST["vaccination"] is None :
    return render(request , "vaccination/vaccination.html" ,sort_values_by(id) )

def age_predict(request) :
    return render(request, 'age_predict/age-predict.html', {} )

