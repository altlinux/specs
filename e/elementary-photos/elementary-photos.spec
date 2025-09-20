%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.photos

%define _libexecdir %_prefix/libexec

Name: elementary-photos
Version: 8.0.1
Release: alt1

Summary: Photo viewer and organizer designed for elementary OS
License: LGPL-2.1
Group: Graphical desktop/Other
Url: https://github.com/elementary/photos

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gexiv2)
BuildRequires: pkgconfig(geocode-glib-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libgphoto2)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: vapi(granite)
BuildRequires: libgomp-devel
BuildRequires: gcc-c++

%description
Photos is a digital photo organizer designed for the Pantheon desktop
environment. It allows you to import photos from disk or camera, organize
them in various ways, view them in full-window or fullscreen mode, and
export them to share with others. It is able to manage a lot of different
image formats, also including raw CR2 files.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md THANKS
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_desktopdir/%{appname}.viewer.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_iconsdir/hicolor/*/apps/%{appname}.viewer.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%_libdir/io.elementary.photos/plugins/libpantheon-photos-transitions.so
%_libexecdir/io.elementary.photos/video-thumbnailer

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
