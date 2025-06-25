%define extension_uuid focused-window-dbus@flexagoon.com

Name: gnome-shell-extension-focused-window-dbus
Version: 8
Release: alt1
Summary: Exposes a D-Bus method to get active window title and class
License: MIT
Group: Graphical desktop/GNOME
Url: https://extensions.gnome.org/extension/5592/focused-window-d-bus
VCS: https://github.com/flexagoon/focused-window-dbus

Source: %name-%version.tar

BuildArch: noarch

%description
This GNOME Shell extension allows you to get the currently focused window
using a D-Bus call. This allows you to get the focused window on Wayland,
where there is no other way to do this.

%prep
%setup

%build
# not needed

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%extension_uuid
cp extension.js metadata.json %buildroot%_datadir/gnome-shell/extensions/%extension_uuid

%files
%_datadir/gnome-shell/extensions/%extension_uuid
%doc LICENSE

%changelog
* Wed Jun 25 2025 Alexander Makeenkov <amakeenk@altlinux.org> 8-alt1
- Initial build for ALT.
