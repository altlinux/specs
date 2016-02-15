# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname serd
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name serd
%define version 0.20.0
%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:           libserd
Version:        0.20.0
Release:        alt1_3
Summary:        A lightweight C library for RDF syntax

Group:          System/Libraries
License:        ISC
URL:            http://drobilla.net/software/serd/
Source0:        http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  glib2-devel
BuildRequires:  python
Source44: import.info
Provides: serd = %{version}-%{release}

%description
%{oldname} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

Serd is not intended to be a swiss-army knife of RDF syntax, but rather is 
suited to resource limited or performance critical applications (e.g. 
converting many gigabytes of NTriples to Turtle), or situations where a 
simple reader/writer with minimal dependencies is ideal (e.g. in LV2 
implementations or embedded applications).is a library to make the use of 
LV2 plugins as simple as possible for applications. 

%package devel
Summary:        Development libraries and headers for %{oldname}
Group:          Development/C
Requires:       %{name} = %{version}
Provides: serd-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
# we'll run ldconfig
sed -i -e 's|bld.add_post_fun(autowaf.run_ldconfig)||' wscript

%build
export CFLAGS="%{optflags}"
./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir} \
    --docdir=%{_docdir}/%{oldname} \
    --test \
    --docs 
./waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-%{maj}.so.*
install -pm 644 AUTHORS COPYING NEWS README %{buildroot}%{_docdir}/%{oldname}

%files
%dir %{_docdir}/%{oldname}/
%{_docdir}/%{oldname}/AUTHORS
%{_docdir}/%{oldname}/COPYING
%{_docdir}/%{oldname}/NEWS
%{_docdir}/%{oldname}/README
%{_libdir}/lib%{oldname}-%{maj}.so.*
%{_bindir}/serdi
%{_mandir}/man1/serdi.1*

%files devel
%{_libdir}/lib%{oldname}-%{maj}*.so
%{_libdir}/pkgconfig/%{oldname}*.pc
%{_includedir}/%{oldname}-%{maj}/
%{_docdir}/%{oldname}/%{oldname}-%{maj}/
%{_mandir}/man3/*.3*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.2-alt1_4
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.2-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.18.2-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.18.2-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt1_2
- fc import

