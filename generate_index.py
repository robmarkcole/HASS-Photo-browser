import glob
import os
import datetime
import argparse

def create_html(www_directory_path : str) -> None:
    www_directory_path = os.path.join(www_directory_path, "")  # If no trailing / add it
    html = "<!DOCTYPE html><html><title>Front Door Images</title>"
    html += "<meta name='viewport' content='width=device-width, initial-scale=1'>"
    html += "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>"
    html += "<link rel='stylesheet' href='css/mycss.css'>"
    html += "<body><div class='w3-content w3-display-container'>"

    files = glob.glob(www_directory_path + "*.jpg")
    for file_path in files:
        time_string = datetime.datetime.utcnow().strftime('%A %d %b %Y %I:%M%p')
        html += "<span class='myDate'>" + time_string + "</span>"
        html += f"<img class='mySlides' src='{www_directory_path}" + os.path.basename(file_path) + "' style='width:100%'>"

    html += "<button class='w3-button w3-black w3-display-left' onclick='plusDivs(-1)'>&#10094;</button>"
    html += "<button class='w3-button w3-black w3-display-right' onclick='plusDivs(1)'>&#10095;</button>"
    html += "</div><script src='js/myscripts.js'></script></body></html>"
    print(html)
    with open("index.html",'w') as index_file:
        index_file.write(html)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an index.html file from a www_directory_path")
    parser.add_argument(
        "--www_directory_path",
        default="/config/www/",
        help="the path to your www directory",
    )
    args = parser.parse_args()
    create_html(args.www_directory_path)
