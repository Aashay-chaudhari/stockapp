Updated 2nd May 2024

Major upgrade for updating package versions to be compatible with Python 3.12 

Major implementations : 
1) Front end: Created a docker image for Angular frontend served on Nginx. The static content is available on port 80
2) Back end: Created a docker image for Django to serve on 8000. The model is currently stored locally, will implement full automation and central model store solution (S3, GCS) later.

