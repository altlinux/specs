%def_with openblas

Name: linbox
%define lname   liblinbox0
Version: 1.7.0
Release: alt1
Summary: C++ library for computation with matrices over ints and finite fields
License: LGPL-2.1+
Group: Sciences/Mathematics
Url: https://linalg.org/

Source: https://github.com/linbox-team/linbox/releases/download/v%version/linbox-%version.tar.gz

Patch: remove-linboxsage-libs-from-pc.patch
Patch1: fix-ksh-pkgconfig.patch
Patch2: linbox-pr-256.patch

# Couldn't find package libatlas-devel on aarch64, armh and ppc64le.
%if_without openblas
ExclusiveArch: i586 x86_64
%endif

BuildRequires: autoconf >= 2.61
BuildRequires: automake >= 1.8
BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: libiml-devel
BuildRequires: libm4ri-devel
BuildRequires: libm4rie-devel
BuildRequires: libmpfr-devel
BuildRequires: libntl-devel
BuildRequires: libflint2-devel
%if_with openblas
BuildRequires: libopenblas-devel
%else
BuildRequires: libatlas-devel
%endif
BuildRequires: fflas-ffpack-devel
BuildRequires: libtinyxml2-devel

%description
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package -n %lname
Summary: C++ library for computation with matrices over ints and finite fields
Group: System/Libraries

%description -n %lname
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package -n lib%name-devel
Summary: Development files for LinBox, a library for computation over finite fields
Group: Development/Other

%description -n lib%name-devel
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

This subpackage contains the include files and library links for
developing against the Givaro library.

%prep
%setup
# %%patch -p1
# %%patch1 -p1
# %%patch2 -p1

%build
%if_with openblas
export LIBS+="-L%_libdir -lgivaro -lopenblas -lgmp"
%endif

%autoreconf
%configure --disable-static \
%ifarch %ix86
  --disable-sse --disable-sse2 \
%endif
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-sse42 \
  --disable-avx --disable-avx2 --disable-fma --disable-fma4 \
  --enable-gmp=yes \
  %if_with openblas
    --enable-openblas=yes \
    --with-blas-libs=" -lopenblas" \
  %endif
#

# Get rid of undesirable hardcoded rpaths, and workaround libtool reordering
# -Wl,--as-needed after all the libraries.
# sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
#     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
#     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
#     -i libtool

%make_build

%install
%makeinstall_std
rm -f "%buildroot/%_libdir"/*.la

%files -n %lname
%_libdir/liblinbox.so.0*

%files -n lib%name-devel
%_bindir/*-config
%_includedir/%name/
%_libdir/liblinbox.so
%_pkgconfigdir/*.pc
%_man1dir/*.1*
%doc COPYING*

%changelog
* Tue Jul 19 2022 Leontiy Volodin <lvol@altlinux.org> 1.7.0-alt1
- New version (1.7.0).
- Built with openblas instead atlas.

* Mon Nov 29 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.3-alt2
- Fixed build with sagemath.
- Added buildrequires.

* Thu Nov 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
