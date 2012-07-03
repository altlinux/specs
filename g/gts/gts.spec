Name: gts
Version: 0.7.6
Release: alt2.cvs20111025
Summary: GNU Triangulated Surface Library
License: LGPL v2
Group: Development/Tools
Url: http://gts.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: libgtk+2-devel libnetpbm-devel

%description
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

%package -n lib%name
Summary: Shared library of GNU Triangulated Surface Library
Group: System/Libraries

%description -n lib%name
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

This package contains a shared library of GNU Triangulated Surface Library.

%package -n lib%name-devel
Summary: Development files of GNU Triangulated Surface Library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

This package contains development files of GNU Triangulated Surface Library.

%package -n lib%name-devel-static
Summary: Static library of GNU Triangulated Surface Library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

This package contains static library of GNU Triangulated Surface Library.

%package -n lib%name-devel-doc
Summary: Documentation for GNU Triangulated Surface Library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

This package contains development documentation for GNU Triangulated Surface
Library.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

#install -d %buildroot%_docdir/%name/html
install -d %buildroot%_docdir/%name/examples
#install -m644 doc/html/* %buildroot%_docdir/%name/html
install -m644 examples/*.c %buildroot%_docdir/%name/examples

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%_bindir/*
%exclude %_bindir/%name-config

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_aclocaldir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name
%_man1dir/*

%changelog
* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt2.cvs20111025
- New snapshot

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt2.cvs20110121
- New snapshot
- Disabled devel-static package

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt2.cvs20100321.2
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt2.cvs20100321.1
- Rebuilt for soname set-versions

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt2.cvs20100321
- New snapshot

* Mon May 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1
- Initial build for Sisyphus

