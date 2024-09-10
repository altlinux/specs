%define rname kwallet

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 safe desktop-wide storage for passwords
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires(post,preun): alternatives >= 0.2

Provides: kf5-kwallet = %version-%release
Obsoletes: kf5-kwallet < %version-%release

Source: %rname-%version.tar
Source1: kwalletd6.po
Patch2: alt-def-blowfish.patch
Patch3: alt-create-wallet.patch
Patch4: alt-org-freedesktop-secrets-service.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules glibc-devel qt6-base-devel qt6-declarative-devel
BuildRequires: libgcrypt-devel libgpgme-devel libassuan-devel
BuildRequires: boost-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kitemviews-devel kf6-knotifications-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kdoctools-devel kf6-kcolorscheme-devel
BuildRequires: qca-qt6-devel
# For secrets API tests
BuildRequires: qca-qt6-ossl

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE work spaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6wallet
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6wallet
KF6 library

%package -n libkf6walletbackend
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6walletbackend
KF6 library


%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1

msgcat --use-first po/ru/kwalletd6.po %SOURCE1 > po/ru/kwalletd6.po.tmp
cat po/ru/kwalletd6.po.tmp >po/ru/kwalletd6.po
rm -f po/ru/kwalletd6.po.tmp

%build
%K6cmake -DBUILD_TESTING=ON
%K6make

%check
LD_LIBRARY_PATH=BUILD/bin BUILD/bin/fdo_secrets_test

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

install -d %buildroot/%_sysconfdir/alternatives/packages.d/
> %buildroot/%_sysconfdir/alternatives/packages.d/%name
# install alternative
if [ "%_K6dbus_srv" == "%_datadir/dbus-1/services" ] ; then
    mkdir -p %buildroot/%_datadir/kf6/dbus-1/services/
    mv %buildroot/%_K6dbus_srv/org.freedesktop.secrets.service %buildroot/%_datadir/kf6/dbus-1/services/
    cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_K6dbus_srv/org.freedesktop.secrets.service %_datadir/dbus-1/services/org.kde.kwalletd6.service %version
__EOF__
    mv %buildroot/%_K6bin/kwallet-query %buildroot/%_K6bin/kwallet-query-6
    cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/kwallet-query %_K6bin/kwallet-query-6 %version
__EOF__
fi

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%config /%_sysconfdir/alternatives/packages.d/%name
%_bindir/kwalletd6
%_K6bin/kwalletd6
%_K6bin/kwallet-query*
%_K6xdgapp/*.desktop
%_K6notif/*.notifyrc
#%_K6srv/*.desktop
%_datadir/dbus-1/services/org.kde.kwalletd5.service
%_datadir/dbus-1/services/org.kde.kwalletd6.service
%_datadir/kf6/dbus-1/services/org.freedesktop.secrets.service
%_datadir/xdg-desktop-portal/portals/kwallet.portal

%files devel
#%_K6inc/kwallet_version.h
%_K6inc/KWallet/
%_K6link/lib*.so
%_K6lib/cmake/KF6Wallet
%_K6dbus_iface/*.xml

%files -n libkf6wallet
%_K6lib/libKF6Wallet.so.*
%files -n libkf6walletbackend
%_K6lib/libKF6WalletBackend.so.*


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- using alternatives for kwallet-query

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

