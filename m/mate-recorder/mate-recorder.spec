%define _unpackaged_files_terminate_build 1

Name: mate-recorder
Version: 1.0.0
Release: alt1

Summary: Screen recording tool based on MATE Desktop
License: GPL-3.0
Group: Graphical desktop/MATE
Url: https://github.com/zhuyaliang/mate-recorder

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libwnck-3.0)

Requires: x264
Requires: gst-plugins-ugly1.0

%description
%summary with Ayatana Indicator support.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %{name}.lang
%doc COPYING README.md
%_bindir/*
%_desktopdir/%{name}.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*%{name}.appdata.xml
%_datadir/dbus-1/interfaces/*.xml

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
