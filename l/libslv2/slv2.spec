# BEGIN SourceDeps(oneline):
BuildRequires: swig waf
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname slv2
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name slv2
%define version 0.6.6
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}

Name:			libslv2
Summary:		LV2 host library
Version:		0.6.6
Release:		alt4_19
License:		GPLv2+
Group:			System/Libraries
Source0:		http://download.drobilla.net/%{oldname}-%{version}.tar.bz2
# Remove dates from html doc files RHBZ#566345
Patch0:			%{oldname}-no-date-on-docs.patch
URL:			http://drobilla.net/software/slv2/

BuildRequires:		doxygen
BuildRequires:		lv2-devel
BuildRequires:		python
BuildRequires:		libredland-devel
BuildRequires:		libjack-devel
# To provide a clean upgrade path from PlanetCCRMA:
Obsoletes:		%{oldname}-examples < 0.6
Provides:		%{oldname}-examples = %{version}-%{release}
Source44: import.info
Provides: slv2 = %{version}-%{release}

%description
SLV2 is a library to make the use of LV2 plugins as simple as possible for 
applications. It is written in standard C using the Redland RDF toolkit. The 
Data (RDF) and code (shared library) functionality in SLV2 is strictly
separated so it is simple to control where each is used (e.g. it is possible
to discover/investigate plugins and related data without loading any shared 
libraries, avoiding the associated risks).

%package devel
Summary:	Development libraries and headers for %{oldname}
Group:		Development/C
Requires:	pkgconfig
Requires:	%{name}%{?_isa} = %{version}
Provides: slv2-devel = %{version}-%{release}

%description devel
SLV2 is a library to make the use of LV2 plugins as simple as possible for
applications. It is written in standard C using the Redland RDF toolkit. The
Data (RDF) and code (shared library) functionality in SLV2 is strictly
separated so it is simple to control where each is used (e.g. it is possible
to discover/investigate plugins and related data without loading any shared
libraries, avoiding the associated risks).

This package contains the headers and development libraries for SLV2.

%prep
%setup -n %{oldname}-%{version} -q 
%patch0 -p1 -b .nodates

# Fix possible multilib issues
sed -i 's|/lib/|/%{_lib}/|g' src/world.c
sed -i "s|/lib'|/%{_lib}'|" autowaf.py

# Remove unnecessary flags
sed -i 's|@REDLAND.*@||' slv2.pc.in
# Fix CFLAGS issue in slv2->redland->rasqal dependency chain
echo "Requires.private: redland" >> slv2.pc.in

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./waf configure --prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--htmldir=%{_docdir}/%{oldname} \
	--build-docs
./waf build -v %{?_smp_mflags}

# Workaround the doxygen bug
rm -f build/default/doc/man/man3/_*

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}.so*
install -pm 644 AUTHORS ChangeLog COPYING README %{buildroot}%{_docdir}/%{oldname}

%files
%dir %{_docdir}/%{oldname}
%{_docdir}/%{oldname}/AUTHORS
%{_docdir}/%{oldname}/ChangeLog
%{_docdir}/%{oldname}/COPYING
%{_docdir}/%{oldname}/README
%{_bindir}/lv2*
%{_libdir}/lib%{oldname}.so.*
%{_mandir}/man1/*

%files devel
%{_docdir}/%{oldname}/*
%exclude %{_docdir}/%{oldname}/AUTHORS
%exclude %{_docdir}/%{oldname}/ChangeLog
%exclude %{_docdir}/%{oldname}/COPYING
%exclude %{_docdir}/%{oldname}/README
%{_includedir}/%{oldname}/
%{_libdir}/pkgconfig/%{oldname}.pc
%{_libdir}/lib%{oldname}.so
%{_mandir}/man3/%{oldname}*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_18
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_15
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_13
- update to new release by fcimport

* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt4_12
- fixed build && accepted for maintainance

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt3.1
- NMU: rebuild with new lv2

* Thu Sep 08 2011 Egor Glukhov <kaman@altlinux.org> 0.6.6-alt3
- Fixed build

* Tue Nov 16 2010 Egor Glukhov <kaman@altlinux.org> 0.6.6-alt2
- Fixed BuildRequires

* Thu Jul 15 2010 Egor Glukhov <kaman@altlinux.org> 0.6.6-alt1
- initial build for Sisyphus
