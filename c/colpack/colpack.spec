Name: colpack
Version: 1.0.4
Release: alt1
Summary: Graph Coloring for Computing Derivatives
License: LGPL v3
Group: Sciences/Mathematics
Url: http://www.cscapes.org/coloringpage/index.htm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cscapes.org/download/ColPack/ColPack-%version.tar.gz

BuildPreReq: gcc-c++

%description
ColPack: Graph Coloring for Computing Derivatives.

%package -n lib%name
Summary: Shared library of Graph Coloring for Computing Derivatives
Group: System/Libraries

%description -n lib%name
ColPack: Graph Coloring for Computing Derivatives.

This package contains shared library of ColPack.

%package -n lib%name-devel
Summary: Development files of Graph Coloring for Computing Derivatives
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
ColPack: Graph Coloring for Computing Derivatives.

This package contains development files of ColPack.

%prep
%setup
rm -fR $(find ./ -name '.svn')

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name

install -m755 ColPack %buildroot%_bindir
cp -P build/lib/*.so* %buildroot%_libdir/
install -m644 build/include/* %buildroot%_includedir/%name

%files
%doc AUTHOR
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Version 1.0.4

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuilt for debuginfo

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

