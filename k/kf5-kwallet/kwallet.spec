%define rname kwallet

Name: kf5-%rname
Version: 5.116.0
Release: alt3
%K5init

Group: System/Libraries
Summary: KDE Frameworks 5 safe desktop-wide storage for passwords
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires(post,preun): alternatives >= 0.2

Source: %rname-%version.tar
Source1: kwalletd5.po
Patch2: alt-def-blowfish.patch
Patch3: alt-create-wallet.patch
Patch4: alt-fix-wallet-format.patch
Patch5: alt-org-freedesktop-secrets-service.patch

# Automatically added by buildreq on Fri Feb 13 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libgpg-error libgpg-error-devel libqt5-core libqt5-dbus libqt5-gui libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ glibc-devel-static kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel libgcrypt-devel libgpgme-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ glibc-devel qt5-base-devel
BuildRequires: libgcrypt-devel libgpgme-devel libassuan-devel
BuildRequires: boost-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kitemviews-devel kf5-knotifications-devel
BuildRequires: kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kdoctools-devel kf5-kdoctools
BuildRequires: libqca-qt5-devel
# For secrets API tests
BuildRequires: qca-qt5-ossl

%description
This framework contains two main components:
* Interface to KWallet, the safe desktop-wide storage for passwords on KDE work spaces.
* The kwalletd used to safely store the passwords on KDE work spaces.

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

%package -n libkf5wallet
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5wallet
KF5 library

%package -n libkwalletbackend5
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkwalletbackend5
KF5 library


%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

msgcat --use-first po/ru/kwalletd5.po %SOURCE1 > po/ru/kwalletd5.po.tmp
cat po/ru/kwalletd5.po.tmp >po/ru/kwalletd5.po
rm -f po/ru/kwalletd5.po.tmp

%build
%K5cmake -DBUILD_TESTING=ON
%K5make

%check
LD_LIBRARY_PATH=BUILD/bin BUILD/bin/fdo_secrets_test

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

install -d %buildroot/%_sysconfdir/alternatives/packages.d/
> %buildroot/%_sysconfdir/alternatives/packages.d/%name
# install alternative
if [ "%_K5dbus_srv" == "%_datadir/dbus-1/services" ] ; then
    mkdir -p %buildroot/%_datadir/kf5/dbus-1/services/
    mv %buildroot/%_K5dbus_srv/org.freedesktop.secrets.service %buildroot/%_datadir/kf5/dbus-1/services/
    cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_K5dbus_srv/org.freedesktop.secrets.service %_datadir/dbus-1/services/org.kde.kwalletd5.service %version
__EOF__
    mv %buildroot/%_K5bin/kwallet-query %buildroot/%_K5bin/kwallet-query-5
    cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/kwallet-query %_K5bin/kwallet-query-5 %version
