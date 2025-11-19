%define _unpackaged_files_terminate_build 1

Name: nitrogen
Version: 1.6.1
Release: alt1

Summary: Background browser and setter for X windows
License: GPL-2.0-or-later
Group: Graphics
URL: https://github.com/l3ib/nitrogen
Vcs: https://github.com/l3ib/nitrogen

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgtkmm2-devel
BuildRequires: libXinerama-devel
BuildRequires: libappstream-glib

%description
A background browser and setter for X windows that can be used in two
modes: browser and recall. It features Multihead and Xinerama awareness,
a recall mode to be used in start up scripts, uses the freedesktop.org
standard for thumbnails, can set the GNOME background, command line set
modes for use in scripts, inotify monitoring of browse directory, lazy
loading of thumbnails to conserve memory and an 'automatic' set mode
which determines the best mode to set an image based on its size.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
appstream-util validate-relax --nonet \
  %buildroot%_datadir/appdata/nitrogen.appdata.xml

%files
%_bindir/nitrogen
%_datadir/appdata/nitrogen.appdata.xml
%_datadir/applications/nitrogen.desktop
%_iconsdir/hicolor/128x128/apps/nitrogen.png
%_iconsdir/hicolor/16x16/actions/wallpaper-centered.png
%_iconsdir/hicolor/16x16/actions/wallpaper-scaled.png
%_iconsdir/hicolor/16x16/actions/wallpaper-tiled.png
%_iconsdir/hicolor/16x16/actions/wallpaper-zoomed.png
%_iconsdir/hicolor/16x16/devices/video-display.png
%_iconsdir/hicolor/16x16/mimetypes/image-x-generic.png
%_iconsdir/hicolor/22x22/apps/nitrogen.png
%_miconsdir/nitrogen.png
%_niconsdir/nitrogen.png
%_liconsdir/nitrogen.png
%_man1dir/nitrogen.1.xz

%changelog
* Mon Nov 19 2025 Pavel Petrykin <silverducks@altlinux.org> 1.6.1-alt1
- Initial build for Alt Linux.
