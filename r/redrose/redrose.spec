%define _unpackaged_files_terminate_build 1

Name: redrose
Version: 0.5.25
Release: alt1

Summary: ABC notation music integrated environment
License: GPL-3.0
Group: Sound
Url: http://brouits.free.fr/redrose/
VCS: https://github.com/be1/redrose

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(drumstick-file)
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(fluidsynth)

Requires: /usr/bin/abcm2ps
Requires: /usr/bin/abc2midi
Requires: fluid-soundfont-gm
Requires: ghostscript-common

%description
%summary

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Music;AudioVideo;|" app/redrose.desktop

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/scalable/apps/%{name}.svg
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/*%{name}.metainfo.xml
%_datadir/mime/packages/*%{name}.xml

%changelog
* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.25-alt1
- Initial build for Sisyphus
