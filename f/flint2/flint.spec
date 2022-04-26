%define soname 16

Name: flint2
Version: 2.8.5
Release: alt1
Summary: Fast Library for Number Theory

# Flint itself is LGPLv2+.  The hmod_mat extension is GPLv2+.
License: LGPL-2.0+ and GPL-2.0+
Group: System/Libraries
Url: https://www.flintlib.org/

Source: %url/%name-%version.tar.gz

BuildPreReq: rpm-build-ninja
BuildRequires: gcc-c++ cmake libgmp-devel libgc-devel libmpfr-devel texlive-collection-basic libblas-devel
#BuildRequires: flexiblas-devel ntl-devel

%description
FLINT is a C library for doing number theory, written by William Hart
and David Harvey.

%package  -n lib%name-%soname
Summary: %summary
Group: System/Libraries

%description  -n lib%name-%soname
FLINT is a C library for doing number theory, written by William Hart
and David Harvey.

%package -n lib%name-devel
Summary: Development files for FLINT
Group: Development/Other

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake -GNinja
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

# Fix permissions
#chmod 0755 %%buildroot%%_libdir/libflint*.so.*

# Install CPimport.txt
#mkdir -p %%buildroot%%_datadir/flint
#cp -p qadic/CPimport.txt %%buildroot%%_datadir/flint

#%%ifnarch %%arm %%ix86
# Tests temporarily disabled on 32-bit builders.
# See https://github.com/wbhart/flint2/issues/786
#%%check
#export LD_LIBRARY_PATH=$PWD
#make check QUIET_CC= QUIET_CXX= QUIET_AR= \
#  LDFLAGS="%%build_ldflags" LIBDIR=%_lib
#%%endif

%files -n lib%name-%soname
%doc AUTHORS NEWS README LICENSE
%_libdir/libflint.so.%{soname}*
#%%_datadir/flint/

%files -n lib%name-devel
%_includedir/flint/
%_libdir/libflint.so

%changelog
* Tue Apr 26 2022 Leontiy Volodin <lvol@altlinux.org> 2.8.5-alt1
- New version (2.8.5).

* Fri Nov 19 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.4-alt1
- New version (2.8.4).

* Fri Nov 05 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.3-alt1
- New version (2.8.3).

* Tue Oct 19 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.2-alt1
- New version (2.8.2).

* Sat Oct 02 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.1-alt1
- New version (2.8.1).

* Wed Sep 29 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for libpynac.
