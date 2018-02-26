Name: ivman
Version: 0.6.14
Release: alt1

Summary: Ivman is an extremely flexible desktop independent frontend to HAL
License: QPL (TrollTech Q Public License)
Group: System/Servers

Url: http://ivman.sourceforge.net
Source0: http://prdownloads.sourceforge.net/ivman/%name-%version.tar.bz2
Source1: %name.initscript
#Source2: IvmConfigConditions.xml.5
#Source2: %name.README.ALT
Source3: %name.configs.tar.bz2
Source4: 92-fstab-nosync.fdi
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Requires:  libhal >= 0.5.3, libdbus >= 0.34, pmount
BuildPreReq: glib2-devel, libxml2-devel, libhal-devel, libdbus-devel, libdbus-glib-devel, pkgconfig, zlib-devel, pmount
Obsoletes: libivman, libivman-devel, libivman-devele-static

%description
Ivman is an extremely flexible desktop independent frontend to HAL, the userspace Hardware Abstraction Layer for Linux. It can be used to execute arbitrary commands when devices are added to or removed from your system, when device properties change, or when devices emit conditions. Any properties of the new or changed device can be included within the executed command.

%prep
%setup -q

%build
%__libtoolize --copy --force
%__aclocal
%__autoconf
%__automake
%configure
%make

%install
%make DESTDIR=%buildroot install
%__install -Dm 755 %SOURCE1 %buildroot%_initrddir/%name

%find_lang %name

cd %buildroot%_sysconfdir/%name
%__tar -jxf %SOURCE3
%__mkdir -p %buildroot%_sysconfdir/hal/fdi/policy
%__install -m 644 %SOURCE4 %buildroot%_sysconfdir/hal/fdi/policy/92-fstab-nosync.fdi

%pre
/usr/sbin/groupadd ivman || :

/usr/sbin/useradd -c "Ivman monitor" -d /dev/null \
 -s /dev/null -r -g ivman ivman 2> /dev/null || :

%files -f %name.lang
%config(noreplace) %_sysconfdir/%name/*.xml
%config(noreplace) %_sysconfdir/hal/fdi/policy/92-fstab-nosync.fdi

%_initdir/*
%_bindir/%name
%_bindir/%name-launch
%_mandir/man*/*

%changelog
* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.6.14-alt1
- new version

* Sat Dec 16 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.6.13-alt3
- next attempt fix preinstall script

* Wed Dec 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.6.13-alt2
- fix preinstall scripts

* Mon Dec 04 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.6.13-alt1
- new version

* Thu Dec 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.7-alt1
- new version
* Fri Nov 25 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.6-alt1.1
- rebuild with libgsf-1.so.113 .
* Thu Nov 24 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.6-alt1
- new version
- remove shared library and headers
* Wed Aug 03 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.4-alt5
- fix #7529
- add policy fstab-nosync to prevent hal write to /etc/fstab
* Mon Aug 01 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.4-alt4
- fix requires pmount
* Wed Jul 13 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.4-alt3
- rebuild with new hal and dbus
* Sun Jul 10 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.4-alt2
- Add initscript
- Add preinstall script (add user ivman)
- Add configs
* Fri Jun 17 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.4-alt1
- New version
- Reenable integration with pmount
* Fri Jun 17 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.2-alt0.5
- Separate packaging  development library and static development library
* Mon Jun 13 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.2-alt0.4
- Separate build library and binary package
* Mon Jun 13 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.2-alt0.3
- Cleanup spec file
* Mon Jun 13 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.2-alt0.2
- Remove bad Gentoo stuff
* Thu Jun  9 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.6.2-alt0.1
- build for ALT Linux
