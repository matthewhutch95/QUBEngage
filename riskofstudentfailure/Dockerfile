# Use the official Ruby image as the base image
FROM ruby:3.0

# Set the working directory inside the container
WORKDIR /app

RUN gem install webrick

# Copy the application code into the container
COPY . .

# Expose the port that WEBrick will run on
EXPOSE 4567

# Command to run the application
CMD ["ruby", "app.rb"]
