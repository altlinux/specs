%def_enable static

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

Name: m4ri
Version: 20240729
Release: alt2
Summary: Linear Algebra over F_2
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://bitbucket.org/malb/m4ri

Source: %url/downloads/%name-%version.tar.gz

# This patch will not be sent upstream, as it is Fedora-specific.
# Permanently disable SSE3 and SSSE3 detection.  Without this patch, the
# config file tends to be regenerated at inconvenient times.
Patch: m4ri-20240729-no-sse3.patch
# Fix a format specifier.
Patch1: m4ri-20240729-printf.patch
# Remove an unnecessary direct library dependency from the pkgconfig file,
# and also cflags used to compile m4ri, but not needed by consumers of m4ri.
Patch2: m4ri-20240729-pkgconfig.patch

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: libpng-devel

%description
M4RI is a library for fast arithmetic with dense matrices over F_2.
The name M4RI comes from the first implemented algorithm: The "Method
of the Four Russians" inversion algorithm published by Gregory Bard.
M4RI is used by the Sage mathematics software and the BRiAl library.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
M4RI is a library for fast arithmetic with dense matrices over F_2.
The name M4RI comes from the first implemented algorithm: The "Method
of the Four Russians" inversion algorithm published by Gregory Bard.
M4RI is used by the Sage mathematics software and the BRiAl library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Provides: bundled(jquery)

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static library files for %name
Group: Development/C

%description -n lib%name-devel-static
The %name-static package contains the static %name library.
%endif

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

# Fix the version number in the documentation, and generate only HTML
%__subst 's/20140914/%version/;/GENERATE_LATEX/s/YES/NO/' m4ri/Doxyfile

%build
%autoreconf
%configure \
  --enable-openmp \
%ifarch x86_64
  --enable-sse2

sed -e 's/^#undef HAVE_MMX/#define HAVE_MMX/' \
    -e 's/^#undef HAVE_SSE$/#define HAVE_SSE/' \
    -e 's/^#undef HAVE_SSE2/#define HAVE_SSE2/' \
    -i m4ri/config.h
sed -e 's/^\(#define __M4RI_HAVE_SSE2[[:blank:]]*\)0/\11/' \
    -e 's/^\(#define __M4RI_SIMD_CFLAGS[[:blank:]]*\).*/\1" -mmmx -msse -msse2"/' \
    -i m4ri/m4ri_config.h
%__subst 's/^SIMD_CFLAGS =.*/SIMD_CFLAGS = -mmmx -msse -msse2/' Makefile
%else
  --disable-sse2
%endif

# Die, rpath, die!
sed -e "s|\(hardcode_libdir_flag_spec=\)'.*|\1|" \
    -e "s|\(runpath_var=\)LD_RUN_PATH|\1|" \
    -i libtool

%make_build

# Build documentation
cd m4ri
doxygen
cd -

%install
%makeinstall_std
rm -f %buildroot%_libdir/lib%name.la
%if_disabled static
rm -f %buildroot%_libdir/lib%name.a
%endif

%check
make check LD_LIBRARY_PATH=$PWD/.libs

%files -n lib%name
%doc AUTHORS
%doc COPYING
%_libdir/lib%name-0.0.%version.so

%files -n lib%name-devel
%doc doc/html
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Thu Oct 03 2024 Leontiy Volodin <lvol@altlinux.org> 20240729-alt2
- Fixed build libm4rie.

* Tue Oct 01 2024 Leontiy Volodin <lvol@altlinux.org> 20240729-alt1
- New version 20240729.

* Mon Oct 25 2021 Leontiy Volodin <lvol@altlinux.org> 20200125-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
