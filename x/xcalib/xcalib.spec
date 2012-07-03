%define _iccdir %_datadir/color/icc

Name: xcalib
Version: 0.8
Release: alt3

Packager: Victor Forsyuk <force@altlinux.org>

Summary: ICC Profile loader
License: GPLv2+
Group: System/Libraries

Url: http://xcalib.sourceforge.net/
Source: http://downloads.sourceforge.net/xcalib/xcalib-source-%version.tar.gz
Patch1: xcalib-buildfix.diff

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: libX11-devel libXext-devel libXxf86vm-devel

%description
xcalib is a tiny monitor calibration loader for XFree86 (or X.org) It is able to
apply the vcgt-tag of the ICC device profile to the  video-LUT (a matrix which
assigns one color value to another). You can make ICC profiles for your screens,
cameras and scanners with LProf or load profiles made by various commercial
profilers.

%prep
%setup
%patch1 -p1

%build
%make_build all

%install
install -d %buildroot{%_bindir,%_iccdir}
install -m755 xcalib %buildroot%_bindir/
install -m644 *.icc %buildroot%_iccdir/

%files
%_bindir/*
%_iccdir/*.icc
%doc README README.profilers

%changelog
* Tue Dec 02 2008 Victor Forsyuk <force@altlinux.org> 0.8-alt3
- Renew build requirements to fix FTBFS.

* Mon Oct 13 2008 Victor Forsyuk <force@altlinux.org> 0.8-alt2
- Adopted from an orphanage.

* Sat Mar 08 2008 Vyacheslav Dikonov <slava@altlinux.ru> 0.8-alt1
- ALTLinux build
