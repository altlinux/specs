%define rname kquickimageeditor

Name: kde5-%rname
Version: 0.2.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KQuickImageEditor QtQuick components
Url: https://invent.kde.org/libraries/kquickimageeditor
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel

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
Requires: libgcrypt-devel libqca-qt5-devel
%description devel
This package contains the development files for %name.


%prep
%setup -n %rname-%version

%build
%K5build \
    #

%install
%K5install
%find_lang --with-kde --all-name %name

%files -f %name.lang
%_K5qml/org/kde/kquickimageeditor/

%files devel
%_K5lib/cmake/KQuickImageEditor/
%_K5archdata/mkspecs/modules/*KQuickImageEditor*.pri

%changelog
* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- initial build
