%define _unpackaged_files_terminate_build 1

Name: freelib
Version: 6.2.0
Release: alt1

Summary: Freelib is book library manager
License: GPL-3.0
Group: Office
Url: https://github.com/petrovvlad/freeLib

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: quazip-qt6-devel
BuildRequires: qt6-svg-devel

%description
%summary

Freelib has the following features:

* Creation of user book libraries from FB2(.ZIP), EPUB, FBD files.
* Conversion to AZW3 (KF8), MOBI, MOBI7 (KF7), EPUB.
* Support of multiple book libraries.
* Import of book libraries from inpx-files.
* Book search and filtering.
* OPDS and Web servers (needs QHttpServer).
* Saving books into selected folder.
* Different export settings for multiple devices.
* Tags for book, author, series with tag-based filtering.
* Book formating support (fonts, initial cap, headers, hyphenation, footnotes)
* Bookreading using external applications. User can settup diffrent applications
  for each format.

# TODO package submodule src/SmtpClient to
#      enable "Sending selected book files to email."

%prep
%setup
%patch -p1
sed -i 's|^Categories=.*|Categories=Office;Database;Viewer;|' data/freelib.desktop

%build
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=None \
       -DCMAKE_INSTALL_PREFIX=/usr \
       -DFREELIB_QT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md doc
%_bindir/%name
%_desktopdir/%{name}.desktop
%dir %_datadir/%name
%dir %_datadir/%name/fonts
%_datadir/%name/fonts/*
%dir %_datadir/%name/help
%_datadir/%name/help/*.md
%dir %_datadir/%name/translations
%_datadir/%name/translations/*
%_datadir/metainfo/%{name}.appdata.xml
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Aug 23 2025 Nikolay Strelkov <snk@altlinux.org> 6.2.0-alt1
- New version 6.2.0.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 6.1.0-alt2
- Applied repocop fix for freedesktop-categories

* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 6.1.0-alt1
- Initial build for Sisyphus (closes: #54218)
