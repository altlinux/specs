# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname serd
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global maj 0

Name:           libserd
Version:        0.30.2
Release:        alt1_1
Summary:        A lightweight C library for RDF syntax

License:        ISC
URL:            http://drobilla.net/software/serd/
Source0:        http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  python3
BuildRequires:  gcc
Source44: import.info
Provides: serd = %{version}-%{release}

%description
%{oldname} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle, TRiG, NTriples, and NQuads.

Serd is suitable for performance-critical or resource-limited applications,
such as serialising very large data sets, network protocols, or embedded
systems that require minimal dependencies and lightweight deployment.

%package devel
Group: Development/Other
Summary:        Development libraries and headers for %{oldname}
Requires:       %{name} = %{version}-%{release}
Provides: serd-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle, TRiG, NTriples, and NQuads.

This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
# we'll run ldconfig, well not any more, see
# https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
sed -i -e 's|bld.add_post_fun(autowaf.run_ldconfig)||' wscript

%build

python3 waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir} \
    --docdir=%{_docdir} \
    --test \
    --docs 
python3 waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} python3 waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-%{maj}.so.*
# Move devel docs to the right directory
install -d %{buildroot}%{_docdir}/%{oldname}/%{oldname}-%{maj}
mv %{buildroot}%{_docdir}/%{oldname}-%{maj}/html %{buildroot}%{_docdir}/%{oldname}/%{oldname}-%{maj}/html

%files
%doc --no-dereference COPYING
%doc AUTHORS NEWS README.md
%doc %{_mandir}/man1/serdi.1*
%{_libdir}/lib%{oldname}-%{maj}.so.*
%{_bindir}/serdi

%files devel
%doc %{_mandir}/man3/serd.3*
%doc %{_docdir}/%{oldname}/%{oldname}-%{maj}/
%{_libdir}/lib%{oldname}-%{maj}*.so
%{_libdir}/pkgconfig/%{oldname}*.pc
%{_includedir}/%{oldname}-%{maj}/

%changelog
* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.30.2-alt1_1
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.30.0-alt1_1
- update to new release by fcimport

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.28.0-alt1_2
- rebuild with libaltascpp

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.22.0-alt1_2
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.22.0-alt1_1
- update to new release by fcimport

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

