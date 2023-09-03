# Lyft Fleet Service Component 🚗

## Starter Repo
[This repo](https://github.com/vagabond-systems/forage-lyft-starter-repo) has everything to get started on the program.

## Overview 🌟
This project serves as a crucial component for Lyft’s emerging rental fleet logistics system. Its primary function is to determine when a car in the fleet needs to be serviced. The system evaluates various factors like the car's engine, battery, and even tire condition. The architecture is built to be flexible, allowing for the easy addition of future criteria.

## Updated UML Diagram 📊
Refactor the codebase with the help of the updated UML diagram.
![UML](https://github.com/z-q-ying/forage-lyft-back-end-engineering/assets/116849653/3e09c0ef-8370-4781-959b-019a6844983f)

## Service Criteria ⚙️
### Engine 🛠
<ul>
  <li>Capulet Engine: Requires servicing after every 30,000 miles</li>
  <li>Willoughby Engine: Requires servicing after every 60,000 miles</li>
  <li>Sternman Engine: Service only when the warning indicator is on</li>
</ul>

### Battery 🔋
<ul>
  <li>Spindler Battery: Requires servicing every 2 years</li>
  <li>Nubbin Battery: Requires servicing every 4 years</li>
</ul>

### Tires 🎡
The tire servicing criteria have been successfully implemented, showcasing the program's extensible design. Tire Servicing Criteria:
<ul>
  <li>Types of Tires: Currently, the Lyft fleet uses two kinds of tires - Carrigan and Octoprime</li>
  <li>Tire Wear Sensor Data: The fleet's new sensors generate an array of four numbers, each between 0 and 1. These numbers represent the wear level of each tire</li>
  <li>Carrigan Tires: Should be serviced if any value in the tire wear array is 0.9 or higher</li>
  <li>Octoprime Tires: Should be serviced if the sum of all values in the tire wear array is 3 or higher</li>
</ul>

### Car Models 🚗
<ul>
  <li>Calliope: Features Capulet Engine and Spindler Battery</li>
  <li>Glissade: Features Willoughby Engine and Spindler Battery</li>
  <li>Palindrome: Features Sternman Engine and Spindler Battery</li>
  <li>Rorschach: Features Willoughby Engine and Nubbin Battery</li>
  <li>Thovex: Features Capulet Engine and Nubbin Battery</li>
</ul>

### Extensibility 🛠️
The system is architected for **extensibility**. This makes it simple to introduce new criteria for servicing, or even add new car models to the fleet. As a case in point, criteria for tire servicing can be incorporated into the system without much hassle.

### Certificate of Completion
Feel free to check out my certificate of completion [here](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Lyft/xSw9echtixLAoPdsH_Lyft_XH88dvsP4RZbP5AAk_1693698920990_completion_certificate.pdf) 🏆 !
