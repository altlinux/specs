Name: lcdproc
Summary: Daemon capable of showing info on LCD displays
Group: System/Kernel and hardware
Version: 0.5.4
Release: alt1
License: GPL

Url: http://lcdproc.omnipotent.net
Source: %name-%version.tar
Source1: lcdd.init
Patch: lcdproc-fix-return.diff
Patch1: lcdproc-add-serdisplib.diff
BuildRequires: liblirc-devel libncurses-devel

%description
LCDproc is a piece of software that displays real-time system
information from your Linux/*BSD box on a LCD.

%prep
%setup -q
%patch1 -p1
subst "s#\(DriverPath\)=.*#\1=%_libdir/lcdproc/#" LCDd.conf

%build
autoreconf
%configure --enable-libusb --enable-stat-nfs --enable-lcdproc-menus --enable-stat-smbfs --enable-drivers=all
%make_build

%install
%makeinstall
# init script
mkdir -p %buildroot%_initdir
install -c -m 0755 %SOURCE1 %buildroot%_initdir/%name

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
* Sat Oct 01 2011 Anton Farygin <rider@altlinux.ru> 0.5.4-alt1
- new version

* Tue Oct 30 2007 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- first build for Sisyphus, based on openSuSE specfile
