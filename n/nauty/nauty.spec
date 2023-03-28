Name: nauty
%define lname   libnauty-2_8_6
Version: 2.8.6
Release: alt1
Epoch: 1
Summary: Tools for computing automorphism groups of graphs
License: Apache-2.0
Group: Sciences/Mathematics
Url: http://pallini.di.uniroma1.it/

Source: http://pallini.di.uniroma1.it/nauty%version.tar.gz
Patch1: nauty-am.diff
Patch2: nauty-uninitialized.diff
BuildRequires: automake
BuildRequires: libgmp-devel
BuildRequires: libtool >= 2
BuildRequires: zlib-devel

%description
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs (*Traces does not accept digraphs at this time).
They can also produce a canonical label. They are written in a
portable subset of C, and run on a considerable number of different
systems.

There is a small suite of programs called gtools included in the
package. For example, geng can generate non-isomorphic graphs very
quickly. There are also generators for bipartite graphs, digraphs,
and multigraphs.

%package -n %lname
Summary: Graph automorphism group computation with Nauty
Group: System/Libraries

%description -n %lname
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

%package devel
Summary: Development files for nauty, a math library
Group: Development/Other
Requires: %lname = %version

%description devel
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

This subpackage contains the header files for developing
applications that want to make use of libnauty.

%prep
%setup -n nauty%version
%autopatch -p1

%build
rm -f makefile
%autoreconf
export CFLAGS="%optflags -Wno-unused"
%configure --disable-popcnt --disable-clz
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%doc changes24-28.txt
%doc COPYRIGHT

%files -n %lname
%_libdir/libnauty*-%version.so

%files devel
%_includedir/nauty/
%_libdir/libnauty.so
%_libdir/libnautyA1.so
%_libdir/libnautyL0.so
%_libdir/libnautyL1.so
%_libdir/libnautyS0.so
%_libdir/libnautyS1.so
%_libdir/libnautyW0.so
%_libdir/libnautyW1.so

%changelog
* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 1:2.8.6-alt1
- New version 2.8.6.

* Fri Jul 15 2022 Leontiy Volodin <lvol@altlinux.org> 27r4-alt1
- New version (27r4).

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.7.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
