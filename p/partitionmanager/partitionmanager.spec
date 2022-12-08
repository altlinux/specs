%def_disable snapshot
%define xdg_name org.kde.partitionmanager

Name: partitionmanager
Version: 22.12.0
Release: alt1

Summary: KDE Partition Manager
License: GPLv3
Group: Graphical desktop/KDE
Url: https://apps.kde.org/%name

%if_disabled snapshot
#Source: https://github.com/KDE/%name/archive/v%version/%name-%version.tar.gz
Source: https://download.kde.org/stable/release-service/%version/src/%name-%version.tar.xz
%else
Vcs: https://github.com/KDE/partitionmanager.git
Source: %name-%version.tar
%endif

%K5init no_altplace appdata

%define qt_ver 5.15.2
%define kpmcore_ver %version

Requires: libkpmcore >= %kpmcore_ver
Requires: qca-qt5-ossl lvm2 cryptsetup polkit

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++ extra-cmake-modules qt5-base-devel >= %qt_ver
BuildRequires: kf5-kcrash-devel kf5-kdoctools-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kdbusaddons-devel
BuildRequires: libpolkitqt5-qt5-devel kf5-kdoctools
BuildRequires: libkpmcore-devel >= %kpmcore_ver libatasmart-devel libblkid-devel
BuildRequires: libappstream-glib-devel

%description
KDE Partition Manager is a utility program to help you manage the disk
devices, partitions and file systems on your computer. It allows you to
easily create, copy, move, delete, resize without losing data, backup and
restore partitions. KDE Partition Manager supports a large number of file
systems, including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.
It makes use of external programs to get its job done, so you might have
to install additional software (preferably packages from your
distribution) to make use of all features and get full support for all
file systems.

%prep
%setup

%build
%K5build

%install
%K5install
%find_lang %name --all-name --with-kde

%files -f %name.lang
%_K5bin/%name
%_K5xdgapp/%xdg_name.desktop
%_K5icon/*/*/apps/%name.*
%_K5cfg/%name.kcfg
%_K5xmlgui/%name/
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/solid/actions/open_in_%name.desktop
%doc README*

%changelog
* Thu Dec 08 2022 Yuri N. Sedunov <aris@altlinux.org> 22.12.0-alt1
- 22.12.0

* Fri Nov 11 2022 Yuri N. Sedunov <aris@altlinux.org> 22.08.3-alt1
- 22.08.3

* Thu Oct 13 2022 Yuri N. Sedunov <aris@altlinux.org> 22.08.2-alt1
- 22.08.2

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 22.08.1-alt1
- 22.08.1

* Thu Aug 18 2022 Yuri N. Sedunov <aris@altlinux.org> 22.08.0-alt1
- 22.08.0

* Thu Jul 07 2022 Yuri N. Sedunov <aris@altlinux.org> 22.04.3-alt1
- 22.04.3

* Thu Jun 09 2022 Yuri N. Sedunov <aris@altlinux.org> 22.04.2-alt1
- 22.04.2

* Thu May 12 2022 Yuri N. Sedunov <aris@altlinux.org> 22.04.1-alt1
- 22.04.1

* Thu Apr 21 2022 Yuri N. Sedunov <aris@altlinux.org> 22.04.0-alt1
- 22.04.0

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 21.12.3-alt1
- 21.12.3

* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 21.12.2-alt1
- 21.12.2

* Fri Jan 07 2022 Yuri N. Sedunov <aris@altlinux.org> 21.12.1-alt1
- 21.12.1

* Thu Dec 09 2021 Yuri N. Sedunov <aris@altlinux.org> 21.12.0-alt1
- 21.12.0

* Thu Nov 04 2021 Yuri N. Sedunov <aris@altlinux.org> 21.08.3-alt1
- 21.08.3

* Fri Oct 08 2021 Yuri N. Sedunov <aris@altlinux.org> 21.08.2-alt1
- 21.08.2

* Thu Sep 02 2021 Yuri N. Sedunov <aris@altlinux.org> 21.08.1-alt1
- 21.08.1

* Thu Aug 12 2021 Yuri N. Sedunov <aris@altlinux.org> 21.08.0-alt1
- 21.08.0

* Thu Jul 08 2021 Yuri N. Sedunov <aris@altlinux.org> 21.04.3-alt1
- 21.04.3

* Thu Jun 10 2021 Yuri N. Sedunov <aris@altlinux.org> 21.04.2-alt1
- 21.04.2

* Thu May 13 2021 Yuri N. Sedunov <aris@altlinux.org> 21.04.1-alt1
- 21.04.1

* Thu Apr 22 2021 Yuri N. Sedunov <aris@altlinux.org> 21.04.0-alt1
- 21.04.0

* Thu Mar 04 2021 Yuri N. Sedunov <aris@altlinux.org> 20.12.3-alt1
- 20.12.3

* Thu Feb 04 2021 Yuri N. Sedunov <aris@altlinux.org> 20.12.2-alt1
- 20.12.2

* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 20.12.1-alt1
- 20.12.1

* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 20.12.0-alt1
- 20.12.0

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt2
- qca-qt5-ossl required (ALT #38105)

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0

* Thu Feb 06 2020 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1.1
- made visible outside KDE (ALT #38046)

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.80.0-alt1
- 3.80.0

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Apr 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for partitionmanager

* Mon Sep 06 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.0.3-alt1
- version 1.0.3

* Mon Apr 26 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.0.2-alt1
- Initial build

