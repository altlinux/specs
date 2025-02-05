%define lver 2_8_9

Name: nauty
Version: 2.8.9
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

%package -n lib%name%version
Summary: Graph automorphism group computation with Nauty
Group: System/Libraries
Provides: lib%name-2_8_8 = %EVR
Obsoletes: lib%name-2_8_8 < %EVR

%description -n lib%name%version
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

%package -n lib%name-devel
Summary: Development files for nauty, a math library
Group: Development/Other
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

This subpackage contains the header files for developing
applications that want to make use of libnauty.

%prep
%setup
%patch -p1
rm -f makefile aclocal.m4

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
export CFLAGS="%optflags -Wno-unused"
%autoreconf
%configure --enable-generic --includedir=%_includedir/nauty
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/{*.la,*.a}

%files
%_bindir/*
%doc changes24-28.txt
%doc COPYRIGHT

%files -n lib%name%version
%_libdir/libnauty*-%version.so

%files -n lib%name-devel
%_includedir/nauty/
%_libdir/libnauty.so
%_libdir/libnauty1.so
%_libdir/libnautyL.so
%_libdir/libnautyL1.so
%ifnarch armh i586
%_libdir/libnautyQ.so
%_libdir/libnautyQ1.so
%endif
%_libdir/libnautyS.so
%_libdir/libnautyS1.so
%_libdir/libnautyW.so
%_libdir/libnautyW1.so
%_pkgconfigdir/libnauty*.pc

%changelog
* Wed Feb 05 2025 Leontiy Volodin <lvol@altlinux.org> 1:2.8.9-alt1
- New version 2.8.9.
- Renamed:
  + lib%%name-%%lver -> lib%%name%%version.
  + %%name-devel -> lib%%name-devel.

* Wed Nov 29 2023 Leontiy Volodin <lvol@altlinux.org> 1:2.8.8-alt1
- New version 2.8.8.

* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 1:2.8.6-alt1
- New version 2.8.6.

* Fri Jul 15 2022 Leontiy Volodin <lvol@altlinux.org> 27r4-alt1
- New version (27r4).

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.7.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
