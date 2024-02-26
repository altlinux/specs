Name: libsratom
Version: 0.6.16
Release: alt1

Summary: A C library for serializing LV2 plugins
License: MIT
Group: System/Libraries
Url: https://github.com/lv2/sratom

Source: %name-%version-%release.tar

BuildRequires: meson
BuildRequires: pkgconfig(serd-0)
BuildRequires: pkgconfig(sord-0)
BuildRequires: pkgconfig(lv2)

%package devel
Summary: Development libraries and headers for sratom
Group: Development/C

%define desc\
sratom is a new C library for serializing LV2 atoms to/from Turtle. It is\
intended to be a full serialization solution for LV2 atoms, allowing\
implementations to serialize binary atoms to strings and read them back again.\
This is particularly useful for saving plugin state, or implementing plugin\
control with network transparency.

%description %desc

%description devel %desc
This package contains the headers and development libraries for sratom.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/libsratom-0.so.*

%files devel
%_includedir/sratom-0
%_libdir/libsratom-0.so
%_pkgconfigdir/sratom-0.pc

%changelog
* Mon Feb 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.16-alt1
- 0.6.16 released

* Fri Jul 14 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.6.6-alt2_1
- Avoid spurious test failure

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_1
- update to new release by fcimport

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_2
- update

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_3
- update to new release by fcimport

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.6-alt1_5
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.6-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.6-alt1_3
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.6-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- update to new release by fcimport

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_1
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_5
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_4
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_5
- fc import
