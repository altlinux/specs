%def_without libnm_glib

Name: NetworkManager-strongswan
Version: 1.5.2
Release: alt1

Summary: NetworkManager strongSwan IPSec VPN plug-in

License: GPLv2+
Group: System/Servers
Url: https://www.strongswan.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://download.strongswan.org/NetworkManager/%name-%version.tar.bz2

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libnm) >= 1.1.0
BuildRequires: pkgconfig(libnma) >= 1.1.0
BuildRequires: intltool
BuildRequires: libtool

%if_with libnm_glib
BuildRequires: pkgconfig(dbus-glib-1) >= 0.30
BuildRequires: pkgconfig(NetworkManager) >= 1.1.0
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-glib-vpn)
BuildRequires: pkgconfig(libnm-gtk)
%endif

Requires: NetworkManager
Requires: strongswan-charon-nm >= 5.8.3

%description
This package contains software for integrating the strongSwan IPSec VPN
with NetworkManager.

%package gnome
Summary: NetworkManager VPN plugin for strongswan - GNOME files
Group: System/Servers

Requires: NetworkManager-strongswan = %EVR

%description gnome
This package contains software for integrating the strongSwan IPSec VPN
with the graphical desktop.

%prep
%setup

%build
%configure \
        --disable-static \
%if_without libnm_glib
        --without-libnm-glib \
%endif
        --with-charon=%_libdir/strongswan/ipsec/charon-nm \
        --enable-more-warnings=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_libexecdir/NetworkManager/VPN/nm-strongswan-service.name
%doc NEWS

%files gnome
%_datadir/gnome-vpn-properties/strongswan
%_libexecdir/NetworkManager/nm-strongswan-auth-dialog
%_libdir/NetworkManager/libnm-vpn-plugin-strongswan.so
%exclude %_libdir/NetworkManager/libnm-vpn-plugin-strongswan.la
#_datadir/appdata/NetworkManager-strongswan.appdata.xml

%if_with libnm_glib
%_libdir/NetworkManager/libnm-*-properties.so
%_sysconfdir/NetworkManager/VPN/nm-strongswan-service.name
%exclude %_libdir/NetworkManager/libnm-strongswan-properties.la
%endif

%changelog
* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Wed Jul 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Sisyphus

* Sun Apr 12 2020 Mikhail Zabaluev <mikhail.zabaluev@gmail.com> - 1.5.0-1
- Updated to 1.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Mikhail Zabaluev <mikhail.zabaluev@gmail.com> - 1.4.5-1
- Update to 1.4.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Mikhail Zabaluev <mikhail.zabaluev@gmail.com> - 1.4.4-1
- new version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.4.3-1
- Update to 1.4.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.4.2-1
- Update to 1.4.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-2
- Bring back the D-Bus policy until new charon-nm is released

* Wed Sep 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-1
- New upstream release that integrates our NetworkManager 1.2 support

* Wed Mar 30 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-3.20160330libnm
- Update the NetworkManager 1.2 support patchset

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3.20151023libnm
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-2.20151023libnm
- Add the NetworkManager 1.2 support patchset

* Mon Oct 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Initial packaging
