%set_verify_elf_method unresolved=strict

Name: gnustep-LoginPanel
Version: 20140127
Release: alt4.cvs20140127
Summary: GNUstep login panel
License: LGPLv2+
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/loginpanel/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/system-apps/loginpanel
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libX11-devel

Requires: gnustep-back

%description
GNUstep login panel.

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
%doc ChangeLog README*
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt4.cvs20140127
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt3.cvs20140127
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt2.cvs20140127
- Added Requires: gnustep-back

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt1.cvs20140127
- Initial build for Sisyphus

