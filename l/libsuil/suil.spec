Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
%define oldname suil
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name suil
%define version 0.10.8
%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:       libsuil
Version:    0.10.8
Release:    alt1_3
Summary:    A lightweight C library for loading and wrapping LV2 plugin UIs

License:    MIT 
URL:        http://drobilla.net/software/suil/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2


BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
# https://fedoraproject.org/wiki/Packaging:Python#Dependencies
BuildRequires:  python3
BuildRequires:  lv2-devel >= 1.16.0
# we need to track changess to these toolkits manually due to the 
# requires filtering below
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel
BuildRequires:  gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core) >= 5.1.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.1.0

# Lets not necessarily pull in toolkits dependancies. They will be provided by
# the host and or the plugin
%define __requires_exclude ^lib.*$
Source44: import.info

%description
%{oldname} makes it possible to load a UI of any toolkit in a host using any other 
toolkit (assuming the toolkits are both supported by %{oldname}). Hosts do not need
to build against or link to foreign toolkit libraries to use UIs written with 
that toolkit (%{oldname} performs its magic at runtime using dynamically 
loaded modules). 

%package devel
Group: Development/Other
Summary:    Development libraries and headers for %{oldname}
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q

# Don't run ldconfig
sed -i -e "s|bld.add_post_fun(autowaf.run_ldconfig)||" wscript

%build

/usr/bin/python3 waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --docdir=%{_docdir}/%{oldname} \
    --no-cocoa \
    --docs 
/usr/bin/python3 waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} /usr/bin/python3 waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-0.so.*
install -pm 644 AUTHORS COPYING NEWS README.md %{buildroot}%{_docdir}/%{oldname}

%files
%{_docdir}/%{oldname}
%exclude %{_docdir}/%{oldname}/%{oldname}-%{maj}
%exclude %{_docdir}/%{oldname}/COPYING
%doc --no-dereference COPYING
%dir %{_libdir}/suil-%{maj}
%{_libdir}/lib%{oldname}-*.so.%{maj}*
%{_libdir}/suil-%{maj}/libsuil_x11_in_gtk2.so
%{_libdir}/suil-%{maj}/libsuil_gtk2_in_qt5.so
%{_libdir}/suil-%{maj}/libsuil_x11_in_qt5.so
%{_libdir}/suil-%{maj}/libsuil_qt5_in_gtk2.so
%{_libdir}/suil-%{maj}/libsuil_x11.so
%{_libdir}/suil-%{maj}/libsuil_x11_in_gtk3.so
%{_libdir}/suil-%{maj}/libsuil_qt5_in_gtk3.so

%files devel
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
%{_docdir}/%{oldname}/%{oldname}-%{maj}
%{_mandir}/man3/%{oldname}.3*

%changelog
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

