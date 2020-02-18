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

# todo
* Move pixabay api key from file