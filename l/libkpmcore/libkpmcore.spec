%define _name kpmcore
%define xdg_name org.kde.%_name
%define _libexecdir %_prefix/libexec

Name: lib%_name
Version: 24.05.2
Release: alt1

Summary: KDE Partition Manager core library
Group: System/Libraries
License: GPL-3.0-or-later
Url: https://github.com/KDE/%_name

Source: https://download.kde.org/stable/release-service/%version/src/%_name-%version.tar.xz
#Source: %url/archive/v%version/%_name-%version.tar.gz

Provides: %_name = %EVR

%define blkid_ver 2.30
%define ecm_ver 5.240.0
%define qt_ver 6.5.0

Requires: sfdisk polkit ntfs-3g exfatprogs btrfs-progs

BuildRequires(pre): rpm-build-kf6
BuildRequires: gcc-c++ extra-cmake-modules >= %ecm_ver
BuildRequires: %_bindir/appstreamcli
#BuildRequires: libdbus-devel libatasmart-devel libblkid-devel >= %blkid_ver libparted-devel
#BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel libqca-qt6-devel
#BuildRequires: libpolkitqt6-qt6-devel
BuildRequires: pkgconfig(blkid) >= %blkid_ver
BuildRequires: pkgconfig(libparted)
BuildRequires: pkgconfig(Qt6Core) >= %qt_ver
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(polkit-qt6-core-1)
#BuildRequires: pkgconfig(KF6I18n)
BuildRequires: kf6-ki18n-devel
#BuildRequires: pkgconfig(KF6CoreAddons)
BuildRequires: kf6-kcoreaddons-devel
#BuildRequires: pkgconfig(KF6WidgetsAddons)
BuildRequires: kf6-kwidgetsaddons-devel

%description
%_name is a Library for managing partitions. Common code for KDE
Partition Manager and other projects.

%package devel
Summary: Development files for icclib
Group: Development/C
Requires: %name = %EVR
Provides: %_name-devel = %EVR

%description devel
%_name is a Library for managing partitions. Common code for KDE
Partition Manager and other projects.

This package provides headers and libraries for development applications
using %_name.

%prep
%setup -n %_name-%version

%build
%K6build

%install
%K6install
%find_lang --all-name %_name

%files -f %_name.lang
%_libexecdir/%{_name}_externalcommand
%_datadir/dbus-1/system-services/%xdg_name.helperinterface.service
%_datadir/dbus-1/system.d/%xdg_name.helperinterface.conf
%_K6lib/*.so.*
%_K6plug/%_name/*.so
%_datadir/polkit-1/actions/%xdg_name.externalcommand.policy

%files devel
%_K6inc/%_name/
%_K6lib/cmake/KPMcore/
%_K6link/*.so


%changelog
* Thu Jul 04 2024 Yuri N. Sedunov <aris@altlinux.org> 24.05.2-alt1
- 24.05.2

* Sat Jun 15 2024 Yuri N. Sedunov <aris@altlinux.org> 24.05.1-alt1
- 24.05.1

* Wed Jun 12 2024 Yuri N. Sedunov <aris@altlinux.org> 24.05.0-alt1
- 24.05.0 (ported to KF6)

* Thu Feb 15 2024 Yuri N. Sedunov <aris@altlinux.org> 23.08.5-alt1
- 23.08.5

* Fri Dec 08 2023 Yuri N. Sedunov <aris@altlinux.org> 23.08.4-alt1
- 23.08.4

* Thu Nov 09 2023 Yuri N. Sedunov <aris@altlinux.org> 23.08.3-alt1
- 23.08.3

* Thu Oct 12 2023 Yuri N. Sedunov <aris@altlinux.org> 23.08.2-alt1
- 23.08.2

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 23.08.1-alt1
- 23.08.1

* Thu Aug 24 2023 Yuri N. Sedunov <aris@altlinux.org> 23.08.0-alt1
- 23.08.0

* Thu Jul 06 2023 Yuri N. Sedunov <aris@altlinux.org> 23.04.3-alt1
- 23.04.3

* Thu Jun 08 2023 Yuri N. Sedunov <aris@altlinux.org> 23.04.2-alt1
- 23.04.2

* Thu May 11 2023 Yuri N. Sedunov <aris@altlinux.org> 23.04.1-alt1
- 23.04.1

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 23.04.0-alt1
- 23.04.0

* Thu Mar 02 2023 Yuri N. Sedunov <aris@altlinux.org> 22.12.3-alt1
- 22.12.3

* Fri Feb 03 2023 Yuri N. Sedunov <aris@altlinux.org> 22.12.2-alt1
- 22.12.2

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

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.80.0-alt1
- 3.80.0

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- first build for Sisyphus

