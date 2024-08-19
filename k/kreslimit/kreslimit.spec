%define rname kreslimit
Name: kreslimit
Version: 2.0.0
Release: alt1

%K6init altplace

Group: Graphical desktop/KDE
Summary: Application resource limit configurator
License: GPL-2.0-or-later

Provides: kde5-kreslimit = %EVR
Obsoletes: kde5-kreslimit < %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-ki18n-devel kf6-kcmutils-devel kf6-kio-devel
BuildRequires: kf6-kdeclarative-devel

%description
Resource limit for launched applications

%prep
%setup 

%build
%K6cmake \
    -DLIBEXEC_INSTALL_DIR=%_K6exec \
    -DCMAKE_BUILD_TYPE=Debug \

%K6make

%install
%K6install

%find_lang %rname --with-kde --all-name

%files -f %rname.lang
%_K6plug/plasma/kcms/systemsettings/*.so
%_K6srv/*.desktop


%changelog
* Mon Aug 19 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.0.0-alt1
- port to KF6

* Mon Aug 12 2024 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt2
- fix requires

* Thu Feb 18 2021 Ivan Razzhivin <underwit@altlinux.org> 1.2.2-alt1
- remove mention from help center
- remove help button

* Wed Sep 09 2020 Ivan Razzhivin <underwit@altlinux.org> 1.2.1-alt1
- the application fills the parent window
- remove multiple items
- set default memory size after adding application

* Fri Aug 07 2020 Ivan Razzhivin <underwit@altlinux.org> 1.2.0-alt1
- select application from list
- add tooltip

* Thu Jun 25 2020 Ivan Razzhivin <underwit@altlinux.org> 1.1.0-alt1
- update translation
- remove unit size column
- remove pidtransit.sh script

* Fri Jun 05 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.3-alt1
- add ability to edit records

* Mon Jun 01 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.2-alt1
- add column for units
- change default values

* Thu Apr 16 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.1-alt1
- change package name
- change units
- set minimum limit size

* Fri Feb 28 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.0-alt1
- init
