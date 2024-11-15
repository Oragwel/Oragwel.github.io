`# Portfolio Website

![Portfolio Screenshot](assets/img/portfolio/portfolio_screenshot.png)

## Table of Contents
- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Live Demo](#live-demo)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

Welcome to my Portfolio Website! This project showcases my skills, projects, and professional experiences in the field of software development. It is designed to demonstrate my expertise in full-stack web development, data analysis, security systems, and more. The website is fully responsive, interactive, and includes dynamic features to enhance user experience.

## Features

- **Dynamic Resume Section**: Automatically calculates and displays age based on the birthdate.
- **Comprehensive Services Section**: Details a range of services including web development, computer repair, security systems installation, and solar equipment consulting.
- **Testimonials Section**: Displays feedback from clients and collaborators.
- **Skills Section**: Visual representation of my proficiency in various technologies.
- **Stats Section**: Highlights key metrics and achievements.
- **Interactive Portfolio**: Showcases projects with descriptions, images, and links to live demos and source code.
- **Contact Form**: Enables visitors to send messages directly through the website using EmailJS.
- **Floating Social Media Bar**: Features interactive social media icons with real-time notification badges.
- **Interactive Notification Windows**: Allows users to view and interact with recent posts from various social media platforms.

## Technologies Used

### Front-End
- **HTML5**
- **CSS3**
- **JavaScript (ES6)**
- **Bootstrap 5.3.3**
- **AOS (Animate on Scroll)**
- **Swiper.js**
- **GLightbox**
- **EmailJS**

### Back-End
- **Go (Golang)**
- **EmailJS for contact form functionality**

### APIs
- **Twitter API**
- **Facebook Graph API**
- **Instagram Graph API**
- **LinkedIn API**
- **Discord API**

## Live Demo

Check out the live version of my portfolio: [Your Portfolio Link](https://yourusername.github.io/your-portfolio/)

## Installation

### Prerequisites

- **Go (Golang)** installed on your machine. You can download it from [here](https://golang.org/dl/).
- **Git** installed on your machine. You can download it from [here](https://git-scm.com/downloads).
- **EmailJS Account**: Sign up for a free account at [EmailJS](https://www.emailjs.com/).

### Clone the Repository

\`git clone https://github.com/yourusername/your-portfolio.git\`
\`cd your-portfolio\`

### Set Up Environment Variables

Create a `.env` file in the root directory of your project and add your API credentials:

\`\`\`env
TWITTER_BEARER_TOKEN=YOUR_TWITTER_BEARER_TOKEN
FACEBOOK_ACCESS_TOKEN=YOUR_FACEBOOK_ACCESS_TOKEN
INSTAGRAM_ACCESS_TOKEN=YOUR_INSTAGRAM_ACCESS_TOKEN
LINKEDIN_ACCESS_TOKEN=YOUR_LINKEDIN_ACCESS_TOKEN
DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
EMAILJS_USER_ID=YOUR_EMAILJS_USER_ID
EMAILJS_SERVICE_ID=YOUR_EMAILJS_SERVICE_ID
EMAILJS_TEMPLATE_ID=YOUR_EMAILJS_TEMPLATE_ID
\`\`\`

Replace the placeholder values with your actual API tokens and EmailJS credentials.

### Install Dependencies

Navigate to the `handlers` directory and install the necessary Go packages:

\`go get github.com/joho/godotenv\`

### Run the Server

Ensure you are in the root directory of your project and run the Go server:

\`go run main.go\`

The server will start on `http://localhost:8080`.

### Deploy Front-End on GitHub Pages

1. **Push your code to GitHub**:
    \`git add .\`
    \`git commit -m "Initial commit"\`
    \`git push origin main\`
2. **Enable GitHub Pages**:
    - Go to your repository on GitHub.
    - Navigate to **Settings** > **Pages**.
    - Under **Source**, select the branch you want to deploy (e.g., `main`) and the `/root` folder.
    - Click **Save**.

Your website will be available at `https://yourusername.github.io/your-portfolio/`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Feel free to reach out to me via the contact form on the website or through my social media channels:

- **Email**: [tidings@outlook.com](mailto:tidings@outlook.com)
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- **Twitter**: [@yourusername](https://twitter.com/yourusername)
- **Facebook**: [Your Facebook Profile](https://facebook.com/yourprofile)
- **Instagram**: [@yourusername](https://instagram.com/yourusername)
- **Discord**: [Your Discord Handle](https://discord.com/users/yourusername)
``