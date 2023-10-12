Group: System/Libraries
%add_optflags %optflags_shared
%define oldname suil
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name suil
%define version 0.10.18
%define autorelease 1

%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:       libsuil
Version:    0.10.18
Release:    alt1_1
Summary:    A lightweight C library for loading and wrapping LV2 plugin UIs

License:    ISC
URL:        https://drobilla.net/software/%{oldname}
Source0:    https://download.drobilla.net/%{oldname}-%{version}.tar.xz
Patch0:     suil-0.10.18-no-gtk-quartz.patch

BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  lv2-devel >= 1.18.3
BuildRequires:  meson >= 0.56
# We need to track changes to these toolkits manually due to the
# required filtering below.
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel
BuildRequires:  gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core) >= 5.1.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.1.0
#BuildRequires:  python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
#BuildRequires:  python3-module-sphinx_lv2_theme

# Lets not necessarily pull in toolkits dependencies. They will be provided by
# the host and/or the plugin.
%define __requires_exclude ^lib.*$
Source44: import.info
Provides: suil = %{version}-%{release}

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
Provides: suil-devel = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1


%build
%meson
%meson_build

%install
%meson_install
#install -d "%{buildroot}%{_docdir}/%{oldname}"
#mv -f "%{buildroot}%{_docdir}/%{oldname}-%{maj}" "%{buildroot}%{_docdir}/%{oldname}/"

%files
%doc AUTHORS NEWS README.md
#exclude %{_docdir}/%{oldname}/%{oldname}-%{maj}
%doc --no-dereference COPYING
%dir %{_libdir}/%{oldname}-%{maj}
%{_libdir}/lib%{oldname}-*.so.%{maj}*
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_x11_in_gtk2.so
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_gtk2_in_qt5.so
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_x11_in_qt5.so
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_qt5_in_gtk2.so
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_x11.so
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_x11_in_gtk3.so
%{_libdir}/%{oldname}-%{maj}/lib%{oldname}_qt5_in_gtk3.so

%files devel
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
#%{_docdir}/%{oldname}/%{oldname}-%{maj}

%changelog
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

