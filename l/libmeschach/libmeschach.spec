%define        _unpackaged_files_terminate_build 1
%define        oname meschach

Name:          lib%{oname}
Version:       1.3.0
Release:       alt0.1
Summary:       C-language library of routines for performing matrix computations
License:       Freely redistributable without restriction
Group:         Sciences/Mathematics
Url:           http://homepage.math.uiowa.edu/~dstewart/meschach/
Vcs:           https://github.com/yageek/Meschach.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
Meschach is a C-language library of routines for performing matrix
computations. It has a collection of data structures which are
self-contained, can be created, destroyed and resized at will which
includes permutations, vectors, matrices, integer vectors, complex
vectors and matrices and sparse matrices.

%package       devel
Summary:       Development files of Meschach
Group:         Development/C

%description   devel
This package contains development files of Meschach.

Meschach is a C-language library of routines for performing matrix
computations. It has a collection of data structures which are
self-contained, can be created, destroyed and resized at will which
includes permutations, vectors, matrices, integer vectors, complex
vectors and matrices and sparse matrices.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DARCH:STRING=%_arch -DBUILD_SHARED_LIBS:BOOL=ON 
%cmake_build

%install
%cmakeinstall_std

%files
%doc README copyright
%_libdir/*.so.*

%files         devel
%doc README copyright DOC/*
%_libdir/*.so
%_includedir/*
%_cmakedir/*


%changelog
* Tue Feb 11 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt0.1
- ^ 1.2b -> 1.3.0 (pre)
- * rename to lib%oname

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b.3
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b.2
- Rebuilt for debuginfo

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b.1
- Fixed headers

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b
- Initial build for Sisyphus

