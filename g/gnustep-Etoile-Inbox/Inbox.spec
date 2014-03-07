%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-Inbox
Version: r7769
Release: alt1.git20120717
Summary: Unified messaging system
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/Inbox.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-RSSkit-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-EtoileUI-devel gnustep-Pantomime-devel

Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-EtoileUI gnustep-RSSkit gnustep-Pantomime

%description
Unified messaging system.

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
	PROJECT_NAME=Inbox

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=Inbox

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc README TODO
%_bindir/*
%_libdir/GNUstep

%changelog
* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r7769-alt1.git20120717
- Initial build for Sisyphus

