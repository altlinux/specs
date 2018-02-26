%define origname trafshow

Name: %origname-linux
Version: 1.3
Release: alt6

Summary: An ncurses-based IP traffic monitoring tool
License: GPL
Group: Monitoring

Source0: ftp://sunsite.unc.edu/pub/linux/system/network/management/%origname-%version.tar.gz
Source1: %name.init
Source2: %name.control
Patch0: trafshow-1.3-glibc.patch
Patch1: trafshow-1.3-config.patch
Patch2: trafshow-1.3-make.patch
Patch3: trafshow-1.3-uptime-fix
Patch4: trafshow-1.3-buffer-overhead.asp.patch
ExclusiveArch: %ix86

PreReq: control

# Automatically added by buildreq on Sat Jan 25 2003
BuildRequires: libncurses-devel libtinfo-devel

Summary(ru_RU.KOI8-R): Консольная утилита мониторинга IP-трафика
Summary(uk_UA.KOI8-U): Консольна утил╕та мон╕торингу IP-траф╕ку

%description
Trafshow will continuously display an ncurses-based graphic
representation of packet traffic on network interfaces.  Trafshow will
also periodically sort and update the traffic information, and may be
useful for monitoring suspicious traffic on your network.

This is Linux (1.3.x) version which is less featureful compared
to BSD version (3.x) but it can monitor PPP links and is still useful.

%description -l ru_RU.KOI8-R
Trafshow обеспечивает отображение пакетного трафика на сетевых интерфейсах,
периодически обновляя и сортируя информацию.

Это Linux-версия (1.3.x), которая менее могуча по сравнению с BSD-версией
(3.x), но способна работать с PPP-интерфейсами и многим нравится больше.

%description -l uk_UA.KOI8-U
Trafshow забезпечу╓ в╕дображення пакетного траф╕ку на мережевих ╕нтерфейсах,
периодично оновлюючи та сотруючи ╕нформац╕ю.

Це Linux-верс╕я (1.3.x), що менш потужна за BSD-верс╕ю (3.x), але здатна
працювати ╕з PPP-╕нтерфейсами та багатьом б╕льш сподоба╓ться.

%prep
%setup -q -n %origname-%version
%patch0 -p1 -b .glibc
%patch1 -p1 -b .config
%patch2 -p1 -b .make
%patch4 -p1 -b .bof

%build
%make_build

%install
install -pD -m755 %origname %buildroot%_bindir/%name
install -pD -m644 %origname.1 %buildroot%_man1dir/%name.1
#install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m755 %SOURCE2 %buildroot%_sysconfdir/control.d/facilities/%name

%pre
/usr/sbin/groupadd -r -f netadmin >/dev/null 2>&1
[ $1 -eq 1 ] || /usr/sbin/control-dump %name

%post
if [ $1 -ge 2 ]; then
	/usr/sbin/control-restore %name
else
	/usr/sbin/control %name public
fi

%files
%_bindir/*
%_man1dir/*
#_initdir/*
%config %_sysconfdir/control.d/facilities/%name
%doc TODO trafshow.lsm

# TODO: make configurable and not hardwire VT & params in initscript?

%changelog
* Sun Apr 13 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt6
- don't install initscript
- drop open(1) dependency, thanks legion@ for reminder

* Wed Nov 29 2006 Michael Shigorin <mike@altlinux.org> 1.3-alt5
- added ASP patch to fix off-by-one bug resulting in possible
  buffer overflow; thanks Andy Shevchenko <andriy asplinux com ua>
  for notifying me and sending a patch (I guess for making it too)

* Mon Nov 17 2003 Michael Shigorin <mike@altlinux.ru> 1.3-alt4
- removed initscript from package (was non-essential, will
  be ported later)

* Fri Mar 07 2003 Michael Shigorin <mike@altlinux.ru> 1.3-alt3
- fixed Requires (added open)

* Mon Jan 27 2003 Michael Shigorin <mike@altlinux.ru> 1.3-alt2
- spec cleanup
- control support
- init script added (taken from Black Cat Linux package and severely modified)
- Patch3 added (from BCL too)

* Tue Nov 19 2002 Michael Shigorin <mike@altlinux.ru> 1.3-alt1
- built for ALT Linux
- spec adapted from RH PT one
- these people were improving it since 1997 at Red Hat Software:
  Tim Powers <timp@redhat.com>
  Michael Maher <mike@redhat.com>
  Otto Hammersmith <otto@redhat.com>

