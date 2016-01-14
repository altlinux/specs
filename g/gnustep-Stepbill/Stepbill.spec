%set_verify_elf_method unresolved=strict

Name: gnustep-Stepbill
Version: 2.4
Release: alt4.1
Summary: Get rid of those nasty Wingdows viruses
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/wheezy/stepbill.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
This is a port of the MacBill, which is based on xbill, source to
GNUstep.

Ever get the feeling that nothing is going right? You're a sysadmin, and
someone's trying to destroy your computers. The little people running
around the screen are trying to infect your computers with Wingdows
[TM], a virus cleverly designed to resemble a popular operating system.
Your objective is to click the mouse on them, ending their potential
threat. If one of the people reaches a computer, it will attempt to
replace your operating system with the virus it carries. It will then
attempt to run off the screen with your vital software.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog StepBill-README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 2.4-alt4.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1
- Initial build for Sisyphus

