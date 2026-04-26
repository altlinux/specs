%define _unpackaged_files_terminate_build 1

Name: dpscreenocr
Version: 1.5.1
Release: alt1

Summary: Program to recognize text on screen
License: Zlib
Group: Office
Url: https://github.com/danpla/dpscreenocr

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(tesseract)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: qt5-base-devel
BuildRequires: pandoc

%description
dpScreenOCR is a program to recognize text on the screen

%prep
%setup
sed -i 's|^Categories=.*|Categories=Graphics;OCR;Scanning;|' data/dpscreenocr.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc LICENSE.txt README.md doc/changelog.txt
%_bindir/*
%_desktopdir/%{name}.desktop
%exclude %_datadir/doc/%name/LICENSE.txt
%exclude %_datadir/doc/%name/changelog.txt
%dir %_datadir/doc/%name
%_datadir/doc/%name/manual.html
%dir %_datadir/doc/%name/manual-data
%_datadir/doc/%name/manual-data/manual.css
%_datadir/doc/%name/manual-data/split.svg
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.1-alt1
- New version 1.5.1.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt2
- Applied repocop fix for freedesktop-desktop

* Sun Jun 01 2025 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
