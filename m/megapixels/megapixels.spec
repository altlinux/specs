%define _unpackaged_files_terminate_build 1
%define git_rev 7741389

Name:    megapixels
Version: 1.5.2
Release: alt1.git%git_rev

Summary: The GTK camera application
License: GPL-3.0+
Group:   Video
Url:     https://github.com/kgmt0/megapixels

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: libgtk4-devel
BuildRequires: libfeedback-devel
BuildRequires: libtiff-devel
BuildRequires: libzbar-devel
BuildRequires: libepoxy-devel
BuildRequires: libXrandr-devel
BuildRequires: gobject-introspection-devel

%description
A GTK4 camera application that knows how to deal with the media request api. It
uses opengl to debayer the raw sensor data for the preview.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/*
%_desktopdir/*.desktop
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/%name
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/*.metainfo.xml

%changelog
* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1.git7741389
- Initial build for Sisyphus.
