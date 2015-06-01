%define rname kaccounts-integration
%define sover 1
%define libkaccounts libkaccounts%sover

Name: kde5-%rname
Version: 15.4.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Framework for storing secrets and accounts
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri May 29 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libaccounts-glib libaccounts-qt51 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsignon-qt51 libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: accounts-qt5-devel extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libdb4-devel python-module-google rpm-build-python3 rpm-build-ruby signon-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: accounts-qt5-devel signon-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Accounts-SSO is the framework we are using to store secrets (tokens, passwords)
and for storing Accounts (small pieces of information containing a name,
a provider, etc).

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

%package -n %libkaccounts
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
Requires: signon
%description -n %libkaccounts
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K5inc/KAccounts/
%_K5link/lib*.so
%_K5lib/cmake/KAccounts

%files -n %libkaccounts
%_K5lib/libkaccounts.so.%sover
%_K5lib/libkaccounts.so.*
%_K5plug/*accounts.so
%_K5srv/*_kaccounts.desktop
%_K5srv/kded/accounts.desktop

%changelog
* Mon Jun 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.1-alt1
- initial build
