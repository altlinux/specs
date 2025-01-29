%define sover 1

%def_enable static

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

Name: m4ri
Version: 20250128
Release: alt1

Summary: Linear Algebra over F_2

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://bitbucket.org/malb/m4ri

Source: %url/downloads/%name-%version.tar.gz
Vcs: git://github.com/malb/m4ri.git

# Fix a format specifier.
Patch: m4ri-20240729-printf.patch

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: libpng-devel

%description
M4RI is a library for fast arithmetic with dense matrices over F_2.
The name M4RI comes from the first implemented algorithm: The "Method
of the Four Russians" inversion algorithm published by Gregory Bard.
M4RI is used by the Sage mathematics software and the BRiAl library.

%package -n lib%name%sover
Summary: %summary
Group: System/Libraries

%description -n lib%name%sover
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

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
The package contains documentation for %name.

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

%files -n lib%name%sover
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files doc
%doc AUTHORS COPYING
%doc doc/html

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Wed Jan 29 2025 Leontiy Volodin <lvol@altlinux.org> 20250128-alt1
- New version 20250128.
- Added vcs tag.
- Packaged documentation separately.

* Thu Oct 03 2024 Leontiy Volodin <lvol@altlinux.org> 20240729-alt2
- Fixed build libm4rie.

* Tue Oct 01 2024 Leontiy Volodin <lvol@altlinux.org> 20240729-alt1
- New version 20240729.

* Mon Oct 25 2021 Leontiy Volodin <lvol@altlinux.org> 20200125-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
