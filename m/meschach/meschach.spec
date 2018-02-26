%define sover 0

Name: meschach
Version: 1.2
Release: alt1.b.3
Summary: C-language library of routines for performing matrix computations
License: Free
Group: Sciences/Mathematics
Url: http://www.math.uiowa.edu/~dstewart/meschach/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
Meschach is a C-language library of routines for performing matrix
computations. It has a collection of data structures which are
self-contained, can be created, destroyed and resized at will which
includes permutations, vectors, matrices, integer vectors, complex
vectors and matrices and sparse matrices.

%package -n lib%name
Summary: C-language library of routines for performing matrix computations
Group: System/Libraries

%description -n lib%name
Meschach is a C-language library of routines for performing matrix
computations. It has a collection of data structures which are
self-contained, can be created, destroyed and resized at will which
includes permutations, vectors, matrices, integer vectors, complex
vectors and matrices and sparse matrices.

%package -n lib%name-devel
Summary: Development files of Meschach
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Meschach is a C-language library of routines for performing matrix
computations. It has a collection of data structures which are
self-contained, can be created, destroyed and resized at will which
includes permutations, vectors, matrices, integer vectors, complex
vectors and matrices and sparse matrices.

This package contains development files of Meschach.

%prep
%setup

%build
%configure --with-all
%make_build all

%install
gcc -shared -Wl,-whole-archive %name.a -Wl,-no-whole-archive \
	-o lib%name.so.%sover -Wl,-soname,lib%name.so.%sover -lm

install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name

install -m644 *.so.* %buildroot%_libdir
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so
install -p -m644 *.h %buildroot%_includedir/%name

%brp_strip_debug %_libdir/*.so*

%files -n lib%name
%doc README copyright
%_libdir/*.so.*

%files -n lib%name-devel
%doc DOC/*
%_libdir/*.so
%_includedir/*

%changelog
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b.3
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b.2
- Rebuilt for debuginfo

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b.1
- Fixed headers

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b
- Initial build for Sisyphus

