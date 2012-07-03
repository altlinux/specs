Name: monica
Version: 3.7
Release: alt2.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Monitor Calibration Tool
License: BSD
Group: Graphics

URL: http://www.pcbypaul.com/software/monica.html
Source: http://www.pcbypaul.com/software/dl/monica-%version.tar.bz2
Patch1: monica-3.7-stdio.patch

Requires: xgamma

# Automatically added by buildreq on Tue Jun 16 2009
BuildRequires: gcc-c++ libX11-devel libXext-devel libXft-devel libfltk-devel

BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel

%description
Monica is a monitor calibration tool. It works as frontend to xgamma to alter
the gamma correction for XFree86 or Xorg. The black point, gray, and color
blocks help to find usable settings for a target of 2.2 gamma, the Web, and
sRGB standard.

%prep
%setup
%patch1 -p1

%build
make CXX="g++ %optflags %optflags_nocpp"

%install
install -pD -m755 monica %buildroot%_bindir/monica

%files
%_bindir/*
%doc authors licence news readme

%changelog
* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt2.2
- FLTK 1.3.0.r8575

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt2.1
- Rebuilt with libfltk13 and for debuginfo

* Tue Jun 16 2009 Victor Forsyuk <force@altlinux.org> 3.7-alt2
- Add missing include of stdio.h header.

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 3.7-alt1
- 3.7

* Tue May 08 2007 Victor Forsyuk <force@altlinux.org> 3.6-alt1
- 3.6

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 3.5-alt2
- Add run-time requirement for xgamma (fix ALT#11189).

* Wed Dec 13 2006 Victor Forsyuk <force@altlinux.org> 3.5-alt1
- 3.5

* Thu Sep 29 2005 Victor Forsyuk <force@altlinux.ru> 3.4-alt1
- 3.4

* Wed Jul 13 2005 Victor Forsyuk <force@altlinux.ru> 3.3-alt1
- 3.3

* Fri Apr 15 2005 Victor Forsyuk <force@altlinux.ru> 3.2-alt1
- Initial build.
