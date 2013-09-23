Name: sparsehash
Version: 2.0.2
Release: alt1

Summary: Google's extremely memory-efficient C++ hash_map implementation
License: BSD
Group: Development/C++

URL: http://code.google.com/p/sparsehash/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://sparsehash.googlecode.com/files/%name-%version.tar.gz

BuildRequires: gcc-c++

%description
The Google SparseHash project contains several C++ template hash-map
implementations in use at Google, with different performance
characteristics, including an implementation that optimizes for space
and one that optimizes for speed.

%package -n lib%name
Summary: Google's extremely memory-efficient C++ hash_map implementation
Group: Development/C++
BuildArch: noarch
Provides: libgoogle-%name = %version-%release
Obsoletes: libgoogle-%name <= 1.5.2

%description -n lib%name
The Google SparseHash project contains several C++ template hash-map
implementations in use at Google, with different performance
characteristics, including an implementation that optimizes for space
and one that optimizes for speed.

%package -n lib%name-devel
Summary: Google's extremely memory-efficient C++ hash_map implementation
Group: Development/C++
Requires: lib%name
Provides: libgoogle-%name = %version-%release
Obsoletes: libgoogle-%name <= 1.5.2

%description -n lib%name-devel
The Google SparseHash project contains several C++ template hash-map
implementations in use at Google, with different performance
characteristics, including an implementation that optimizes for space
and one that optimizes for speed.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc %_docdir/sparsehash-%version

%files -n lib%name-devel
%_includedir/google
%_includedir/%name
%_pkgconfigdir/lib%name.pc

%changelog
* Mon Sep 23 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.1
- Fixed build

* Wed Nov 11 2009 Maxim Ivanov <redbaron at altlinux.org> 1.5.2-alt1
- Initial build for ALT Linux

