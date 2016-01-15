%set_verify_elf_method unresolved=strict

Name: gnustep-easydiff
Version: 0.4.1
Release: alt6.git20121210.1
Summary: GNUstep's implementation of the OPENSTEP FileMerge application
License: GPLv2+ and GPLv3
Group: File tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-easydiff.git
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
EasyDiff is GNUstep's implementation of the OPENSTEP FileMerge
application. EasyDiff allows for easy merging of differences between
files and is a convenient way to explore changes. It also knows about
different SCMSs and is useful in resolving merge conflicts.

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

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt6.git20121210.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt6.git20121210
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt5.git20121210
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt4.git20121210
- Rebuilt with new gnustep-gui

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt3.git20121210
- Added menu file (thnx kostyalamer@)

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.git20121210
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20121210
- Initial build for Sisyphus

