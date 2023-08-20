# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: picom-conf
Version: 0.17.0
Release: alt1.20230814

Summary: GUI configuration tool for picom X composite manager
License: LGPL-2.1-or-later
Group: Graphical desktop/Other

Url: https://github.com/qtilities/picom-conf
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qtilitools
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: pkgconfig(libconfig++) pkgconfig(libconfig)

Obsoletes: compton-conf =< 0.17.0

Requires: picom

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_datadir/metainfo/picom_conf.appdata.xml
%_datadir/%name/
%_desktopdir/picom_conf.desktop
%doc AUTHORS COPYING README.md

%changelog
* Sun Aug 20 2023 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1.20230814
- New version
- Fix License
- Clean Packager

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Mon Apr 27 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Tue Mar 20 2018 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- rebuilt against current libraries

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

