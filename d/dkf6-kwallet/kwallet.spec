%define rname kwallet

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init

Group: System/Libraries
Summary: KDE Frameworks 6 safe desktop-wide storage for passwords
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires(post,preun): alternatives >= 0.2

# allow to proper evolution install
# Provides: gnome-keyring = 60
# Provides: kf5-kwallet = %%version-%%release
# Obsoletes: kf5-kwallet < %%version-%%release

Source: %name-%version.tar
Source1: kwalletd6.po
Patch2: alt-def-blowfish.patch
Patch3: alt-create-wallet.patch
Patch4: alt-fdo-secrets-ksecretd.patch
Patch5: alt-l10n.patch

BuildRequires(pre): rpm-build-dkf6
BuildRequires: deepin-extra-cmake-modules glibc-devel dqt6-tools-devel dqt6-declarative-devel
BuildRequires: vulkan-headers libdqt6-test
BuildRequires: libgcrypt-devel libgpgme-dqt6-devel libassuan-devel libsecret-devel
BuildRequires: boost-devel
BuildRequires: dkf6-kauth-devel dkf6-kcodecs-devel dkf6-kconfig-devel dkf6-kconfigwidgets-devel
BuildRequires: dkf6-kcoreaddons-devel dkf6-kdbusaddons-devel dkf6-kguiaddons-devel dkf6-ki18n-devel
BuildRequires: dkf6-kiconthemes-devel dkf6-kitemviews-devel dkf6-knotifications-devel
BuildRequires: dkf6-kservice-devel dkf6-kwidgetsaddons-devel dkf6-kwindowsystem-devel
BuildRequires: dkf6-kdoctools-devel dkf6-kcolorscheme-devel dkf6-kcrash-devel
BuildRequires: qca-dqt6-devel
# For secrets API tests
BuildRequires: qca-dqt6-ossl

# find libraries
%add_findprov_lib_path %_DK6lib

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE work spaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libdkf6wallet
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6wallet
KF6 library

%package -n libdkf6walletbackend
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6walletbackend
KF6 library


%prep
%setup -n %name-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1

msgcat --use-first po/ru/kwalletd6.po %SOURCE1 > po/ru/kwalletd6.po.tmp
cat po/ru/kwalletd6.po.tmp >po/ru/kwalletd6.po
rm -f po/ru/kwalletd6.po.tmp

%build
%DK6cmake -DBUILD_TESTING=ON
%DK6make

%check
%ifarch x86_64
LD_LIBRARY_PATH=BUILD/bin BUILD/bin/fdo_secrets_test
%endif

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

install -d %buildroot/%_sysconfdir/alternatives/packages.d/
> %buildroot/%_sysconfdir/alternatives/packages.d/%name
# install alternative
# if [ "%_DK6dbus_srv" == "%_DK6data/dbus-1/services" ] ; then
#     mkdir -p %buildroot/%_DK6data/dbus-1/services/
#     mv %buildroot/%_DK6dbus_srv/org.freedesktop.secrets.service %buildroot/%_DK6data/dbus-1/services/
# fi
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_DK6data/dbus-1/services/org.freedesktop.secrets.service %_DK6data/dbus-1/services/org.freedesktop.secrets.service %version
__EOF__
mv %buildroot/%_DK6bin/kwallet-query %buildroot/%_DK6bin/kwallet-query-6
cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/kwallet-query %_DK6bin/kwallet-query-6 %version
__EOF__

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories

%files
%config /%_sysconfdir/alternatives/packages.d/%name
%_DK6bin/ksecretd
%exclude %_bindir/kwalletd6
%_DK6bin/kwalletd6
%_DK6bin/kwallet-query*
%_DK6xdgapp/*.desktop
%_DK6notif/*.notifyrc
# %_DK6dbus_srv/org.*kwallet*.service
%_DK6dbus_srv/org.*secret*.service
%_DK6dbus_srv/org.freedesktop.secrets.service
%_DK6data/xdg-desktop-portal/portals/kwallet.portal
%dir %_DK6data/man/
%dir %_DK6data/man/man1/
%_DK6data/man/man1/kwallet-query.1.xz

%files devel
#%_DK6inc/kwallet_version.h
%_DK6inc/KWallet/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6Wallet
%_DK6dbus_iface/*.xml

%files -n libdkf6wallet
%_DK6lib/libKF6Wallet.so.*
%files -n libdkf6walletbackend
%_DK6lib/libKF6WalletBackend.so.*


%changelog
* Thu Oct 01 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Mon Dec 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt2
- fix l10n (thanks mcpain@alt)

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Mon Jun 30 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.1-alt3
- fix launch kwalletmanager

* Mon Jun 30 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.1-alt2
- using ksecretd as org.freedesktop.secrets alternative

* Thu May 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.1-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

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

