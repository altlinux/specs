Name: judy
Version: 1.0.5
Release: alt2
Summary: Judy is a C library that implements a dynamic array
License: LGPLv2.1
Group: Sciences/Mathematics
Url: https://sourceforge.net/projects/judy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): gcc-c++ gcc libstdc++-devel

Requires: lib%name = %version-%release

%description
Judy is a C library that implements a dynamic array. Empty Judy arrays
are declared with null pointers. A Judy array consumes memory only when
populated yet can grow to take advantage of all available memory. Judy's
key benefits are: scalability, performance, memory efficiency, and ease
of use.

%package -n lib%name
Summary: Shared libraries of Judy
Group: System/Libraries

%description -n lib%name
Judy is a C library that implements a dynamic array. Empty Judy arrays
are declared with null pointers. A Judy array consumes memory only when
populated yet can grow to take advantage of all available memory. Judy's
key benefits are: scalability, performance, memory efficiency, and ease
of use.

This package contains shared libraries of Judy.

%package -n lib%name-devel
Summary: Development files of Judy
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Judy is a C library that implements a dynamic array. Empty Judy arrays
are declared with null pointers. A Judy array consumes memory only when
populated yet can grow to take advantage of all available memory. Judy's
key benefits are: scalability, performance, memory efficiency, and ease
of use.

This package contains development files of Judy.

%package -n lib%name-devel-doc
Summary: Documentation for Judy
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Judy is a C library that implements a dynamic array. Empty Judy arrays
are declared with null pointers. A Judy array consumes memory only when
populated yet can grow to take advantage of all available memory. Judy's
key benefits are: scalability, performance, memory efficiency, and ease
of use.

This package contains development documentation of Judy.

%prep
%setup

rm -fR autom4te.cache

%build
%add_optflags -fno-strict-aliasing -fpermissive
%autoreconf

%configure
for i in $(find ./ -name Makefile); do
	sed -i 's|%_arch-alt-linux-gcc|g++|g' $i
done

%make_build

%install
%makeinstall_std

install -d %buildroot%_bindir
install -m644 tool/jhton %buildroot%_bindir

%files
%_bindir/*

%files -n lib%name
%doc AUTHORS COPYING ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/*/*
%doc examples

%changelog
* Sun Oct 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt2
- Provided Judy1, JudySL and JudyHS (ALT #27813)

* Thu May 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus

