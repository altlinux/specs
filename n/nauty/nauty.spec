%define lver 2_8_8

Name: nauty
Version: 2.8.8
Release: alt1
Epoch: 1

Summary: Tools for computing automorphism groups of graphs

License: Apache-2.0
Group: Sciences/Mathematics
Url: https://pallini.di.uniroma1.it/

# Source-url: https://pallini.di.uniroma1.it/nauty%lver.tar.gz
Source: nauty-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: automake libgmp-devel libtool >= 2 zlib-devel

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

%package -n lib%{name}-%lver
Summary: Graph automorphism group computation with Nauty
Group: System/Libraries

%description -n lib%{name}-%lver
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

%package devel
Summary: Development files for nauty, a math library
Group: Development/Other
Requires: lib%{name}-%lver = %version

%description devel
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

This subpackage contains the header files for developing
applications that want to make use of libnauty.

%prep
%setup
%patch -p1

%build
rm -f makefile
%autoreconf
export CFLAGS="%optflags -Wno-unused"
%configure --enable-generic
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%doc changes24-28.txt
%doc COPYRIGHT

%files -n lib%{name}-%lver
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
%ifnarch armh i586
%_libdir/libnautyQ0.so
%_libdir/libnautyQ1.so
%endif

%changelog
* Wed Nov 29 2023 Leontiy Volodin <lvol@altlinux.org> 1:2.8.8-alt1
- New version 2.8.8.

* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 1:2.8.6-alt1
- New version 2.8.6.

* Fri Jul 15 2022 Leontiy Volodin <lvol@altlinux.org> 27r4-alt1
- New version (27r4).

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.7.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
