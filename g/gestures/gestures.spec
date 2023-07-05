%define uuid com.gitlab.cunidev.Gestures

Name: gestures
Version: 0.3.1
Release: alt1

Summary: A minimal Gtk+ GUI app for libinput-gestures
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://gitlab.com/cunidev/gestures
BuildArch: noarch

Source0: %name-%version.tar.gz
Patch1: conf-as-folder-fix.patch

Requires: python3
Requires: libinput-gestures
Requires: libinput-tools
Requires: xdotool
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: python3-module-pygobject3
BuildRequires: gettext

%description
%summary

%prep
%setup
%patch1 -p1

sed 's|^#!@PYTHON@|#!%__python3|' -i %name/__main__.py

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/glib-2.0/schemas/%uuid.gschema.xml
%_datadir/applications/%uuid.desktop
%_iconsdir/hicolor/scalable/apps/%uuid.svg
%_datadir/appdata/%uuid.appdata.xml

%changelog
* Sat Jun 10 2023 Anton Kurachenko <srebrov@altlinux.org> 0.3.1-alt1
- Initial build for ALT
