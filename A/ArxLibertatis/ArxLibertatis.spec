# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     ArxLibertatis
Version:  1.2
Release:  alt2

Summary:  Cross-platform port of Arx Fatalis, a first-person role-playing game
License:  GPL-3.0-or-later
Group:    Games/Other
Url:      https://github.com/arx/ArxLibertatis

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libfreetype-devel
BuildRequires: libSDL2-devel
BuildRequires: libGLEW-devel
BuildRequires: libepoxy-devel
BuildRequires: libopenal-devel
BuildRequires: boost-devel-headers
BuildRequires: boost-interprocess-devel
BuildRequires: cppunit-devel
BuildRequires: libglm-devel
BuildRequires: inkscape
BuildRequires: optipng
BuildRequires: ImageMagick

%description
%summary.

%package devel
Summary: Developments files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Developments files for %name.

%prep
%setup

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

# Remove unpackages files
rm -r %buildroot%_datadir/blender

%check
%cmake_build --target check

%files
%_bindir/*
%_prefix/libexec/arxtool
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_libdir/*.so.*
%_gamesdatadir/arx
%_man1dir/*
%_man6dir/*
%doc *.md

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Sat Jan 22 2022 Anton Midyukov <antohami@altlinux.org> 1.2-alt2
- 1.2 Release

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.2-alt1.20200607.1
- NMU: spec: adapted to new cmake macros.

* Sat Jun 13 2020 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20200607
- Initial build for Sisyphus
