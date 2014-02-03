%set_verify_elf_method unresolved=strict

Name: gnustep-DictionaryReader
Version: 2006
Release: alt3
Summary: DictionaryReader is a dictionary application
License: GPLv2
Group: Graphical desktop/GNUstep
Url: https://www.unix-ag.uni-kl.de/~guenther/gnustep/dictionaryreader.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
DictionaryReader is a dictionary application that queries Dict servers
in the internet to let you look up words. It's aimed to be lightweight
and easy to use.

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

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog NEWS TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2006-alt1
- Initial build for Sisyphus

