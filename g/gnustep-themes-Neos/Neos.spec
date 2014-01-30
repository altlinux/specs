%set_verify_elf_method unresolved=strict

Name: gnustep-themes-Neos
Version: 0.1
Release: alt2
Summary: GNUstep's Neos theme
License: Public domain
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/themes/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

Requires: gnustep-back

%description
Neos theme for GNUstep.

%prep
%setup

%install
install -d %buildroot%_libdir/GNUstep/Themes
cp -fR Neos.theme %buildroot%_libdir/GNUstep/Themes/

%files
%_libdir/GNUstep

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

