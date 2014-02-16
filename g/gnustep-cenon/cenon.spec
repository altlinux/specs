Name: gnustep-cenon
Version: 4.0.2
Release: alt3
Summary: Vector graphics tool for GNUstep
License: vhfPL
Group: Graphical desktop/GNUstep
Url: http://www.cenon.info/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-CenonLibrary

%description
Cenon is a vector graphics tool for GNUstep. It is built upon a modular
graphical core, and offers a variety of applications beyond desktop
publishing.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

TOPDIR=$PWD
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-DMAXFLOAT=3.40282347e+38F -I$TOPDIR -I$TOPDIR/GraphicObjects.subproj"
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

install -d %buildroot%_libdir/GNUstep
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%doc NEWS README COPYRIGHT LICENSE ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3
- Applied repocop patch

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Built with clang

* Mon Mar 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

