Name: lp_server
Version: 1.1.6
Release: alt1

Summary: Exports a printer port to network

License: GPL
Group: Development/Other
Url: http://www.freesource.info/wiki/Stat'i/SetevajaPechat'

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://lprng.sourceforge.net/DISTRIB/UNIXTOOLS/lp_server/%name-%version.tar.bz2
Source1: %name.init
Source2: %name.sysconfig
Patch: %name-%version.patch

# Automatically added by buildreq on Tue Jan 31 2006
BuildRequires: libelf-devel libncurses-devel libnet2-devel libtinfo-devel

%description
This program allows you to 'export' a printer on your local host
to be used by an LPRng spooler.  It is basically simulating an
HP JetDirect interface,  which opens a connection on port 9100
and simply dumps input to the PostScript Engine.

%prep
%setup -q
%patch -p0 -b .orig

%build
%configure
%make

%install
install -D man/%name.8 %buildroot%_man8dir/%name.8
install -D src/%name %buildroot%_sbindir/%name
install -D %SOURCE1 %buildroot/%_initdir/%name
install -D %SOURCE2 %buildroot/%_sysconfdir/sysconfig/%name
# install -d %buildroot%_spooldir/lpd

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE CHANGES README
%_sbindir/*
%_man8dir/*
%_initdir/%name
#%attr(775,lp,lp) %dir %_spooldir/lpd
%_sysconfdir/sysconfig/%name

%changelog
* Fri Feb 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- add init file for sysvinit, add sysconfig file (thanks to pv@)
- add patch for background mode
- add Url

* Tue Jan 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt0.1
- initial build for ALT Linux Sisyphus
