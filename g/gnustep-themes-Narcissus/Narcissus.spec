%set_verify_elf_method unresolved=strict

Name: gnustep-themes-Narcissus
Version: r9538
Release: alt2.svn20131105
Summary: GNUstep's Narcissus theme
License: Free
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/etoile/mockups/narcissus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/etoile/trunk/Etoile/Themes/Narcissus.theme/
Source: %name-%version.tar

Requires: gnustep-back

%description
Narcissus theme for GNUstep.

%prep
%setup

%install
install -d %buildroot%_libdir/GNUstep/Themes/Narcissus.theme
cp -fR Resources %buildroot%_libdir/GNUstep/Themes/Narcissus.theme/

%files
%_libdir/GNUstep

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9538-alt2.svn20131105
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9538-alt1.svn20131105
- Version r9538

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9160-alt1.svn20130928
- Version r9160

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r6046-alt1.svn20100419
- Initial build for Sisyphus

