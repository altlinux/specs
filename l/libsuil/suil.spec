# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ waf
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname suil
%global maj 0
Name:       libsuil
Version:    0.6.16
Release:    alt1_1
Summary:    A lightweight C library for loading and wrapping LV2 plugin UIs

Group:      System/Libraries
License:    MIT 
URL:        http://drobilla.net/software/suil/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz
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
Requires:   %{name} = %{version}-%{release}
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
    --docdir=%{_docdir}/%{oldname}-devel-%{version} \
    --docs 
./waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-0.so.*

%files
%doc AUTHORS NEWS README COPYING
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
%{_docdir}/%{oldname}-devel-%{version}
%{_mandir}/man3/%{oldname}.3*

%changelog
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

