Name: debhelper
Version: 7.1.1
Release: alt1

Summary: Tools for Debian Packages

Group: System/Configuration/Packaging
License: GPL
Url: http://packages.debian.org/unstable/devel/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.debian.org/debian/pool/main/d/%name/%{name}_%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Wed Jan 07 2009
BuildRequires: dpkg perl-Test-Pod po4a

%description
The packages contains helper utilities for Debian alien.

%prep
%setup -q -n %name

%build
make -f debian/rules build

%install
rm -f *{es,fr}.1
rm -f dh_testversion*
%makeinstall_std

#install -d -m 755 %buildroot

# autoscripts
#install -d -m 755 %buildroot%_datadir/debhelper/autoscripts
#install -m 644 autoscripts/* %buildroot%_datadir/debhelper/autoscripts

# perl modules
#install -d -m 755 %buildroot%perl_vendorlib/Debian/Debhelper
#install -m 644 Debian/Debhelper/* %buildroot%perl_vendorlib/Debian/Debhelper

# man pages
install -d -m 755 %buildroot%_man1dir/
install -d -m 755 %buildroot%_man7dir/
install -m 644 *.1 %buildroot%_man1dir/
install -m 644 *.7 %buildroot%_man7dir/

# binaries
install -d -m 755 %buildroot%_bindir
install -m 755 dh_*[^1-9] %buildroot%_bindir

%files
%doc doc debian/{changelog,copyright} examples/
%_bindir/*
%_datadir/%name/
%perl_vendorlib/Debian/
%_man1dir/*
%_man7dir/*

%changelog
* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 7.1.1-alt1
- new version 7.1.1 (with rpmrb script)
- update buildreq

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 7.0.16-alt1
- new version 7.0.16 (with rpmrb script)

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 6.0.2-alt1
- new version 6.0.2 (with rpmrb script)

* Wed Apr 11 2007 Vitaly Lipatov <lav@altlinux.ru> 5.0.44-alt1
- new version 5.0.44 (with rpmrb script)

* Sun Oct 08 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0.40-alt0.1
- new version 5.0.40 (with rpmrb script)

* Tue Sep 19 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0.37.3-alt0.1
- new version (5.0.37.3)
- fix URL
- switch to noarch
- add packager

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0.22-alt0.1
- initial build for ALT Linux Sisyphus

