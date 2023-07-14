# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname sratom
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name sratom
%define version 0.6.6
%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:       libsratom
Version:    0.6.6
Release:    alt2_1
Summary:    A C library for serializing LV2 plugins

License:    MIT
URL:        http://drobilla.net/software/%{oldname}/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2
# Patch from upstream
Patch0:     %{oldname}-remove-deprecated-doxygen.patch
# Avoid bogus test failure
Patch1: 0001-Fixed-sratom_test-false-negative.patch

BuildRequires:  python3
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  libsord-devel >= 0.14.0
BuildRequires:  libserd-devel >= 0.30.0
BuildRequires:  lv2-devel >= 1.10.0
BuildRequires:  gcc
Source44: import.info
Provides: sratom = %{version}-%{release}

%description
%{oldname} is a new C library for serializing LV2 atoms to/from Turtle. It is 
intended to be a full serialization solution for LV2 atoms, allowing 
implementations to serialize binary atoms to strings and read them back again. 
This is particularly useful for saving plugin state, or implementing plugin 
control with network transparency.

%package devel
Group: Development/Other
Summary:    Development libraries and headers for %{oldname}
Requires:   %{name} = %{version}-%{release}
Provides: sratom-devel = %{version}-%{release}

%description devel
%{oldname} is a C library for serializing LV2 atoms to/from Turtle. It is 
intended to be a full serialization solution for LV2 atoms, allowing 
implementations to serialize binary atoms to strings and read them back again. 
This is particularly useful for saving plugin state, or implementing plugin 
control with network transparency.

This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1
%patch1 -p1


# for packagers sake, build the tests with debug symbols
sed -i -e "s| '-ftest-coverage'\]|\
 '-ftest-coverage'\] + '%{optflags}'.split(' ')|" wscript

%build

python3 waf configure -v \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir} \
    --docdir=%{_docdir}/%{oldname} \
    --test \
    --docs 
python3 waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} python3 waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-0.so.*
install -pm 644 COPYING NEWS README.md %{buildroot}%{_docdir}/%{oldname}

%check
./build/sratom_test

%files
%{_docdir}/%{oldname}
%exclude %{_docdir}/%{oldname}/%{oldname}-%{maj}/
%exclude %{_docdir}/%{oldname}/COPYING
%doc --no-dereference COPYING
%{_libdir}/lib%{oldname}-%{maj}.so.*

%files devel
%{_docdir}/%{oldname}/%{oldname}-%{maj}/
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
%{_mandir}/man3/*

%changelog
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

