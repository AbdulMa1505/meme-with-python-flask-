# meme-with-python-flask-
A  Flask app that fetches memes from the Meme API and displays a meme image along with its subreddit
# This is a no-nonsense Flask app that fetches memes from the Meme API and displays a meme image along with its subreddit. It's a straightforward example meant to get you started with Flask, virtual environments, and using APIs.
# Features
- Meme Fetching: Pulls a meme image URL and its subreddit from the Meme API.
- Dynamic HTML: Uses a Jinja2 template (index.html) to render the meme and subreddit on a webpage.
 #Prerequisites
- Python 3.x (check with python3 --version)
- pip (comes with Python)
- Flask and requests packages
# Notes & Considerations
- Code Tweaks:
If you run into issues with the page not displaying the template, try moving the route decorator to the index() function instead of getMeme().

- Debug Mode:
The app runs with debug=True which is great for development but remember to disable it in a production setting.

# Future Improvements:

- Better error handling for API calls.
- UI/UX enhancements on the front end.
- Possibly display the subreddit as text rather than as an image.
