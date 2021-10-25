%def_enable static

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%global blaslib openblas
%define soname 0

Name: iml
Version: 1.0.5
Release: alt3
Summary: Finds solutions to systems of linear equations over integers
Group: Engineering
License: BSD-3-Clause
Url: https://cs.uwaterloo.ca/~astorjoh/iml.html

Source: https://cs.uwaterloo.ca/~astorjoh/%name-%version.tar.bz2
Source44: import.info

BuildRequires: gcc
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: libopenblas-devel

%description
IML provides efficient routines to compute exact solutions to dense
systems of linear equations over the integers.  The following
functionality is provided:
- Nonsingular rational system solving.
- Compute the right nullspace of an integer matrix.
- Certified linear system solving.

%package -n lib%name%soname
Group: Engineering
Summary: %summary
Provides: %name = %version-%release

%description -n lib%name%soname
IML provides efficient routines to compute exact solutions to dense
systems of linear equations over the integers.  The following
functionality is provided:
- Nonsingular rational system solving.
- Compute the right nullspace of an integer matrix.
- Certified linear system solving.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for %name
Provides: %name-devel = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/C
Summary: Static library for %name
Provides: %name-devel-static = %version-%release

%description -n lib%name-devel-static
The %name-static package contains a static library for %name.
%endif

%prep
%setup

%build
%configure --enable-shared --with-cblas="-lopenblas" \
  --with-cblas-include=%_includedir/openblas

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la
rm -fr %buildroot%_datadir/%name
%if_disabled static
rm -f %buildroot%_libdir/lib%name.a
%endif

%check
export LD_LIBRARY_PATH=$PWD/src/.libs
make check

%files -n lib%name%soname
%doc AUTHORS README
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc doc/liblink doc/libroutines examples
%_includedir/*
%_libdir/lib%name.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Mon Oct 25 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt3
- Initial build for ALT Sisyphus (ported from autoimports).
- Built as require for sagemath.

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt2_16
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_15
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_15
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_12
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_11
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_10
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_9
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_5
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3
- initial fc import

