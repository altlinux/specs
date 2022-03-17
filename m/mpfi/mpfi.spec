# BEGIN SourceDeps(oneline):
BuildRequires: texinfo
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define fontpkgname mpfi
%define soname 0

%def_enable static
%def_disable tests

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

Name: mpfi
Version: 1.5.4
Release: alt1

Summary: An interval arithmetic library based on MPFR

License: LGPL-2.1+
Group: Engineering
Url: http://perso.ens-lyon.fr/nathalie.revol/software.html

Source: https://perso.ens-lyon.fr/nathalie.revol/softwares/%name-%version.tar.bz2
Source44: import.info

BuildRequires: gcc
BuildRequires: libmpfr-devel
BuildRequires: libgmp-devel libgmpxx-devel

%description
MPFI is intended to be a portable library written in C for arbitrary
precision interval arithmetic with intervals represented using MPFR
reliable floating-point numbers. It is based on the GNU MP library and
on the MPFR library and is part of the latter. The purpose of an
arbitrary precision interval arithmetic is on the one hand to get
"guaranteed" results, thanks to interval computation, and on the other
hand to obtain accurate results, thanks to multiple precision
arithmetic. The MPFI library is built upon MPFR in order to benefit
from the correct roundings provided by MPFR. Further advantages of
using MPFR are its portability and compliance with the IEEE 754
standard for floating-point arithmetic.

%package -n lib%name%soname
Group: Engineering
Summary: %summary

%description -n lib%name%soname
MPFI is intended to be a portable library written in C for arbitrary
precision interval arithmetic with intervals represented using MPFR
reliable floating-point numbers. It is based on the GNU MP library and
on the MPFR library and is part of the latter. The purpose of an
arbitrary precision interval arithmetic is on the one hand to get
"guaranteed" results, thanks to interval computation, and on the other
hand to obtain accurate results, thanks to multiple precision
arithmetic. The MPFI library is built upon MPFR in order to benefit
from the correct roundings provided by MPFR. Further advantages of
using MPFR are its portability and compliance with the IEEE 754
standard for floating-point arithmetic.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for %name

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/C
Summary: Static library for %name

%description -n lib%name-devel-static
The %name-static package contains the static %name library.
%endif

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
rm -f %buildroot%_infodir/dir

# Remove libtool archives
rm -f %buildroot%_libdir/*.la

# Remove dir file in the info directory
rm -f %buildroot%_infodir/dir

%if_disabled static
rm -f %buildroot%_libdir/lib%name.a
%endif

# Package docs in %%doc
rm -rf %buildroot%_datadir/doc/mpfi/

%if_enabled tests
%check
make check
%endif

%files -n lib%name%soname
%doc AUTHORS NEWS TODO COPYING COPYING.LESSER
%_libdir/libmpfi.so.%{soname}*

%files -n lib%name-devel
%_includedir/mpfi.h
%_includedir/mpfi_io.h
%_infodir/%name.info*
%_libdir/libmpfi.so
%_pkgconfigdir/mpfi.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Thu Mar 17 2022 Leontiy Volodin <lvol@altlinux.org> 1.5.4-alt1
- New version (1.5.4) with rpmgs script.

* Wed Oct 20 2021 Leontiy Volodin <lvol@altlinux.org> 1.5.3-alt3
- Initial build for ALT Sisyphus.
- Built as require for sagemath.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.5.3-alt2_9
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.5.3-alt2_8
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt2_7
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_7
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_6
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_5
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_4
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_3
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_2
- update to new release by fcimport

* Fri Jun 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_12
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_10
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_9
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_8
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_7
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- initial fc import

