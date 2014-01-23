#set_verify_elf_method unresolved=strict

Name: gnustep-Burn
Version: 0.5.0
Release: alt1.cvs20140123
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

%description
Burn.app is a GNUstep based CD burning program for GNU/Linux. It serves
as front-end for Jorg Schilling's cdrtools, cdrdao, and cdparanoia.

You will no longer need to remember ugly command line parameters for
cdrecord or write shell scripts. With Burn.app you compile your CD by
point-and-click operation and save your projects for later reuse.
Burn.app will hide as many settings as possible from you, thus making it
very easy and user-friendly to create your own CDs.

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

%files
%doc BUGS CHANGELOG CREDITS README TODO
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.cvs20140123
- Initial build for Sisyphus

