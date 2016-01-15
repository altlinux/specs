%set_verify_elf_method unresolved=strict

Name: gnustep-Bean
Version: 0.1
Release: alt4.cvs20140127.1
Summary: A word processor
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/bean/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/ported-apps/Util/Bean
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-pbxbuild

Requires: gnustep-back

%description
A word processor.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

pbxbuild -p Bean.xcodeproj -g

%make_build -C pbxbuild \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std -C pbxbuild GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.cvs20140127.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4.cvs20140127
- Built with clang

* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.cvs20140127
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.cvs20140127
- Added Requires: gnustep-back

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140127
- Initial build for Sisyphus

