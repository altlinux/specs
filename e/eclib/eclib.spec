%define with_allprogs 0
%define lname libec
%define soname 10

Name: eclib
Version: 20230424
Release: alt2
Summary: Tools for create the elliptic curve database
Group: Sciences/Mathematics
License: GPL-2.0+
Url: http://homepages.warwick.ac.uk/~masgaj/mwrank/

Source: https://github.com/JohnCremona/eclib/releases/download/%version/%name-%version.tar.bz2
Patch1: ax_boost_base-loongarch64.patch

BuildRequires: boost-program_options-devel
BuildRequires: libflint2-devel
BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: libntl-devel
BuildRequires: pari-devel

%description
John Cremona's programs for enumerating and computing with elliptic
curves defined over the rational numbers.

%package -n %lname%soname
Summary: Library for Computations on elliptic curves
Group: System/Libraries

%description -n %lname%soname
Library for Computations on Elliptic Curves.

%package devel
Summary: Development Files for %name
Group: Development/C++

%description devel
Development libraries and headers for %name.

%package tools
Summary: %summary
Group: Sciences/Mathematics

%description tools
John Cremona's programs for enumerating and computing with elliptic
curves defined over the rational numbers.

%prep
%setup
%patch1 -p1

%build
# FLINT_LEVEL 2 assumes that the C int type == half the width of a limb_t.
# This is only true on 64 bit platforms.
# %%ifnarch armh i586
#   export FLINT_LEVEL=2
# %%endif

export CPPFLAGS="-I %_includedir/flint"
# %%ifarch %%ix86
# Excess precision leads to test failures
# export CFLAGS="%%build_cflags -ffloat-store"
# export CXXFLAGS="$CFLAGS"
# %%endif
%autoreconf
%configure \
        --disable-static \
        --enable-shared \
        --with-flint \
        --with-boost \
%if %with_allprogs
        --enable-allprogs
%else
        --disable-allprogs
%endif

# Get rid of undesirable hardcoded rpaths.
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -i libtool

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la
%if !%with_allprogs
rm %buildroot%_docdir/%name/{g0n,howto,progs}.txt
%endif
# Packed in %%doc.
rm -f %buildroot%_docdir/%name/mwrank/mwrank.*

%check
make check LD_LIBRARY_PATH=%buildroot%_libdir

%files -n %lname%soname
%_libdir/%lname.so.%{soname}*

%files devel
%doc doc/g0n.txt
%_includedir/%name/
%_libdir/%lname.so
%_pkgconfigdir/%name.pc

%files tools
%doc AUTHORS NEWS README doc/mwrank COPYING
%if %with_allprogs
%_bindir/*
%else
%_bindir/mwrank
%endif
%_man1dir/mwrank.1*

%changelog
* Sun Nov 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20230424-alt2
- NMU: fixed FTBFS on LoongArch.

* Thu Apr 27 2023 Leontiy Volodin <lvol@altlinux.org> 20230424-alt1
- New version.

* Wed Oct 19 2022 Leontiy Volodin <lvol@altlinux.org> 20221012-alt1
- New version.

* Wed Jun 22 2022 Leontiy Volodin <lvol@altlinux.org> 20220621-alt1
- New version.
- Upstream:
  + fix saturation for non-reduced models and some refactoring.
  + upped library version.

* Tue Jun 21 2022 Leontiy Volodin <lvol@altlinux.org> 20220620-alt1
- New version.
- Upstream:
  + fix sign bug in quartic minimisation found by Bill Allombert.
  + fix possibly unreduced pari output of p2points.
  + fix saturation bug where Tamagawa primes were not always tested.

* Mon Nov 08 2021 Leontiy Volodin <lvol@altlinux.org> 20210625-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
