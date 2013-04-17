Name: gnustep-CenonLibrary
Version: 4.0.0.1
Release: alt1
Summary: Cenon Library
License: vhfPL
Group: Graphical desktop/GNUstep
Url: http://www.cenon.info/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
Cenon is a graphical tool of a special kind. Build upon a modular
graphical core, Cenon offers a wide variety of possibilities and
applications.

This package contains Cenon Library.

%prep
%setup -n Cenon


%install
install -d %buildroot%_libdir/GNUstep
cd ..
cp -fR Cenon %buildroot%_libdir/GNUstep/

%files
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Cenon/Projects/Cenon.cenon/document

%changelog
* Wed Apr 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0.1-alt1
- Initial build for Sisyphus

