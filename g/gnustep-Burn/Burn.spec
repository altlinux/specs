#set_verify_elf_method unresolved=strict

Name: gnustep-Burn
Version: 0.5.0
Release: alt3.cvs20140123
Summary: Burn ist a front-end for Jorg Schilling's cdrtools, cdrdao, and cdparanoia
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@gsburn.cvs.sourceforge.net:/cvsroot/gsburn login
# cvs -z3 -d:pserver:anonymous@gsburn.cvs.sourceforge.net:/cvsroot/gsburn co -P Burn.app
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-CDPlayer-devel libao-devel libmad-devel

Requires: gnustep-CDPlayer
Requires: gnustep-back

%description
Burn.app is a GNUstep based CD burning program for GNU/Linux. It serves
as front-end for Jorg Schilling's cdrtools, cdrdao, and cdparanoia.

You will no longer need to remember ugly command line parameters for
cdrecord or write shell scripts. With Burn.app you compile your CD by
point-and-click operation and save your projects for later reuse.
Burn.app will hide as many settings as possible from you, thus making it
very easy and user-friendly to create your own CDs.

%package devel
Summary: Development files of Burn
Group: Development/Objective-C
BuildArch: noarch
Requires: %name = %EVR

%description devel
Burn.app is a GNUstep based CD burning program for GNU/Linux. It serves
as front-end for Jorg Schilling's cdrtools, cdrdao, and cdparanoia.

This package contains development files of Burn.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -d %buildroot%_includedir/Burn
install -m644 *.h Burn/*.h %buildroot%_includedir/Burn/

%files
%doc BUGS CHANGELOG CREDITS README TODO
%_bindir/*
%_libdir/GNUstep

%files devel
%_includedir/*

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt3.cvs20140123
- Added Requires: gnustep-CDPlayer and Requires: gnustep-back

* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.cvs20140123
- Added headers

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.cvs20140123
- Initial build for Sisyphus

