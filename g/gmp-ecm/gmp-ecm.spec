%define so_version 1

Name: gmp-ecm
Version: 7.0.4
Release: alt1

Summary: Elliptic Curve Method for Integer Factorization

License: GPL-3.0
Group: Sciences/Mathematics
Url: https://gforge.inria.fr/projects/ecm

Source: https://gforge.inria.fr/frs/download.php/36224/ecm-%version.tar.gz

BuildRequires: libgmp-devel

%description
GMP-ECM reads the numbers to be factored from stdin (one number on each
line) and requires a numerical parameter, the stage 1 bound B1. A reasonable
stage 2 bound B2 for the given B1 is chosen by default, but can be overridden
by a second numerical parameter. By default, GMP-ECM uses the ECM factoring
algorithm.

%package -n libecm%so_version
Summary: Library for Elliptic Curve Integer Factorization
Group: System/Libraries

%description -n libecm%so_version
Library for ecm. To use the library, you need to install ecm-devel, include
"ecm.h" in your source file and link with -lecm.

%package -n libecm-devel
Summary: Development files for the gmp-ecm package
Group: Development/C++

%description -n libecm-devel
This package contains header files required when building applications which
use the libecm library.

%prep
%setup -n ecm-%version

%build
%configure \
%ifnarch x86_64
    --disable-sse2 \
%endif
    --disable-shellcmd \
    --enable-shared \
    --disable-static

# Eliminate hardcoded rpaths; workaround libtool reordering -Wl,--as-needed
# after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build

%install
%makeinstall_std

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc AUTHORS COPYING COPYING.LIB NEWS README README.lib
%_bindir/ecm
%_man1dir/ecm.1.xz

%files -n libecm-devel
%_includedir/ecm.h
%_libdir/libecm.so

%files -n libecm%so_version
%_libdir/libecm.so.%{so_version}*

%changelog
* Thu Oct 28 2021 Leontiy Volodin <lvol@altlinux.org> 7.0.4-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
