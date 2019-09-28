# HASS-Photo-browser
Browse `jpg` photos in your Home Assistant `www/images` folder.

Taken from the thread https://community.home-assistant.io/t/image-file-browser-view-for-ha-front-end/41877/12

Credit [Ken Depledge](https://community.home-assistant.io/u/ken.d/summary)

## Usage
Place the python script `generate_index.py` and the `css` and `js` folders from this repository in your Home Assistant `config/www` directory (create this if if doesn't exist). Place your images in a subdirectory of `www` called `images`. Your directory structure is then:
```
config
    www
        generate_index.py
        css folder
        js folder
    images
        contains the jpg images
```

An `index.html` file is used to serve images on the Home Assistant front end. Use a [shell_command](https://www.home-assistant.io/components/shell_command/) to create this file by adding to `configuration.yaml`:
```
shell_command:
  update_images: python3 /user/.homeassistant/www/generate_index.py --image_directory_path /user/.homeassistant/www/images
```

Manually call the shell command via the `Services` tool in `Developer Tools`. Alternatively use an automation triggered by the [folder_watcher](https://www.home-assistant.io/components/folder_watcher/) integration. In your `automations.yaml`:

NEEDS UPDATING
```yaml

```

Display the images on the Home Assistant front end using an Lovelace [iframe card](https://www.home-assistant.io/lovelace/iframe/) using `url: /local/index.html`:

<p align="center">
<img src="https://github.com/robmarkcole/HASS-Photo-browser/blob/master/assets/usage.png" width="500">
</p>

## Troubleshooting
* **Problem**: the images dont show in the iframe. **Solution**: It might take a little time before they appear on restart of HA.
* **Problem**: the images haven't been updated in the iframe. **Solution**: In Chrome `More tools - Clear browsing data - Clear cached images and data`