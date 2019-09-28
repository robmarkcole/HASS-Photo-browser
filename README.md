# HASS-Photo-browser
Browse photos in your Home Assistant www folder.

Creates an `index.html` file that displays all the photos in your www folder. 

Taken from the thread https://community.home-assistant.io/t/image-file-browser-view-for-ha-front-end/41877/12
Credit Ken Depledge

## Usage
Use an automation to recreate the `index.html` file when a new photo is available. The automation is triggered by the [folder_watcher](https://www.home-assistant.io/components/folder_watcher/) integration. In your `automations.yaml`:

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
