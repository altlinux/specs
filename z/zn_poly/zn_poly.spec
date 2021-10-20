%define soname 0

Name: zn_poly
Version: 0.9.2
Release: alt1
Summary: C library for polynomial arithmetic

# All files released under "GPLv2 or GPLv3", except:
# - include/wide_arith.h is part LGPLv2+ and part GPLv2+
# - include/profiler.h is part GPLv2+
License: (GPL-2.0 or GPL-3.0) and GPL-2.0+ and LGPL-2.1+
Group: Sciences/Mathematics
Url: https://gitlab.com/sagemath/%name

Source: https://gitlab.com/sagemath/%name/archive/%version/%name-%version.tar.bz2

BuildRequires: gcc libgmp-devel python3

%description
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
any modulus that fits into an unsigned long.

%package -n lib%name%soname
Summary: %summary
Group: Sciences/Mathematics

%description -n lib%name%soname
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
any modulus that fits into an unsigned long.

%package -n lib%name-devel
Summary: Development files for %name
Group: Sciences/Mathematics

%description -n lib%name-devel
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
any modulus that fits into an unsigned long.

This package contains the development files.

# %package -n lib%name-devel-static
# Summary: Development files for %name
# Group: Sciences/Mathematics
#
# %description -n lib%name-devel-static
# zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n is
# any modulus that fits into an unsigned long.
#
# This package contains the static library.

%prep
%setup

%__subst "s|typedef unsigned long  ulong;|\/\/typedef unsigned long  ulong;|g" include/zn_poly.h

%build
python3 makemakefile.py --cflags="%optflags -fPIC" --prefix=%prefix \
    --gmp-prefix=%prefix \
    --disable-tuning \
    > makefile

%make_build all libzn_poly.so libzn_poly-%version.so LDFLAGS="$RPM_LD_FLAGS"

%install
# install manually, because makefile does not honor DESTDIR
mkdir -p %buildroot%_includedir/zn_poly/
mkdir -p %buildroot%_libdir
cp -pv include/*.h %buildroot%_includedir/zn_poly/
# cp -pv libzn_poly.a %buildroot%_libdir
cp -pv libzn_poly-%version.so %buildroot%_libdir
ln -s libzn_poly-%version.so %buildroot%_libdir/libzn_poly-0.9.so
ln -s libzn_poly-0.9.so %buildroot%_libdir/libzn_poly.so

%check
make test LDFLAGS="$RPM_LD_FLAGS"
./test/test all

%files -n lib%name%soname
%doc COPYING gpl-?.0.txt
%doc demo/bernoulli/bernoulli.c doc/REFERENCES
%_libdir/libzn_poly-%version.so
%_libdir/libzn_poly-0.9.so

%files -n lib%name-devel
%_libdir/libzn_poly.so
%_includedir/zn_poly/

# %files -n lib%name-devel-static
# %_libdir/libzn_poly.a

%changelog
* Wed Oct 20 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
