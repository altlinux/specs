# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name lv2
%define version 1.6.0
%global debug_package %{nil}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           lv2
Version:        1.6.0
Release:        alt1_2
Summary:        Audio Plugin Standard
Group:          System/Libraries

# lv2specgen template.html is CC-AT-SA
License:        ISC
URL:            http://lv2plug.in
Source:         http://lv2plug.in/spec/lv2-%{version}.tar.bz2

BuildRequires:  doxygen graphviz python-module-rdflib
# TODO: it complains about missing this, 
# (Error importing pygments, syntax highlighting disabled)
# but the syntax-highlighting in the generated docs looks strange
#BuildRequires: python-pygments

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
Summary:        API for the LV2 Audio Plugin Standard
Group:          Development/C

Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       lv2core-devel = 6.0-4
Obsoletes:      lv2core-devel < 6.0-4
Provides:       lv2-ui-devel = 2.4-5
Obsoletes:      lv2-ui-devel < 2.4-5

%description    devel
lv2-devel contains the lv2.h header file and headers for all of the
LV@ specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%package        doc
Summary:        Documentation for the LV2 Audio Plugin Standard
Group:          Documentation
BuildArch:      noarch
Obsoletes:      %{name}-docs < 1.6.0-2
Provides:       %{name}-docs = %{version}-%{release}

%description    doc
Documentation for the LV2 plugin API.

%prep
%setup -q

%build
./waf configure -vv --prefix=%{_prefix} --libdir=%{_libdir} --debug \
  --docs --docdir=%{_pkgdocdir} --no-plugins
./waf -vv %{?_smp_mflags}

%install
DESTDIR=%buildroot ./waf -vv install
mv %{buildroot}%{_pkgdocdir}/%{name}/lv2plug.in/* %{buildroot}%{_pkgdocdir}
find %{buildroot}%{_pkgdocdir} -type d -empty | xargs rmdir
for f in COPYING NEWS README ; do
    install -p -m0644 $f %{buildroot}%{_pkgdocdir}
done

%files
# don't include doc files via %%doc here (bz 913540)
%dir %{_pkgdocdir}
%{_pkgdocdir}/COPYING
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README
%{_libdir}/%{name}/
%exclude %{_libdir}/%{name}/*/*.[ch]

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/%{name}/*/*.[hc]
%{_libdir}/pkgconfig/lv2core.pc
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_pkgdocdir}/

%changelog
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

