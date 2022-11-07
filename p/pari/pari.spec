Name: pari
%define sover 8
%define lname libpari-gmp-tls%sover
Version: 2.15.1
Release: alt1
Summary: Computer Algebra System for computations in Number Theory
License: GPL-2.0-only
Group: Sciences/Mathematics
Url: https://pari.math.u-bordeaux.fr/
#Git-Clone:	https://pari.math.u-bordeaux.fr/git/pari.git
#Git-Web:	https://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi

Source: https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%version.tar.gz
Patch1: pari-nodate.diff
BuildRequires: libfltk-devel
BuildRequires: libgmp-devel
BuildRequires: libX11-devel
BuildRequires: libreadline-devel
BuildRequires: xorg-proto-devel
BuildRequires: texlive texlive-dist

%description
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%package gp
Summary: Frontend to the PARI Computer Algebra System
Group: Sciences/Mathematics

%description gp
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%package -n %lname
Summary: Computer Algebra System library for fast computations in Number Theory
# This is used by the data packages to avoid having a too-old version of libpari:
Group: System/Libraries
Provides: libpari-gmp = %version

%description -n %lname
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%package devel
Summary: Development files for the PARI CAS
Group: Development/Other
Requires: %lname = %version

%description devel
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%prep
%setup
# Get rid of undesirable hardcoded rpaths.
sed -i "s|runpathprefix='.*'|runpathprefix=''|" \
  config/get_ld

%build
./Configure --prefix="%prefix" \
  --bindir="%_bindir" --includedir="%_includedir" \
  --libdir="%_libdir" \
  --sysdatadir="%_libdir" --datadir="%_datadir/%name" \
  --mt=pthread
%make_build all \
  CFLAGS="%optflags -fno-strict-aliasing" \
  STRIP=true

%install
%makeinstall_std

%files gp
%_bindir/*
%_datadir/%name
%_libdir/%name.cfg
%_mandir/man*/*

%files -n %lname
%doc COPYING
%_libdir/libpari-gmp-tls.so.%version
%_libdir/libpari-gmp-tls.so.%sover

%files devel
%doc examples/
%doc CHANGES CHANGES-* NEW README
%_includedir/pari/
%_libdir/libpari.so

%changelog
* Mon Nov 07 2022 Leontiy Volodin <lvol@altlinux.org> 2.15.1-alt1
- New version (2.15.1).

* Tue Oct 25 2022 Leontiy Volodin <lvol@altlinux.org> 2.15.0-alt1
- New version (2.15.0).

* Thu Apr 07 2022 Leontiy Volodin <lvol@altlinux.org> 2.13.4-alt1
- New version (2.13.4) with rpmgs script.

* Tue Oct 26 2021 Leontiy Volodin <lvol@altlinux.org> 2.13.3-alt1
- New version (2.13.3) with rpmgs script.

* Fri Jul 02 2021 Leontiy Volodin <lvol@altlinux.org> 2.13.2-alt1
- New version (2.13.2) with rpmgs script.

* Fri Jun 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.13.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
