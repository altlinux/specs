%set_verify_elf_method unresolved=strict

Name: gnustep-themes-Nesedah
Version: r9537
Release: alt3.svn20131105
Summary: GNUstep's Nesedah theme
License: Free
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/etoile/trunk/Etoile/Themes/Nesedah.theme/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

Requires: gnustep-back

%description
Nesedah theme for GNUstep.

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
%_libdir/GNUstep

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9537-alt3.svn20131105
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9537-alt2.svn20131105
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9537-alt1.svn20131105
- Version r9537

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9169-alt1.svn20131001
- Version r9169

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r7355-alt1.svn20111116
- Initial build for Sisyphus

