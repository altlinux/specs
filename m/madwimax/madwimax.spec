Name: madwimax
Version: 0.1.1
Release: alt2.1
License: GPL2

Url: http://madwimax.googlecode.com

Group: Networking/Other
Summary: MadWimax is a driver for the wimax device Samsung SWC U200

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

# git://github.com/ago/madwimax.git
Source: %name.tar
Source1: wimax0.tar
Source2: %name.sysconfig
Source3: %name.udev-handler
Patch1: %name-alt-deps.patch
Patch2: %name-alt-netscripts.patch

# Automatically added by buildreq on Thu Oct 07 2010
BuildRequires: asciidoc docbook2X libusb-devel python-modules-encodings time xsltproc

Requires: tunctl

%description
This is MadWimax, a reverse-engineered Linux driver for mobile WiMAX
(802.16e) devices based on Samsung CMC-730 chip.

Authors:

gordick:Alexander Gordeev <lasaine@lvk.cs.msu.su>
isenbaev:Vladislav Isenbaev <isenbaev@gmail.com>

%description -l ru_RU.utf8
MadWimax - реверс-инжинированный Linux драйвер для устройств доступа к сетям
mobile WiMAX (802.16e), выполненных на основе чипа Samsung CMC-730.
На данный момент поддерживаются следующие устройства:

* Samsung SWC-U200
* Samsung SWC-E100
* Samsung SWM-S10R (входит в состав нетбука Samsung NC-10)

Авторы:

gordick:Alexander Gordeev <lasaine@lvk.cs.msu.su>
isenbaev:Vladislav Isenbaev <isenbaev@gmail.com>

%prep
%setup -n %name
%patch1 -p1
%patch2 -p1

%build
cp INSTALL INSTALL.TXT
%autoreconf

%configure
%make_build

%install
%makeinstall_std
rename z60 60 %buildroot%_sysconfdir/udev/rules.d/z60*.rules

install -d -m 755 %buildroot%_sysconfdir/net/ifaces/
tar xf %SOURCE1 -C %buildroot%_sysconfdir/net/ifaces/

install -d -m 755 %buildroot%_sysconfdir/sysconfig/
install -m 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -d -m 755 %buildroot/lib/udev
install -m 755 %SOURCE3 %buildroot/lib/udev/%name
%__subst "
	s|RUN+=\"%_sbindir/madwimax|RUN+=\"/lib/udev/%name|
	" %buildroot%_sysconfdir/udev/rules.d/*.rules

%files
%doc AUTHORS ChangeLog INSTALL.TXT NEWS README THANKS TODO scripts/events/*.sh*
%_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sysconfdir/udev/rules.d/*.rules
%_sysconfdir/net/ifaces/wimax0
/lib/udev/%name
%_sbindir/madwimax
%_man8dir/*

%changelog
* Sun May 22 2011 Hihin Ruslan <ruslandh@altlinux.ru> 0.1.1-alt2.1
- Build for Sisyphus

* Tue Oct 12 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.1.1-alt2
- add netscripts/etcnet support to event.sh

* Sun Oct 10 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.1.1-alt1
- new version
- upstream GIT repo
- add %_sysconfdir/sysconfig/%name configuration

* Tue Sep 08 2009 Hihin Ruslan <ruslandh@altlinux.ru> 0.1.0-alt2
- correct /etc/net/wimax0

* Thu Apr 23 2009 Hihin Ruslan <ruslandh@altlinux.ru> 0.1.0-alt1
- first build for ALT Linux Sisyphus
