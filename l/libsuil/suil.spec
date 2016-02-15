# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ waf
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname suil
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name suil
%define version 0.8.2
%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:       libsuil
Version:    0.8.2
Release:    alt1_4
Summary:    A lightweight C library for loading and wrapping LV2 plugin UIs

Group:      System/Libraries
License:    MIT 
URL:        http://drobilla.net/software/suil/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python
BuildRequires:  lv2-devel
# we need to track changess to these toolkits manually due to the 
# requires filtering below
BuildRequires:  gtk2-devel
BuildRequires:  qt4-devel

# lets not unecessarily pull in toolkits dependancies. They will be provided by 
# the host and or the plugin
%filter_from_requires /.*libatk.*/d
%filter_from_requires /.*libcairo.*/d
%filter_from_requires /.*libfont.*/d
%filter_from_requires /.*libfree.*/d
%filter_from_requires /.*libg.*/d
%filter_from_requires /.*libpango.*/d
%filter_from_requires /.*libQt.*/d
%filter_from_requires /.*libX*/d

Source44: import.info
Provides: suil = %{version}-%{release}

%description
%{oldname} makes it possible to load a UI of any toolkit in a host using any other 
toolkit (assuming the toolkits are both supported by %{oldname}). Hosts do not need
to build against or link to foreign toolkit libraries to use UIs written with 
that toolkit (%{oldname} performs its magic at runtime using dynamically 
loaded modules). 

%package devel
Summary:    Development libraries and headers for %{oldname}
Group:      Development/C
Requires:   %{name} = %{version}
Provides: suil-devel = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
# we'll run ldconfig, and add our optflags 
sed -i -e "s|bld.add_post_fun(autowaf.run_ldconfig)||" wscript

%build
export CXXFLAGS="%{optflags}"
./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --docdir=%{_docdir}/%{oldname} \
    --docs 
./waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-0.so.*
install -pm 644 AUTHORS COPYING NEWS README %{buildroot}%{_docdir}/%{oldname}

%files
%{_docdir}/%{oldname}
%exclude %{_docdir}/%{oldname}/%{oldname}-%{maj}
%dir %{_libdir}/suil-%{maj}
%{_libdir}/lib%{oldname}-*.so.*
%{_libdir}/suil-%{maj}/libsuil_gtk2_in_qt4.so
%{_libdir}/suil-%{maj}/libsuil_qt4_in_gtk2.so
%{_libdir}/suil-%{maj}/libsuil_x11_in_qt4.so
%{_libdir}/suil-%{maj}/libsuil_x11_in_gtk2.so

%files devel
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
%{_docdir}/%{oldname}/%{oldname}-%{maj}
%{_mandir}/man3/%{oldname}.3*

%changelog
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

