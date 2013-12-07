Name: lcdproc
Version: 0.5.6
Release: alt3

Summary: Show info on LCD displays
License: GPL
Group: System/Kernel and hardware

Url: http://lcdproc.omnipotent.net
Source0: %name-%version.tar.gz
Source1: lcdd.init
Source100: lcdproc.watch
Patch0: lcdproc-fix-return.diff
Patch1: lcdproc-add-serdisplib.diff

BuildRequires: libfreetype-devel
BuildRequires: libftdi-devel
BuildRequires: libhid-devel
BuildRequires: liblirc-devel
BuildRequires: libncurses-devel
BuildRequires: libpth-devel
BuildRequires: libusb-devel
BuildRequires: libX11-devel

%description
LCDproc is a client/server suite inclduding drivers for all
kinds of nifty LCD displays. The server supports several
serial devices: Matrix Orbital, Crystal Fontz, Bayrad, LB216,
LCDM001 (kernelconcepts.de), Wirz-SLI and PIC-an-LCD; and some
devices connected to the LPT port: HD44780, STV5730, T6963,
SED1520 and SED1330. Various clients are available that display
things like CPU load, system load, memory usage, uptime, and a lot more.
See also %url.

%prep
%setup
#patch1 -p1
subst "s#\(DriverPath\)=.*#\1=%_libdir/lcdproc/#" LCDd.conf

%build
%autoreconf
%configure \
	--enable-libusb \
	--enable-stat-nfs \
	--enable-lcdproc-menus \
	--enable-stat-smbfs \
	--enable-drivers=all

%make_build

%install
%makeinstall
install -pDm755 %SOURCE1 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc %_mandir/man?/*.*
%_bindir/*
%exclude %_bindir/lcdmetar.pl
%_sbindir/*
%_libdir/lcdproc
%config %_sysconfdir/*.conf
%_initdir/*

%changelog
* Sat Dec 07 2013 Michael Shigorin <mike@altlinux.org> 0.5.6-alt3
- improved summary/description
- picked several more BR: from fedora spec

* Sat Dec 07 2013 Michael Shigorin <mike@altlinux.org> 0.5.6-alt2
- rebuilt to ensure safe upgrade from autoimports

* Fri Dec 06 2013 Michael Shigorin <mike@altlinux.org> 0.5.6-alt1
- added watch file
- new version (watch file uupdate)

* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.5.5-alt1
- 0.5.5
- minor spec cleanup
- dropped patch1 (doesn't apply by now)

* Sat Oct 01 2011 Anton Farygin <rider@altlinux.ru> 0.5.4-alt1
- new version

* Tue Oct 30 2007 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- first build for Sisyphus, based on openSuSE specfile
