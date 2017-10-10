# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: waf
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname serd
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global maj 0

Name:           libserd
Version:        0.28.0
Release:        alt1_2
Summary:        A lightweight C library for RDF syntax

License:        ISC
URL:            http://drobilla.net/software/serd/
Source0:        http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  python
BuildRequires:  gcc-common
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
Group: Development/Other
Summary:        Development libraries and headers for %{oldname}
Requires:       %{name} = %{version}-%{release}
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
export LDFLAGS="%{__global_ldflags}"
./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir} \
    --docdir=%{_docdir} \
    --test \
    --docs 
./waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-%{maj}.so.*
# Move devel docs to the right directory
install -d %{buildroot}%{_docdir}/%{oldname}/%{oldname}-%{maj}
mv %{buildroot}%{_docdir}/%{oldname}-%{maj}/html %{buildroot}%{_docdir}/%{oldname}/%{oldname}-%{maj}/html

%files
%doc COPYING
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

