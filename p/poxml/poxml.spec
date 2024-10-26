%define rname poxml

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Conversions between PO and XML
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-poxml = %EVR
Obsoletes: kde5-poxml < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/*


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

