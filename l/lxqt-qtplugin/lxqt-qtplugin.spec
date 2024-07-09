# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-qtplugin
Version: 2.0.0
Release: alt1

Summary: LxQt platform integration plugin for Qt
License: LGPL-2.1
Group: Graphical desktop/Other

Url: https://github.com/lxqt/lxqt-qtplugin
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: liblxqt-devel >= 2.0.0
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: libqt6xdg-devel
BuildRequires: libdbusmenu-lxqt-devel
BuildRequires: libfm-qt6-devel

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
%_libdir/qt6/plugins/platformthemes/libqtlxqt.so
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0

* Sat Apr 13 2024 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- New version 1.4.1.

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Sat Jun 06 2020 Anton Midyukov <antohami@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Tue Aug 14 2018 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt2
- rebuild with new Qt

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt3
- rebuilt against current qt

* Mon Aug 21 2017 Michael Shigorin <mike@altlinux.org> 0.11.0-alt2
- rebuilt against current qt (closes: #33756)

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- whoops, missed qtxdg somehow

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