__EOF__
fi

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories5/*.*categories

%files
%config /%_sysconfdir/alternatives/packages.d/%name
%_bindir/kwalletd5
%_K5bin/kwalletd5
%_K5bin/kwallet-query*
%_K5xdgapp/*.desktop
%_K5notif/*.notifyrc
%_K5srv/*.desktop
%_datadir/dbus-1/services/org.kde.kwalletd5.service
%_datadir/kf5/dbus-1/services/org.freedesktop.secrets.service

%files devel
#%_K5inc/kwallet_version.h
%_K5inc/KWallet/
%_K5link/lib*.so
%_K5lib/cmake/KF5Wallet
%_K5archdata/mkspecs/modules/qt_KWallet.pri
%_K5dbus_iface/*.xml

%files -n libkf5wallet
%_K5lib/libKF5Wallet.so.*
%files -n libkwalletbackend5
%_K5lib/libkwalletbackend5.so.*

%changelog
* Mon Aug 12 2024 Sergey V Turchin <zerg@altlinux.org> 5.116.0-alt3
- fix package

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 5.116.0-alt2
- using alternatives for kwallet-query

* Thu May 23 2024 Sergey V Turchin <zerg@altlinux.org> 5.116.0-alt1
- new version

* Mon Feb 12 2024 Sergey V Turchin <zerg@altlinux.org> 5.115.0-alt1
- new version

* Mon Jan 15 2024 Sergey V Turchin <zerg@altlinux.org> 5.114.0-alt1
- new version

* Fri Dec 15 2023 Sergey V Turchin <zerg@altlinux.org> 5.113.0-alt1
- new version

* Thu Nov 30 2023 Sergey V Turchin <zerg@altlinux.org> 5.112.0-alt2
- fix empty alternatives file

* Wed Nov 15 2023 Sergey V Turchin <zerg@altlinux.org> 5.112.0-alt1
- new version

* Thu Nov 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.111.0-alt2
- don't force alternate placement placement
- add alternative for dbus org.freedesktop.secrets.service

* Thu Oct 19 2023 Sergey V Turchin <zerg@altlinux.org> 5.111.0-alt1
- new version

* Mon Sep 11 2023 Sergey V Turchin <zerg@altlinux.org> 5.110.0-alt1
- new version

* Thu Aug 31 2023 Sergey V Turchin <zerg@altlinux.org> 5.109.0-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.108.0-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 5.107.0-alt1
- new version

* Mon May 15 2023 Sergey V Turchin <zerg@altlinux.org> 5.106.0-alt1
- new version

* Mon Apr 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.105.0-alt1
- new version

* Tue Mar 14 2023 Sergey V Turchin <zerg@altlinux.org> 5.104.0-alt1
- new version

* Mon Feb 13 2023 Sergey V Turchin <zerg@altlinux.org> 5.103.0-alt1
- new version

* Mon Jan 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.102.0-alt1
- new version

* Tue Dec 20 2022 Slava Aseev <ptrnine@altlinux.org> 5.101.0-alt2
- add org.freedesktop.secrets.service file

* Fri Dec 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.101.0-alt1
- new version

* Mon Nov 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.100.0-alt1
- new version

* Tue Oct 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.99.0-alt1
- new version

* Mon Sep 12 2022 Sergey V Turchin <zerg@altlinux.org> 5.98.0-alt1
- new version

* Fri Aug 19 2022 Oleg Solovyov <mcpain@altlinux.org> 5.97.0-alt2
- fix incorrect format in wallets (patch by ptrnine@)

* Mon Aug 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.97.0-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.96.0-alt1
- new version

* Tue Jun 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.95.0-alt1
- new version

* Tue May 31 2022 Slava Aseev <ptrnine@altlinux.org> 5.94.0-alt2
- fix blinking fdo_secrets_test

* Mon May 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.94.0-alt1
- new version

* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.93.0-alt1
- new version

* Mon Mar 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.92.0-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.91.0-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.90.0-alt1
- new version

* Thu Dec 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.89.0-alt1
- new version

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.88.0-alt1
- new version

* Mon Oct 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.87.0-alt1
- new version

* Mon Sep 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.86.0-alt1
- new version

* Thu Aug 19 2021 Slava Aseev <ptrnine@altlinux.org> 5.85.0-alt2
- Secret Service API patch:
  + fix mangling of invalid collection object paths
  + allow any characters to be used in wallet names

* Mon Aug 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.85.0-alt1
- new version

* Wed Jul 21 2021 Oleg Solovyov <mcpain@altlinux.org> 5.84.0-alt3
- create wallet when user refuses to set password

* Tue Jul 20 2021 Slava Aseev <ptrnine@altlinux.org> 5.84.0-alt2
- Update Secret Service API patch to the new version

* Tue Jul 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.84.0-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.83.0-alt1
- new version

* Fri Jun 04 2021 Slava Aseev <ptrnine@altlinux.org> 5.82.0-alt3
- Do not keep dbus-daemon waiting if KWallet is disabled (fixes: #40132)

* Thu May 13 2021 Slava Aseev <ptrnine@altlinux.org> 5.82.0-alt2
- Introduce Secret Service API

* Wed May 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.82.0-alt1
- new version

* Mon Apr 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.81.0-alt1
- new version

* Thu Mar 18 2021 Sergey V Turchin <zerg@altlinux.org> 5.80.0-alt1
- new version

* Mon Feb 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.79.0-alt1
- new version

* Sun Jan 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.78.0-alt1
- new version

* Mon Dec 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.77.0-alt1
- new version

* Mon Nov 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.76.0-alt1
- new version

* Tue Oct 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.75.0-alt1
- new version

* Mon Sep 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.74.0-alt1
- new version

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.73.0-alt1
- new version

* Thu Jul 23 2020 Sergey V Turchin <zerg@altlinux.org> 5.72.0-alt1
- new version

* Tue May 12 2020 Sergey V Turchin <zerg@altlinux.org> 5.70.0-alt1
- new version

* Wed Apr 15 2020 Sergey V Turchin <zerg@altlinux.org> 5.69.0-alt1
- new version

* Mon Mar 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.68.0-alt1
- new version

* Mon Feb 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.67.0-alt1
- new version

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.66.0-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.65.0-alt1
- new version

* Mon Nov 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.64.0-alt1
- new version

* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.63.0-alt1
- new version

* Mon Sep 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.62.0-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 5.61.0-alt1
- new version

* Mon Jul 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.60.0-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.59.0-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 5.58.0-alt1
- new version

* Mon Apr 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.57.0-alt1
- new version

* Thu Apr 04 2019 Oleg Solovyov <mcpain@altlinux.org> 5.56.0-alt3
- fix package

* Wed Apr 03 2019 Oleg Solovyov <mcpain@altlinux.org> 5.56.0-alt2
- creating wallet: translate new strings, set icon to warning

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.56.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.55.0-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt2
- new version

* Tue Jan 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt1
- new version

* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1%ubt
- new version

* Wed Sep 05 2018 Sergey V Turchin <zerg@altlinux.org> 5.49.0-alt1%ubt
- new version

* Tue Sep 04 2018 Oleg Solovyov <mcpain@altlinux.org> 5.48.0-alt3%ubt
- kwallet: edit notification text

* Mon Sep 03 2018 Oleg Solovyov <mcpain@altlinux.org> 5.48.0-alt2%ubt
- kwallet: create a wallet when user refuses to do so

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.47.0-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.46.0-alt1%ubt
- new version

* Fri May 04 2018 Sergey V Turchin <zerg@altlinux.org> 5.45.0-alt1%ubt
- new version

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1%ubt
- new version

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1%ubt
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1%ubt
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1%ubt
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1%ubt
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.30.0-alt1%ubt
- new version

* Tue Dec 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.29.0-alt1%ubt
- new version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt0.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt0.M80P.1
- build for M80P

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- new version

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- new version

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt2
- don't use gpg by default

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt3
- build with gpgmepp

* Fri Jul 31 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt2
- move dbus service to standard place

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build
