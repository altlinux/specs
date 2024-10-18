%define rname kquickimageeditor

Name: kde6-%rname
Version: 0.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KQuickImageEditor QtQuick components
Url: https://invent.kde.org/libraries/kquickimageeditor
License: GPL-2.0-or-later

Requires: kf6-kirigami

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing capabilities.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
This package contains the development files for %name.


%prep
%setup -n %rname-%version

%build
%K6build \
    #

%install
%K6install
%find_lang --with-kde --all-name %name

%files -f %name.lang
%_K6qml/org/kde/kquickimageeditor/

%files devel
%_K6lib/cmake/KQuickImageEditor/
%_K6archdata/mkspecs/modules/*KQuickImageEditor*.pri


%changelog
* Fri Oct 18 2024 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- initial build
