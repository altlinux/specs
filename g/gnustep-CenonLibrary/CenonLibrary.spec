Name: gnustep-CenonLibrary
Version: 4.0.0.1
Release: alt1.qa1
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

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Cenon/Projects/Cenon.cenon/document

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.0.1-alt1.qa1
- NMU: applied repocop patch

* Wed Apr 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0.1-alt1
- Initial build for Sisyphus

