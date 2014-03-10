%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-StepChat
Version: 0.2
Release: alt2.git20131126
Summary: A instant messenger for jabber
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/StepChat.git
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator libssl-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-XMPPKit-devel
BuildPreReq: gnustep-Etoile-AddressesKit-devel

Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-XMPPKit gnustep-Etoile-AddressesKit

%description
A instant messenger for jabber.

%package docs
Summary: Documentation for StepChat
Group: Documentation
BuildArch: noarch

%description docs
A instant messenger for jabber.

This package contains documentation for StepChat.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=StepChat

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=StepChat

install -d %buildroot%_docdir/GNUstep/StepChat
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/StepChat/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README LICENSE
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files docs
%_docdir/GNUstep

%changelog
* Mon Mar 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.git20131126
- Added menu file (thnx kostyalamer@)

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20131126
- Initial build for Sisyphus

