# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: waf
# END SourceDeps(oneline)
BuildRequires: gcc-c++
%add_optflags %optflags_shared
%define oldname lilv
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name lilv
%define version 0.16.0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}
%global maj 0

Name:       liblilv
Version:    0.16.0
Release:    alt1_3
Summary:    An LV2 Resource Description Framework Library

Group:      System/Libraries
License:    MIT
URL:        http://drobilla.net/software/lilv/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2
Patch1:     lilv-0.16.0-gcc.patch
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  sord-devel >= 0.12.0
BuildRequires:  sratom-devel >= 0.4.0
BuildRequires:  lv2-devel >= 1.0.0
BuildRequires:  python-devel
BuildRequires:  swig


Source44: import.info
Provides: lilv = %{version}-%{release}

%description
%{oldname} is a library to make the use of LV2 plugins as simple as possible 
for applications. Lilv is the successor to SLV2, rewritten to be significantly 
faster and have minimal dependencies. 

%package devel
Summary:    Development libraries and headers for %{oldname}
Group:      Development/C
Requires:   %{name} = %{version}-%{release}
Provides: lilv-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for Resource Description Syntax which 
supports reading and writing Turtle and NTriples.

This package contains the headers and development libraries for %{oldname}.

%package -n python-module-lilv
Summary:    Python bindings for %{oldname}
Group:      Development/Python
Requires:   %{name} = %{version}-%{release}

%description -n python-module-lilv 
%{oldname} is a lightweight C library for Resource Description Syntax which 
supports reading and writing Turtle and NTriples.

This package contains the python libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q 
%patch1 -p1 
# we'll run ld config
sed -i -e 's|bld.add_post_fun(autowaf.run_ldconfig)||' wscript
# for packagers sake, build the tests with debug symbols
sed -i -e "s|'-ftest-coverage'\]|\
 '-ftest-coverage' \] + '%{optflags}'.split(' ')|" wscript

%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
./waf configure -v --prefix=%{_prefix}\
 --libdir=%{_libdir} --configdir=%{_sysconfdir} --mandir=%{_mandir}\
 --docdir=%{_pkgdocdir}\
 --docs --test --dyn-manifest --bindings 
./waf -v build %{?_smp_mflags}

%install
./waf -v install --destdir=%{buildroot} 
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-0.so.*

%check
./build/test/lilv_test

%files
%doc AUTHORS NEWS README COPYING
%exclude %{_pkgdocdir}/%{oldname}-%{maj}/
%{_libdir}/lib%{oldname}-%{maj}.so.*
%{_bindir}/lilv-bench
%{_bindir}/lv2info
%{_bindir}/lv2ls
%{_bindir}/lv2bench
%dir %{_sysconfdir}/bash_completion.d/
%{_sysconfdir}/bash_completion.d/lilv
%{_mandir}/man1/*

%files devel
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
%{_pkgdocdir}/%{oldname}-%{maj}/
%{_mandir}/man3/*

%files -n python-module-lilv
%{python_sitelibdir_noarch}/%{oldname}.*
%{python_sitelibdir}/_%{oldname}.so

%changelog
* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.14.4-alt1_2
- fc import

