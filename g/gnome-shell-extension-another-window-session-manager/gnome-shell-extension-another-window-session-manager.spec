%define _unpackaged_files_terminate_build 1
%define app_id org.gnome.shell.extensions.another-window-session-manager
%define uuid another-window-session-manager@gmail.com

Name: gnome-shell-extension-another-window-session-manager
Version: 47
Release: alt1.git0164e49a

Summary: Close open windows gracefully and save them as a session. 
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://github.com/nlpsuge/gnome-shell-extension-another-window-session-manager
Vcs: https://github.com/nlpsuge/gnome-shell-extension-another-window-session-manager
Source: %name-%version-alt.tar
Patch0: gnome_shell_extension_another_window_session_manager-47-alt-add_gnome47_and_48_support.patch

Requires: gnome-shell >= 45

BuildRequires: /usr/bin/gnome-extensions
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: unzip

BuildArch: noarch

%description
Another Window Session Manager is a GNOME extension for saving and restoring
application sessions on X11/Wayland. It gracefully closes apps,
auto-saves sessions, and restores window positions, workspaces,
and states (maximized, tiled, etc.). Supports multi-monitor and session search.

%prep
%setup -n %name-%version-alt
%patch0 -p1

%build
gnome-extensions pack \
    --extra-source=dbus-interfaces/ \
    --extra-source=icons/ \
    --extra-source=model/ \
    --extra-source=template/ \
    --extra-source=ui/ \
    --extra-source=utils/ \
    --extra-source=closeSession.js \
    --extra-source=constants.js \
    --extra-source=indicator.js \
    --extra-source=moveSession.js \
    --extra-source=openWindowsTracker.js \
    --extra-source=prefsCloseWindow.js \
    --extra-source=prefsColumnView.js \
    --extra-source=prefsWidgets.js \
    --extra-source=prefsWindowPickableEntry.js \
    --extra-source=restoreSession.js \
    --extra-source=saveSession.js \
    --extra-source=windowTilingSupport.js \
    --force

%install
install -d %buildroot%_datadir/gnome-shell/extensions/%uuid

unzip "%uuid.shell-extension.zip" -d "%buildroot%_datadir/gnome-shell/extensions/%uuid/"

mkdir --parents "%buildroot%_datadir/glib-2.0/schemas/"
mv "%buildroot%_datadir/gnome-shell/extensions/%uuid/schemas/%app_id.gschema.xml" "%buildroot%_datadir/glib-2.0/schemas/"
rm -rf "%buildroot%_datadir/gnome-shell/extensions/%uuid/schemas"

%files
%_datadir/gnome-shell/extensions/%uuid/*
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%changelog
* Tue Jun 03 2025 Semen Fomchenkov <armatik@altlinux.org> 47-alt1.git0164e49a
- Initial build.
