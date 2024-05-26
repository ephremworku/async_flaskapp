# use Nginx image

FROM nginx

# remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# replace it with the new nginx.conf
COPY nginx.conf etc/nginx/conf.d/