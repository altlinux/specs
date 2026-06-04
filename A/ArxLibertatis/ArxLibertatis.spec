# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 0

Name:     ArxLibertatis
Version:  1.2.1
Release:  alt1

Summary:  Cross-platform port of Arx Fatalis, a first-person role-playing game
License:  GPL-3.0-or-later
Group:    Games/Other
URL:      https://github.com/arx/ArxLibertatis
VCS:      https://github.com/arx/ArxLibertatis

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

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
BuildRequires: ImageMagick-tools

%description
%summary.

%package -n libArxIO%sover
Summary: Shared library for %name
Group: System/Libraries

%description -n libArxIO0
Shared library for %name.

%package devel
Summary: Developments files for %name
Group: Development/Other
Requires: libArxIO%sover = %EVR

%description devel
Developments files for %name.

%prep
%setup
%autopatch -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

# Remove unpackaged files
rm -r %buildroot%_datadir/blender

%check
%cmake_build --target check

%files
%_bindir/*
%_prefix/libexec/arxtool
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_gamesdatadir/arx
%_man1dir/*.1.*
%_man6dir/*.6.*
%doc *.md

%files -n libArxIO%sover
%_libdir/libArxIO.so.%sover
%_libdir/libArxIO.so.%version

%files devel
%_libdir/libArxIO.so
%_includedir/*

%changelog
* Mon Apr 13 2026 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- New version 1.2.1.
- New subpackage with library.

* Sat Jan 22 2022 Anton Midyukov <antohami@altlinux.org> 1.2-alt2
- 1.2 Release

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.2-alt1.20200607.1
- NMU: spec: adapted to new cmake macros.

* Sat Jun 13 2020 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20200607
- Initial build for Sisyphus
