%set_verify_elf_method unresolved=strict

Name: gnustep-Charmap
Version: 0.3
Release: alt1.rc1
Summary: Character map
License: GPLv2
Group: Graphical desktop/GNUstep
Url: https://savannah.nongnu.org/projects/charmap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%_bindir/*
%_libdir/GNUstep

%files docs
%doc Documentation/*.pdf

%changelog
* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.rc1
- Initial build for Sisyphus

