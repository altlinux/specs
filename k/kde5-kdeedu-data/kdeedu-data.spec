%define rname kdeedu-data

Name: kde5-%rname
Version: 15.12.2
Release: alt2
%K5init

Group: Graphical desktop/KDE
Summary: Common KDE EDU data
Url: http://www.kde.org
License: GPLv2+

Requires: kf5-filesystem

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Fri Mar 18 2016 (-bi)
# optimized out: cmake cmake-modules gcc-c++ gtk-update-icon-cache libqt5-core libstdc++-devel python-base python3 python3-base rpm-build-python3
BuildRequires: extra-cmake-modules qt5-base-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data apps

%files
%doc COPYING*
%_K5data/apps/kvtml/
%_K5icon/*/*/actions/*.*

%changelog
* Sat Mar 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- make package noarch

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
