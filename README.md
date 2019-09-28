# HASS-Photo-browser
Browse `jpg` photos in your Home Assistant www folder.

Creates an `index.html` file that displays all the photos in your `www` folder. 

Taken from the thread https://community.home-assistant.io/t/image-file-browser-view-for-ha-front-end/41877/12

Credit Ken Depledge

## Usage
Place the python script and `css` and `js` folders from this repository in your Home Assistant `/config/www` directory. Place your images in a subdirectory of `www` called `images` (or another subdirectory in `www`). To manually create the `index.html` file run:
```
$ python3 generate_index.py --image_directory_path /Users/robin/.homeassistant/www/images
```

Alternatively use an automation to recreate the `index.html` file when a new photo is available. The automation is triggered by the [folder_watcher](https://www.home-assistant.io/components/folder_watcher/) integration. In your `automations.yaml`:

```yaml
- id: '1569591328937'
  alias: Rebuild image index
  trigger:
  - event_data:
      event_type: created
    event_type: folder_watcher
    platform: event
  condition: []
  action:
  - event: HASS_FOLDER_WATCH
    event_data:
      name: hassfolder
```

Display the file on the Home Assistant front end using an Lovelace iframe card using `url: /local/index.html`:

## Troubleshooting
* Problem: the images haven't been updated in the iframe. Solute: In Chrome `More tools - Clear browsing data - Clear cached images and data`