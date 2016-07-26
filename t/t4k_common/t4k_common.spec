# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libSDL_ttf-devel
# END SourceDeps(oneline)
Name: t4k_common
Version: 0.1.1
Release: alt2_14
URL: http://tux4kids.alioth.debian.org/
Summary: Library for Tux4Kids applications
License: GPLv3+
Source0: https://alioth.debian.org/frs/download.php/3540/%{name}-%{version}.tar.gz
Patch0: t4k_common-0.1.1-libpng15.patch
Group: System/Libraries
BuildRequires: libSDL-devel libSDL_mixer-devel libSDL_image-devel
BuildRequires: libSDL_pango-devel libSDL_net-devel librsvg-devel librsvg-gir-devel libcairo-devel
BuildRequires: libpng-devel libxml2-devel doxygen
Provides: bundled(liblinebreak)
Source44: import.info

%package devel
Summary: Development files for the Tux4Kids library
Group: Development/C++
Requires: %{name}%{?_isa} = %{version}
Requires: pkg-config

%description
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

%description devel
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

These are the development files.

%prep
%setup -q

%patch0 -p0

%build
%configure
make %{?_smp_mflags}
doxygen
rm -f doxygen/html/installdox

%install
INSTALL='install -p' make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_includedir}/t4k_scandir.h
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

%files
%doc COPYING README
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%doc doxygen/html/
%{_libdir}/lib%{name}.so
%{_includedir}/t4k*.h
%{_libdir}/pkgconfig/t4k_common.pc

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_9
- update to new release by fcimport

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2_8.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_8
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_7
- converted by srpmconvert script

* Tue Jan 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_2
- dropped hook

* Fri Oct 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2
- use fedora versions

* Tue Aug 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_1.8
- initial release by fcimport

