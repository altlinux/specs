#define git_date .git20111208
%define git_date %nil

%define dbus_version 1.1
%define libdbus_glib_version 0.76
%define libgudev_version 143

Name: ModemManager
Version: 0.5.2
Release: alt2%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: Mobile broadband modem management service
Url: http://gitorious.org/projects/modemmanager
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

Requires: dbus >= %dbus_version

BuildRequires(pre): rpm-build-licenses

BuildRequires: libdbus-glib-devel
BuildRequires: libgudev-devel >= %libgudev_version
BuildRequires: intltool
BuildRequires: ppp-devel
BuildRequires: libpolkit-devel
BuildRequires: gtk-doc

%description
ModemManager provides a DBus interface to communicate with
mobile broadband (GSM, CDMA, UMTS, ...) cards. Implements
a loadable plugin interface to add work-arounds for
non standard devices.

%prep
%setup -n %name-%version
%patch0 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--with-udev-base-dir=/lib/udev \
	--with-polkit \
	--with-docs

%make_build

%check
make check

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc ChangeLog NEWS AUTHORS README
%_datadir/dbus-1/system-services/*.service
%dir %_libdir/ModemManager/
%_libdir/ModemManager/*.so
%_sbindir/*
%_sysconfdir/dbus-1/system.d/*.conf
%_datadir/dbus-1/interfaces/*.xml
/lib/udev/rules.d/*
%_iconsdir/hicolor/*/apps/*
%_datadir/polkit-1/actions/*.policy

%exclude %_libdir/ModemManager/*.la
%exclude %_libdir/pppd/*/mm-test-pppd-plugin.la
%exclude %_libdir/pppd/*/mm-test-pppd-plugin.so

# Not needed to be packaged now.
# Maybe to package it later as the devel subpackage.
%exclude %_includedir/mm/mm-modem.h

%changelog
* Tue Apr 03 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt2
- Patches from upstream git:
  + option: hso_get_cid() always returns >= 0.
  + serial: fix crash when sending some commands to a closed port.
  + gsm: define the PPP auth preferences for STATIC and DHCP device use.

* Mon Mar 19 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Thu Mar 01 2012 Mikhail Efremov <sem@altlinux.org> 0.5.1.97-alt1
- Updated to 0.5.1.97 (0.5.2 RC).

* Thu Dec 08 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20111208
- upstream git snapshot (MM_05 branch).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20110821
- upstream git snapshot (0.5 release and some bugfixes).

* Mon Aug 01 2011 Mikhail Efremov <sem@altlinux.org> 0.4.998-alt1.git20110728
- upstream git snapshot (MM_05 branch) (closes: #25834).

* Fri Jun 24 2011 Mikhail Efremov <sem@altlinux.org> 0.4.997-alt1.git20110624
- upstream git snapshot (MM_05 branch) (closes: #25766).

* Sun May 01 2011 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20110501
- upstream git snapshot

* Tue Nov 30 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20101130
- upstream git snapshot

* Wed Sep 22 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100922
- upstream git snapshot (#23978 may be closed).

* Mon Sep 06 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100906
- upstream git snapshot

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100722
- upstream git snapshot

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100628
- upstream git snapshot

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.3.997-alt1
- 0.3.997 (0.4-beta1)

* Tue Apr 27 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100227
- upstream git snapshot

* Fri Feb 05 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100204
- upstream git snapshot

* Mon Jan 18 2010 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt3.git20100105
- get version of pppd during build.

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt2.git20100105
- BuildRequire ppp-devel.
- upstream git snapshot

* Fri Dec 25 2009 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt2.git20091225
- upstream git snapshot

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt1
- 0.2.997

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20091124
- upstream git snapshot

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20091026
- upstream git snapshot

* Mon Feb 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- initial build for Sisyphus

