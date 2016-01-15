%set_verify_elf_method unresolved=strict

Name: gnustep-Switcher
Version: 20140127
Release: alt3.cvs20140127.1
Summary: Allow applications to appear when the icon is clicked on from another workspace
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@cvs.savannah.gnu.org:/sources/gap co gap/bundles/Switcher
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
This is a quick hack to allow applications to appear when the icon is
clicked on from another workspace.

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

%files
%doc README ChangeLog
%_libdir/GNUstep

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 20140127-alt3.cvs20140127.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt3.cvs20140127
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt2.cvs20140127
- Added Requires: gnustep-back

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt1.cvs20140127
- Initial build for Sisyphus

