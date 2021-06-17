Name: bliss
%define lname   libbliss-0_73
Version: 0.73
Release: alt1
Summary: A Tool for Computing Automorphism Groups and Canonical Labelings of Graphs
License: LGPL-3.0
Group: Sciences/Mathematics
Url: http://www.tcs.hut.fi/Software/bliss/

Source: http://www.tcs.hut.fi/Software/bliss/%name-%version.zip
Patch1: bliss-am.diff
Patch2: bliss-nodate.diff
BuildRequires: automake
BuildRequires: gcc-c++
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
%add_optflags -lgmp
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -f "%buildroot/%_libdir"/*.la

%files
%doc COPYING*
%_bindir/bliss*

%files -n %lname
%_libdir/libbliss-0.73.so
%_libdir/libbliss_gmp-0.73.so

%files devel
%_libdir/libbliss.so
%_libdir/libbliss_gmp.so
%_includedir/bliss/

%changelog
* Sat Jun 12 2021 Leontiy Volodin <lvol@altlinux.org> 0.73-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
