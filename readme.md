Updated 2nd May 2024

Major upgrade for updating package versions to be compatible with Python 3.12 

Major implementations : 

1) Front end: Created a docker image for Angular frontend served on Nginx. The static content is available on port 80
2) Back end: Created a docker image for Django to serve on 8000. The model is currently stored locally, will implement full automation and central model store solution (S3, GCS) later.



ARCHITECTURE OVERVIEW : 

1) Set up code on EC2 using Github
2) Create a docker compose file in the code, so we can run the docker compose command from github actions
3) In the actions, the EC2 instance will first pull the latest code from the Github Repo, and then build a docker image out of the new code

Expections from Github Actions : 

1) Each time github repo is updated, start a workflow. 
2) The workflow should run some basic tests, and if they fail then revert the changes

EC2 Set up : 

1) Installing Docker, Docker Compose and Github

# Update your packages
sudo apt update

# Install Docker
sudo apt install docker.io

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Git
sudo apt install git

2) Pull the github code to EC2 instance (As the repo is public, no git authentication needed for pull)
git clone https://github.com/yourusername/yourrepository.git

