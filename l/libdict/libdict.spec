Name: libdict
Version: 0.3.0
Release: alt2.git20140826

Summary: C library of key-value data structures with an object-oriented interface
License: BSD
Group: System/Libraries

Url: https://github.com/fmela/libdict
# https://github.com/fmela/libdict.git
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%description
libdict is a C library that provides the following data structures with
efficient insert, lookup, and delete routines:

* height-balanced (AVL) tree
* red-black tree
* splay tree
* weight-balanced tree
* path-reduction tree
* treap
* hashtable, using separate chaining
* hashtable, using open addressing with linear probing

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
libdict is a C library that provides the following data structures with
efficient insert, lookup, and delete routines:

* height-balanced (AVL) tree
* red-black tree
* splay tree
* weight-balanced tree
* path-reduction tree
* treap
* hashtable, using separate chaining
* hashtable, using open addressing with linear probing

This package contains development files for %name.

%prep
%setup

%build
%make_build

%install
%if "%_lib" == "lib64"
LIB_SUFFIX=64
%endif
%makeinstall_std \
	INSTALL_PREFIX=%buildroot%prefix \
	LIB_SUFFIX=$LIB_SUFFIX

%files
%doc README.md REFERENCES TODO
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Jun 29 2019 Michael Shigorin <mike@altlinux.org> 0.3.0-alt2.git20140826
- fixed build on 64-bit architectures
- minor spec cleanup

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20140826
- Initial build for Sisyphus

