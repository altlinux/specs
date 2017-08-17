%define rname kirigami

Name: kf5-%rname
Version: 5.37.0
Release: alt2%ubt
%K5init

Group: System/Libraries
Summary: A QtQuick based components set
Url: https://techbase.kde.org/Kirigami
License: %lgpl2only

Requires: %name-common = %version-%release
Requires: qt5-quickcontrols2

Source0: %rname-%version.tar

BuildRequires(pre):	rpm-build-kf5 rpm-build-ubt rpm-build-licenses
BuildRequires: extra-cmake-modules qt5-quickcontrols2-devel
BuildRequires: qt5-svg-devel qt5-tools-devel
BuildRequires: kf5-plasma-framework-devel kf5-kpackage-devel

%description
Kirigami is a set of QtQuick components at the moment targeted for mobile use
(in the future desktop as well) targeting both Plasma Mobile and Android. It's
not a whole set of components, all the "Primitive" ones like buttons and
textboxes are a job for QtQuickControls (soon QtQuickControls2) but it's a set
of high level components to make the creation of applications that look and feel
great on mobile as well as desktop devices and follow the
https://community.kde.org/KDE_Visual_Design_Group/KirigamiHIG . The target of
those components is anybody that wants to do an application using QtQuick as its
main UI, especially if targeting a mobile platform, without adding many
dependencies. They work on a variety of platforms, such as Plasma Mobile,
Desktop Linux, Android and Windows. It will eventually become a Tier-1 KDE
Framework.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %version-%release
%description devel
The %name-devel package contains libraries and header files for developing
applications that use %name

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%files
%_K5qml/org/kde/kirigami.2/

%files devel
%_libdir/cmake/KF5Kirigami2/
%_K5archdata/mkspecs/modules/qt_Kirigami2.pri

%changelog
* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt2%ubt
- cleanup specfile

* Wed Aug 16 2017 Stanislav Levin <slev@altlinux.org> 5.37.0-alt1%ubt
- Updated to newest upstream version

* Thu Aug 03 2017 Levin Stanislav  <slev@altlinux.org> 2.2.0-alt1%ubt
- Initial build

