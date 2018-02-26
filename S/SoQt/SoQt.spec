Name: SoQt
Version: 1.5.0
Release: alt6
Summary: Qt GUI component toolkit library for Coin
License: GPL
Group: Development/Tools
Url: http://www.coin3d.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://ftp.coin3d.org/coin/src/all/SoQt-1.5.0.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: libGL-devel libGLU-devel doxygen gcc-c++ gcc-fortran
BuildPreReq: libX11-devel libcoin3d-devel libqt4-devel

%description
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

%package -n lib%name
Summary: Shared libraries of SoQt
Group: System/Libraries
Requires: libcoin3d
Conflicts: %name < %version-%release

%description -n lib%name
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

This package contains shared libraries of SoQt.

%package -n lib%name-devel
Summary: Development files for SoQt
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libcoin3d-devel
Conflicts: %name < %version-%release
Conflicts: xinetd-devel

%description -n lib%name-devel
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

This package contains development files for SoQt.

%package -n lib%name-devel-doc
Summary: Documentation for SoQt
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

This package contains development documentation for SoQt.

%prep
%setup

%build
export QTDIR=%_qt4dir
export CPPFLAGS="%optflags"
%configure \
	--disable-static \
	--enable-html \
	--enable-man \
	--enable-html-help \
	--enable-debug=no \
	--enable-symbols=no \
	--with-doxygen=%_bindir \
	--with-x \
	--with-mesa \
	--with-coin=%prefix \
	--with-opengl=%prefix \
	--with-qt=%_qt4dir
%make_build

%install
touch htmlhelp/SoQt-1_5.chm
%makeinstall_std

#install -d %buildroot%_docdir/%name
#mv %buildroot%_datadir/SoQt/html %buildroot%_docdir/%name/

%files

%files -n lib%name
%doc AUTHORS BUGS.txt COPYING ChangeLog FAQ LICENSE.GPL NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/*
%_man1dir/*
%_datadir/Coin/conf/*
%_libdir/*.so
%_includedir/*
%_aclocaldir/*
%_man3dir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc docs/*
%doc %_docdir/soqt

%changelog
* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt6
- Rebuilt with coin3d 3.1.3-alt5

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt5
- Added -g into compiler flags

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt4
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt3
- Rebuilt with set-versioned libXi

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Rebuilt for soname set-versions

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt4
- Rebuilt without libcoin3d-devel-static

* Mon May 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt3
- Rebuild for Qt4

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.M50.1
- Port for Branch 5.0

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt2
- lib%name-devel: added explicit conflict with xinetd-devel

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt0.M50.1
- Port for Branch 5.0

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.2
- Remove common package

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.1
- Disable static library
- Fix for x86_64

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
