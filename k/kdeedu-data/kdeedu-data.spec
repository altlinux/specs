%define rname kdeedu-data

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Common KDE EDU data
Url: http://www.kde.org
License: GPL-2.0-only

Requires: kde-common
Provides:  kde5-kdeedu-data = %EVR
Obsoletes: kde5-kdeedu-data < %EVR

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: extra-cmake-modules qt6-declarative-devel kf6-ki18n-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data apps

%files
%doc COPYING*
%_K6data/apps/kvtml/
%_K6icon/*/*/actions/*.*


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

