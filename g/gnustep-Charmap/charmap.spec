%set_verify_elf_method unresolved=strict

Name: gnustep-Charmap
Version: 0.3
Release: alt4.rc1.1
Summary: Character map
License: GPLv2
Group: Graphical desktop/GNUstep
Url: https://savannah.nongnu.org/projects/charmap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Charmap is a powerful character map built with the OpenStep standard,
which means that it can run on Mac OSX and GNUstep (http://www.gnustep.org),
both OpenStep implementations. Feature-wise it is modelled after
gucharmap (gucharmap.sourceforge.net). It uses Unicode.org's Unicode
standard data to display a wide range of information on each character,
including CJK proununciation, cross-references, Unicode decomposition,
and UTF-8 and decimal representations.

%package docs
Summary: Documentation for Charmap
Group: Documentation
BuildArch: noarch

%description docs
Charmap is a powerful character map built with the OpenStep standard,
which means that it can run on Mac OSX and GNUstep (http://www.gnustep.org),
both OpenStep implementations. Feature-wise it is modelled after
gucharmap (gucharmap.sourceforge.net). It uses Unicode.org's Unicode
standard data to display a wide range of information on each character,
including CJK proununciation, cross-references, Unicode decomposition,
and UTF-8 and decimal representations.

This package contains documentation for Charmap.

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files docs
%doc Documentation/*.pdf

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt4.rc1.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt4.rc1
- Built with clang

* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3.rc1
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.rc1
- Added Requires: gnustep-back

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.rc1
- Initial build for Sisyphus

