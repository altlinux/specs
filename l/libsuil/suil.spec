Name: libsuil
Version: 0.10.24
Release: alt1

Summary: A lightweight C library for loading and wrapping LV2 plugin UIs
License: ISC
Group: System/Libraries
Url: https://gitlab.com/lv2/suil

Source: %name-%version.tar

BuildRequires: meson
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-x11-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt6Widgets)

%package gtk2
Summary: suil gtk2 wrapper plugin
Group: System/Libraries
Requires: libsuil = %EVR

%package gtk3
Summary: suil gtk3 wrapper plugin
Group: System/Libraries
Requires: libsuil = %EVR

%package qt5
Summary: suil qt5 wrapper plugin
Group: System/Libraries
Requires: libsuil = %EVR

%package qt6
Summary: suil qt6 wrapper plugin
Group: System/Libraries
Requires: libsuil = %EVR

%package devel
Summary: Development libraries and headers for suil
Group: Development/C

%define desc\
suil makes it possible to load a UI of any toolkit in a host using any other\
toolkit (assuming the toolkits are both supported by suil). Hosts do not need\
to build against or link to foreign toolkit libraries to use UIs written with\
that toolkit suil performs its magic at runtime using dynamically loaded modules.

%description %desc

%description gtk2 %desc

%description gtk3 %desc

%description qt5 %desc

%description qt6 %desc

%description devel %desc
This package contains the headers and development libraries for suil.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS COPYING NEWS README.md
%dir %_libdir/suil-0
%_libdir/libsuil-0.so.*
%_libdir/suil-0/libsuil_x11.so

%files gtk2
%_libdir/suil-0/libsuil_x11_in_gtk2.so

%files gtk3
%_libdir/suil-0/libsuil_x11_in_gtk3.so

%files qt5
%_libdir/suil-0/libsuil_x11_in_qt5.so

%files qt6
%_libdir/suil-0/libsuil_x11_in_qt6.so

%files devel
%_libdir/libsuil-0.so
%_libdir/pkgconfig/suil-0.pc
%_includedir/suil-0

%changelog
* Fri Nov 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.24-alt1
- 0.10.24 released

* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 0.10.18-alt1_1
- update to new release by fcimport

* Thu Nov 11 2021 Igor Vlasenko <viy@altlinux.org> 0.10.8-alt1_3
- build w/o qt4 (closes: #41330)

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.8-alt1_1
- new version

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt1_2
- update

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1_3
- update to new release by fcimport

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_1
- new version

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_5
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_2
- update to new release by fcimport

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_1
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.16-alt1_2
- update to new release by fcimport

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.16-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.12-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.12-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.10-alt1_2
- fc import

