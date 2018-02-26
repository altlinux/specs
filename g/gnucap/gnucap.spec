%define ver 2009-08-22
Name: gnucap
Version: 20090822
Release: alt1

Summary: GNU Circuit Analysis Package

License: GPL
Group: Video
#Group: Applications/Engineering
Url: http://www.gnucap.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: ftp://ftp.geda.seul.org/pub/geda/dist/%name-%ver.tar.bz2
Source: http://www.gnucap.org/devel/%name-%ver.tar.bz2

# manually removed: linux-libc-headers
# Automatically added by buildreq on Fri Nov 28 2008
BuildRequires: gcc-c++ libreadline-devel tetex-latex

%description
gnucap is a general purpose circuit simulator.  It performs nonlinear
dc and transient analyses, fourier analysis, and ac analysis
linearized at an operating point.  It is fully interactive and
command driven.  It can also be run in batch mode or as a server.
The output is produced as it simulates.  Spice compatible models
for the MOSFET (level 1-7) and diode are included in this
release.

%prep
%setup -q -n %name-%ver

%build
%configure

%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Thu Aug 27 2009 Vitaly Lipatov <lav@altlinux.ru> 20090822-alt1
- new version 20090822 (with rpmrb script)

* Tue Jul 28 2009 Vitaly Lipatov <lav@altlinux.ru> 20090202-alt1
- new version 20090202 (with rpmrb script)

* Fri Nov 28 2008 Vitaly Lipatov <lav@altlinux.ru> 20080527-alt1
- new version (20080527)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 20070329-alt0.1
- new version (20070329)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 20060830-alt0.1
- new version (20060830)
- rewrite spec, update buildreq

* Wed Sep 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20050610-alt0.1
- initial build for ALT Linux Sisyphus

