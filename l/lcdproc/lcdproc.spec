Name: lcdproc
Version: 0.5.6
Release: alt1

Summary: Daemon capable of showing info on LCD displays
License: GPL
Group: System/Kernel and hardware

Url: http://lcdproc.omnipotent.net
Source0: %name-%version.tar.gz
Source1: lcdd.init
Source100: lcdproc.watch
Patch0: lcdproc-fix-return.diff
Patch1: lcdproc-add-serdisplib.diff

BuildRequires: liblirc-devel libncurses-devel

%description
LCDproc is a piece of software that displays real-time system
information from your Linux/*BSD box on a LCD.

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
