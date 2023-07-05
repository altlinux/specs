Name: libinput-gestures
Version: 2.74
Release: alt1

Summary: Actions gestures on your touchpad using libinput
License: GPL-2.0-only
Group: System/Libraries
URL: https://github.com/bulletmark/libinput-gestures
BuildArch: noarch

Source0: %name-%version.tar.gz

Requires: libinput-tools
Requires: python3
Requires: xdotool
Requires: wmctrl
BuildRequires(pre): rpm-build-python3

%description
Libinput-gestures is a utility which reads libinput gestures from your touchpad
and maps them to gestures you configure in a configuration file. Each gesture
can be configured to activate a shell command which is typically an xdotool
command to action desktop/window/application keyboard combinations and commands.

See the examples in the provided libinput-gestures.conf file.
My motivation for creating this is to use triple swipe up/down to switch GNOME
workspaces, and triple swipe left/right to go backwards/forwards in my browser,
as per the default configuration.

This small and simple utility is only intended to be used temporarily until
GNOME and other DE's action libinput gestures natively. It parses the output of
the libinput-list-devices and libinput-debug-events utilities so is a little
fragile to any version changes in their output format.

%prep
%setup

%build

%install
%makeinstall_std

%files
%_sysconfdir/*
%_bindir/%name
%_bindir/%name-setup
%_iconsdir/hicolor/128x128/apps/*
%_datadir/applications/*
%dir %_docdir/%name
%_docdir/%name/*
%_prefix/lib/systemd/user/%name.service

%changelog
* Sat Jun 10 2023 Anton Kurachenko <srebrov@altlinux.org> 2.74-alt1
- Initial build for ALT
