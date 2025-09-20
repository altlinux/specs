%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.camera

Name: elementary-camera
Version: 8.0.2
Release: alt1

Summary: Camera app designed for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/camera

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: vapi(libcanberra)

%description
%summary

%prep
%setup
sed -i 's|^Categories=.*|Categories=GNOME;GTK;AudioVideo;Recorder;|' data/io.elementary.camera.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc COPYING README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus
