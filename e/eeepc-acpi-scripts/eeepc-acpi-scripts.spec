Name: eeepc-acpi-scripts
Version: 1.1.9
Release: alt5

Summary: Debian eeePC support scripts
License: GPL
Group: System/Kernel and hardware

BuildArch: noarch

Url: http://git.debian.org/?p=debian-eeepc/eeepc-acpi-scripts.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: acpid udev amixer aosd_cat
Requires: rfkill >= 0.3.3

Conflicts: eeepc-scripts


%description
This package adds support to the special features of Asus Eee PC series of
laptops. These include sleep (suspend) and hotkeys such as wireless,
brightness, mute, volume, video output toggle and the 'soft' keys available in
some models.


%prep
%setup
%patch -p1
#sed -i 's,/etc/default,%_datadir,g' etc/acpi/*/*

%install
mkdir -p %buildroot%_sysconfdir/acpi/{actions,events,lib}
install -p -m0755 etc/acpi/actions/* %buildroot%_sysconfdir/acpi/actions/
install -p -m0644 etc/acpi/events/* %buildroot%_sysconfdir/acpi/events/
install -p -m0644 etc/acpi/lib/* %buildroot%_sysconfdir/acpi/lib/

mkdir -p %buildroot%_sysconfdir/modprobe.d
install -p -m0644 etc/modprobe.d/* %buildroot%_sysconfdir/modprobe.d/

mkdir -p %buildroot/lib/udev/rules.d
install -p -m0644 lib/udev/rules.d/* %buildroot/lib/udev/rules.d/
install -p -m0755 lib/udev/[^r]* %buildroot/lib/udev/

mkdir -p %buildroot%_datadir/%name
install -p -m0644 functions.sh %buildroot%_datadir/%name/

install -pD -m0644 debian/eeepc-acpi-scripts.default.in %buildroot%_sysconfdir/default/%name
install -pD -m0755 debian/eeepc-acpi-scripts.init %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig/%name.d
cat > %buildroot%_sysconfdir/sysconfig/%name.d/00README << _E_O_F_
# put here custom configuration snippets
# do not remove or edit THIS file
_E_O_F_

mkdir -p %buildroot%_localstatedir/%name

%post
%post_service %name
%_initdir/acpid condreload

%preun
%preun_service %name
%_initdir/acpid condreload


%files
%_sysconfdir/acpi/*
%_sysconfdir/modprobe.d/*
%_sysconfdir/default/%name
%_sysconfdir/sysconfig/%name.d
%_initdir/%name
/lib/udev/*
%exclude %dir /lib/udev/rules.d/
%_datadir/%name/
%_localstatedir/%name/
%doc TODO debian/NEWS debian/README.Debian debian/changelog debian/copyright


%changelog
* Wed May 12 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.9-alt5
- 00README

* Wed Apr 28 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.9-alt4
- defaults moved to /etc/defaults

* Wed Apr 28 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.9-alt3
- package redesigned

* Wed Apr 28 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.9-alt2
- reasonable defaults; always use first soundcard to deal with alsa-plugin-pulse

* Wed Apr 28 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.9-alt1
- new upstream version

* Tue Jan 12 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.6.0-alt1
- upstream updated

* Tue Jan 12 2010 Mykola Grechukh <gns@altlinux.ru> 1.1.2-alt2
- require amixer

* Tue Aug 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Fri May 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.0-alt4
- 1.1.0-8-g39afa73
- SHE support (from upstream shengine branch)

* Thu May 14 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.0-alt3
- add condstop target to the initscript to make preun_service happy (repocop)

* Mon May 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.0-alt2
- fix /etc/acpi/actions/{lid,sleep}.sh

* Sat May 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.0-alt1
- initial build
- tested on 901 with 2.6.30-rc4 kernel, your mileage may vary
