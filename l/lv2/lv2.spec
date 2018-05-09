Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: waf
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name lv2
%define version 1.14.0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           lv2
Version:        1.14.0
Release:        alt1_5
Summary:        Audio Plugin Standard

# lv2specgen template.html is CC-AT-SA
License:        ISC
URL:            http://lv2plug.in
Source:         http://lv2plug.in/spec/lv2-%{version}.tar.bz2

BuildRequires:  doxygen graphviz libgraphviz python-module-rdflib
BuildRequires:  libsndfile-devel
BuildRequires:  gcc
BuildRequires:  python-module-Pygments
BuildRequires:  python-devel

# this package replaces lv2core 
Provides:       lv2core = 6.0-4
Obsoletes:      lv2core < 6.0-4
Provides:       lv2-ui = 2.4-5
Obsoletes:      lv2-ui < 2.4-5
Source44: import.info

%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.  

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.

%package        devel
Group: Development/C
Summary:        API for the LV2 Audio Plugin Standard

Requires:       %{name} = %{version}-%{release}
Provides:       lv2core-devel = 6.0-4
Obsoletes:      lv2core-devel < 6.0-4
Provides:       lv2-ui-devel = 2.4-5
Obsoletes:      lv2-ui-devel < 2.4-5

%description    devel
lv2-devel contains the lv2.h header file and headers for all of the
LV2 specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%package        doc
Group: Documentation
Summary:        Documentation for the LV2 Audio Plugin Standard
BuildArch:      noarch
Obsoletes:      %{name}-docs < 1.6.0-2
Provides:       %{name}-docs = %{version}-%{release}

%description    doc
Documentation for the LV2 plugin API.

%package        example-plugins
Group: Sound
Summary:        Examples of the LV2 Audio Plugin Standard

%description    example-plugins
Example LV2 audio plugins

%prep
%setup -q
# Fix wrong interpreter in lv2specgen.py
sed -i '1s|^#!.*|#!%{__python}|' lv2specgen/lv2specgen.py

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
./waf configure -vv --prefix=%{_prefix} --libdir=%{_libdir} --debug \
  --docs --docdir=%{_docdir}/%{name} --lv2dir=%{_libdir}/lv2
./waf -vv %{?_smp_mflags}

%install
DESTDIR=%buildroot ./waf -vv install
mv %{buildroot}%{_docdir}/%{name}/%{name}/lv2plug.in/* %{buildroot}%{_docdir}/%{name}
find %{buildroot}%{_docdir}/%{name} -type d -empty | xargs rmdir
for f in COPYING NEWS README.md ; do
    install -p -m0644 $f %{buildroot}%{_docdir}/%{name}
done

%files
# don't include doc files via %%doc here (bz 913540)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README.md
%{_libdir}/%{name}/

%exclude %{_libdir}/%{name}/*/*.[ch]
%exclude %{_libdir}/%{name}/eg-*

%files devel
%{_bindir}/lv2specgen.py
%{_datadir}/lv2specgen
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/%{name}/*/*.[hc]
%{_libdir}/pkgconfig/lv2core.pc
%{_libdir}/pkgconfig/%{name}.pc

%exclude %{_libdir}/%{name}/eg-*

%files example-plugins
%{_libdir}/%{name}/eg-*

%files doc
%{_docdir}/%{name}/

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_5
- update to new release by fcimport

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- update to new release by fcimport

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- import

