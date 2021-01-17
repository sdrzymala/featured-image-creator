# featured-image-creator
Simple website to generate featured-images for wordpress blog
![app screenshoot](misc/app_screenshoot_1.png)


# what's inside
   * python - language
   * flask - framework
   * pixabay - api
   * docker - run, test and host

# where
Currently avaliable at: [https://featured-image-creator.azurewebsites.net/](https://featured-image-creator.azurewebsites.net/)

# docker
build:   
`docker build . --tag img-featured-image-creator -f dockerfiles/standard.Dockerfile`      

`docker build . --tag img-featured-image-creator-alpine -f dockerfiles/alpine.Dockerfile`   

run:   
`docker run -d -p 5000:5000 img-featured-image-creator`   

`docker run -d -p 5000:5000 img-featured-image-creator-alpine`   

remove, rebuild and run:   
`docker container rm imagegenerator --force && docker build . --tag img-featured-image-creator-alpine -f dockerfiles/alpine.Dockerfile && docker run -d -p 5000:5000 --name imagegenerator img-featured-image-creator-alpine`   


# deployment
0. Prepare 
    * Make sure docker deamon is running 
    * Build image locally   
    `docker build . --tag img-featured-image-creator-alpine -f dockerfiles/alpine.Dockerfile`
1. Push image to ACR
    * Login to Azure  
    `az login`
    * Login to Azure Container Registry   
    `az acr login --name cregsdwebapp`
    * Tag local image  
    `docker tag img-featured-image-creator-alpine cregsdwebapp.azurecr.io/python/img-featured-image-creator-alpine`
    * Push local image to Azure Container Registry   
    `docker push cregsdwebapp.azurecr.io/python/img-featured-image-creator-alpine`
2. Run app
    * First time:
        * Create web app on azure
        * Configure web app - add WEBSITES_PORT:5000 to application settings
    * Second time:
        * Restart app

# todo
* Move pixabay api key from file
* Automate deployment