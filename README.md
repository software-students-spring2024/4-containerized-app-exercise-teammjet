![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)
![Machine Learning Client CI](https://github.com/software-students-spring2024/4-containerized-app-exercise-teammjet/actions/workflows/ml_client.yml/badge.svg)
![Web App CI/CD](https://github.com/software-students-spring2024/4-containerized-app-exercise-teammjet/actions/workflows/web_app.yml/badge.svg)


# Campus Exchange Auto-Labeler
The Campus Exchange Auto-Labeler is an extension of our group's project for exercise 2, which allows college students to trade items on a platform shared by other college students. Users simply upload a photo of the item they wish to trade, and the Auto-Labeler effortlessly generates a string description of the item which can be used to aid purchasing decisions on Campus Exchange (TM).

- **Web App:** Users upload pictures of items and the app returns a categorized label for each item
- **Machine Learning Client:** Alexnet library for labeling photos
- **Database:** For each item, a MongoDB database stores photo and an string representation of its respective category generated by machine learning algorithm

# How to Run

Create and navigate to local repository. Then run command below, which removes any containers whose ports are needed.

    docker-compose down

To install the required dependencies and run the program, run the following command.

    docker-compose up --build

To open the app, open a web browser and navigate to [localhost:5001](http://localhost:5001/). Do not go to the address that the program tells you to navigate to.

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.


# Contributors

- [Eleazer Neri](https://github.com/afknero)
- [Terry Qiu](https://github.com/TerryQtt)
- [Marc Etter](https://github.com/Morcupine)
- [Johan Gallardo](https://github.com/JohanGallardo)
