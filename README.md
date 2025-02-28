# NetBox IPAM Tree Plugin

A NetBox plugin that provides a hierarchical tree view of your IP Address Management (IPAM) data. This plugin enhances NetBox's IPAM functionality by offering a more intuitive way to visualize and navigate your IP address hierarchy.

## Features

- Hierarchical tree view of prefixes and IP addresses
- Integrated with NetBox's permission system
- Display of key information including description, status, role, utilization, site, and VLAN
- Interactive expandable/collapsible tree nodes

## Screenshots

[Screenshots to be added]

## Requirements

- NetBox 4.2 or later
- Python 3.10 or later

## Installation

### 1. Install the package

```bash
# Download the plugin
git clone https://github.com/Kani999/netbox-ipamtree.git
cd netbox-ipamtree

# Install the plugin
pip install -e .
```

### 2. Enable the plugin in NetBox

Add the plugin to your NetBox configuration. Edit your `configuration.py` file:

```python
PLUGINS = [
    'ipamtree',
]

# Optional: Plugin configuration settings
PLUGINS_CONFIG = {
    'ipamtree': {
        # Add any plugin-specific settings here
    }
}
```

### 3. Run migrations and collect static files

```bash
# Apply any migrations
python /opt/netbox/netbox/manage.py migrate

# Collect static files
python /opt/netbox/netbox/manage.py collectstatic --no-input
```

### 4. Restart NetBox services

```bash
# If using supervisord
supervisorctl restart netbox netbox-rq

# If using systemd
systemctl restart netbox netbox-rq
```

## Usage

After installation, a new "IPAM Tree" menu item will appear in the navigation menu. Click on it to access the tree view of your IPAM data.

The tree view provides the following information for each prefix:
- Description/Device
- Status
- Role
- Utilization
- Site
- VLAN

You can expand and collapse tree nodes to explore your IP address hierarchy.

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/Kani999/netbox-ipamtree.git
cd netbox-ipamtree

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -e .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
