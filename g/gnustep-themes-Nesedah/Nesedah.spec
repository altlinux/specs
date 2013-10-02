%set_verify_elf_method unresolved=strict

Name: gnustep-themes-Nesedah
Version: r9169
Release: alt1.svn20131001
Summary: GNUstep's Nesedah theme
License: Free
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/etoile/trunk/Etoile/Themes/Nesedah.theme/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
Nesedah theme for GNUstep.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%_libdir/GNUstep

%changelog
* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9169-alt1.svn20131001
- Version r9169

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r7355-alt1.svn20111116
- Initial build for Sisyphus

