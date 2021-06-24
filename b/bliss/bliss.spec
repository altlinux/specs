Name: bliss
%define lname   libbliss-0_77
Version: 0.77
Release: alt1
Summary: A Tool for Computing Automorphism Groups and Canonical Labelings of Graphs
License: LGPL-3.0
Group: Sciences/Mathematics
Url: https://users.aalto.fi/~tjunttil/bliss/

Source: %url/downloads/%name-%version.zip
Patch1: bliss-nodate.diff
Patch2: cmake.patch
BuildRequires: gcc-c++
BuildRequires: cmake rpm-build-ninja
BuildRequires: libgmp-devel
BuildRequires: libtool
BuildRequires: unzip

%description
bliss is a tool for computing automorphism groups and canonical forms
of graphs. It has both a command line user interface as well as C++
and C programming language APIs.

%package -n %lname
Summary: Library for computing automorphism groups and canonical forms of graphs
Group: System/Libraries

%description -n %lname
bliss is a tool for computing automorphism groups and canonical forms
of graphs.

%package devel
Summary: Development files for bliss, a math library
Group: Development/Other
Requires: %lname = %version

%description devel
bliss is a tool for computing automorphism groups and canonical forms
of graphs.

This subpackage contains libraries and header files for developing
applications that want to make use of the Bliss library.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake \
    -GNinja \
    -DBUILD_STATIC=OFF \
    -DUSE_GMP=ON \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
#
%cmake_build

%install
%cmake_install

%files
%doc COPYING*
%_bindir/bliss*

%files -n %lname
%_libdir/libbliss.so.%version

%files devel
%doc CHANGES.txt README.txt
%_libdir/libbliss.so
%_includedir/bliss/

%changelog
* Wed Jun 23 2021 Leontiy Volodin <lvol@altlinux.org> 0.77-alt1
- New version (0.77) with rpmgs script.
- Changed url.
- Built with cmake.
- Updated patches (thanks opensuse).

* Sat Jun 12 2021 Leontiy Volodin <lvol@altlinux.org> 0.73-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
