%set_verify_elf_method unresolved=strict

Name: gnustep-Vespucci
Version: 0.1
Release: alt1.cvs20140125
Summary: Vespucci is a navigator for the World Wide Web
License: Free
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/vespucci/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/user-apps/Vespucci
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-simplewebkit-devel

Requires: gnustep-simplewebkit

%description
Vespucci is a web browser which uses a WebKit-compatible rendering
engine, thus it can either use Apple's WebKit or GNUstep's SimpleWebKit.

Features:

* multiple-document support, with recent document list
* standard back/forward buttons
* bookmarks, in Safari-compatible format (it can read safari bookmarks
  directly)
* Workspace integration
* webloc link file support (just copy over the file from Mac)
* Open URL service
* Cookie management

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
%_bindir/*
%_libdir/GNUstep

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140125
- Initial build for Sisyphus

