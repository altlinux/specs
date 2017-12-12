%define rname purpose

Name: kf5-%rname
Version: 1.2.1
Release: alt1%ubt
%K5init altplace

Group: Graphical desktop/KDE
Summary: Abstraction to provide and leverage actions of a specific kind
Url: http://www.kde.org
License: LGPLv2.1+

Requires: kde5-connect

Source: %rname-%version.tar
Patch1: alt-libs-static.patch

# Automatically added by buildreq on Tue Feb 16 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ gtk-update-icon-cache libEGL-devel libGL-devel libaccounts-glib libaccounts-qt51 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsignon-qt51 libstdc++-devel libxcbutil-keysyms perl-Encode perl-XML-Parser pkg-config python-base python-module-google python-modules python3 python3-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: accounts-qt5-devel extra-cmake-modules intltool kde5-kaccounts-integration-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel qt5-declarative-devel rpm-build-python3 rpm-build-ruby signon-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel
#BuildRequires: kde5-connect
BuildRequires: accounts-qt5-devel intltool kde5-kaccounts-integration-devel signon-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5purposewidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5purposewidgets
KF5 library

%package -n libkf5purpose
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5purpose
KF5 library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data purpose kpackage

%files common

%files
%_K5exec/purpose*
%_K5plug/purpose/
%_K5qml/org/kde/purpose/
%_K5data/purpose/
%_K5data/kpackage/Purpose/
#%_K5icon/*/*/apps/reviewboard.*
%_K5icon/*/*/actions/kipiplugin_youtube.*
%_K5icon/*/*/apps/*purpose*.*
%_datadir/accounts/services/kde/

%files devel
%_K5inc/purpose/
%_K5inc/purposewidgets/
%_K5link/lib*.so
%_K5lib/cmake/KDEExperimentalPurpose/

%files -n libkf5purpose
%_K5lib/libKF5Purpose.so.*
%files -n libkf5purposewidgets
%_K5lib/libKF5PurposeWidgets.so.*

%changelog
* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1%ubt
- new version

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1%ubt
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
