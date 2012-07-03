%def_disable hal 

Name: pmount
Version: 0.9.23
Release: alt2

Summary: Automounter tool for HAL/dbus
License: GPL
Group: Monitoring

Url: http://pmount.alioth.debian.org/

Source0: %name-%version.tar.gz

Source3: %name.control

Patch0: pmount-0.9.16-alt-makefile.patch
Patch2: pmount-0.9.17-alt-floppy.patch
Patch3: pmount-0.9.23-alt-natspec.patch

Requires: mount

Packager: Afanasov Dmitry <ender@altlinux.org>

%{?_enable_hal:BuildRequires: libhal-devel >= 0.5.7}
BuildRequires: libdbus-devel >= 0.94, libsysfs-devel, pkgconfig, intltool, libblkid-devel
PreReq: control

# hack for build in hasher
BuildPreReq: glib2-devel

# Automatically added by buildreq on Wed Aug 29 2007
BuildRequires: gcc-c++ libnatspec-devel libsysfs-devel perl-XML-Parser

%description
pmount allows unprivileged users to mount replaceable media USB, FireWire and
PCMCIA without record in /etc/fstab. It creates powerful system of automounting
as project GNOME Utopia, and limits volume of a code which should be carried
out with the rights root up to a minimum. Version 0.9 includes also integration
with cryptsetup for transparent connection crypto devices.

%description -l ru_RU.UTF8
pmount позволяет непривигелированным пользователям подключать(монтировать)
сменные носители USB, FireWire и PCMCIA без записи в /etc/fstab. Это создает
мощную систему автомонтирования, как проект GNOME Utopia, и ограничивает объем
кода, который должен выполняться с правами  root до минимума. Версия 0.9
включает также интеграцию с cryptsetup для прозрачного подключения криптованых
устройств.

%package hal
Summary: HAL-aware wrapper around pmount
Group: Monitoring

Requires: pmount

%description hal
pmount-hal extends pmount by making it work together with hal (Hardware
Abstration Layer).

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure \
	--with-media-dir=/media/ \
	--with-lock-dir=/var/lock/pmount/ \
	--with-whitelist=/etc/pmount.allow \
	--with-mount-prog=/bin/mount \
	--with-umount-prog=/bin/umount \
	--with-cryptsetup-prog=/usr/sbin/cryptsetup \
	%{subst_enable hal} \
	--with-natspec
%make_build

%install
%make_install DESTDIR=%buildroot install
%__install -pD -m755 %SOURCE3 %buildroot%_controldir/%name

%find_lang %name

%pre
%pre_control pmount

%post
%post_control -s restricted pmount

%files -f %name.lang
%doc AUTHORS ChangeLog README.devel TODO
%config(noreplace) %_sysconfdir/pmount.allow
%_controldir/%name
%attr(700,root,root) %_bindir/p*mount
%_man1dir/pmount.1*
%_man1dir/pumount.1*

%if_enabled hal
%files hal
%_bindir/pmount-hal
%_man1dir/pmount-hal.1*
%endif


%changelog
* Tue Feb 15 2011 Afanasov Dmitry <ender@altlinux.org> 0.9.23-alt2
- build without pmount-hal

* Thu Jan 27 2011 Afanasov Dmitry <ender@altlinux.org> 0.9.23-alt1
- 0.9.20 -> 0.9.23

* Thu Sep 17 2009 Afanasov Dmitry <ender@altlinux.org> 0.9.20-alt1
- 0.9.19 -> 0.9.20
- remove applied alt-umount patch
- update alt-ext4 patch

* Tue Aug 04 2009 Afanasov Dmitry <ender@altlinux.org> 0.9.19-alt3
- use xgrp as default control's value (Closes: #20931)
- install p*mount executables with 700 filemode.

* Tue Aug 04 2009 Afanasov Dmitry <ender@altlinux.org> 0.9.19-alt2
- apply alt-ext4 patch (Closes: #20930)

* Wed Mar 04 2009 Afanasov Dmitry <ender@altlinux.org> 0.9.19-alt1
- 0.9.18 -> 0.9.19

* Mon Oct 27 2008 Afanasov Dmitry <ender@altlinux.org> 0.9.18-alt1.1
- 0.9.17 -> 0.9.18

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 0.9.17-alt2
- don't use obsolete macros

* Tue Jan 08 2008 Igor Zubkov <icesik@altlinux.org> 0.9.17-alt1
- 0.9.16 -> 0.9.17

* Wed Aug 29 2007 Igor Zubkov <icesik@altlinux.org> 0.9.16-alt2
- pmount now respect locale settings via libnatspec (closes #10180)

* Wed Aug 08 2007 Igor Zubkov <icesik@altlinux.org> 0.9.16-alt1
- 0.9.13 -> 0.9.16
- update Url
- update patches
- buildreq

* Mon Dec 04 2006 Igor Zubkov <icesik@altlinux.org> 0.9.13-alt4
- rebuild with new dbus
- fix work with new dbus (patch3)
- bump buildprereq libdbus to >= 0.94

* Sun Dec 03 2006 Igor Zubkov <icesik@altlinux.org> 0.9.13-alt3
- s/wheelonly/xgrp/ (#9475)
- add help messages to control file

* Tue Oct 24 2006 Igor Zubkov <icesik@altlinux.org> 0.9.13-alt2
- change mount order for floppy (#9532)

* Wed Oct 18 2006 Igor Zubkov <icesik@altlinux.org> 0.9.13-alt1
- 0.9.11 -> 0.9.13 (#10056)
- fix problem with charsets (#9554 and #10137)
- fix working with cryptsetup
- closes #8081, typo in pmount manual page
- add requires to mount
- add docs
- mark config /etc/pmount.allow as noreplace
- buildreq
- small spec clean up

* Wed May 24 2006 Anton Farygin <rider@altlinux.ru> 0.9.11-alt1
- new version

* Fri Apr 21 2006 Anton Farygin <rider@altlinux.ru> 0.9.9-alt2
- buildrequires fixed

* Fri Apr 14 2006 Anton Farygin <rider@altlinux.ru> 0.9.9-alt1
- new version

* Tue Dec 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.3-alt1.1
- Rebuild with libsysfs.so.2.0.0 .

* Wed Jul 13 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.9.3-alt1
- new version
* Fri Jun 17 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.8-alt1
- first build for ALT Linux
- add patch for Makefile
- add control facility
