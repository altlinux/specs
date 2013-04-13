# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
%define oldname slv2
Name:			libslv2
Summary:		LV2 host library
Version:		0.6.6
Release:		alt4_12
License:		GPLv2+
Group:			System/Libraries
Source0:		http://download.drobilla.net/%{oldname}-%{version}.tar.bz2
# Remove dates from html doc files RHBZ#566345
Patch0:			%{oldname}-no-date-on-docs.patch
URL:			http://drobilla.net/software/slv2/

BuildRequires:		doxygen
BuildRequires:		lv2-devel
BuildRequires:		libredland-devel
BuildRequires:		libjack-devel
# To provide a clean upgrade path from PlanetCCRMA:
Obsoletes:		%{oldname}-examples < 0.6
Provides:		%{oldname}-examples = %{version}-%{release}
Source44: import.info

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
Requires:	%{name}%{?_isa} = %{version}-%{release}

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
	--htmldir=%{_docdir}/%{oldname}-devel-%{version} \
	--build-docs
./waf build -v %{?_smp_mflags}

# Workaround the doxygen bug
rm -f build/default/doc/man/man3/_*

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}.so*

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/lv2*
%{_libdir}/lib%{oldname}.so.*
%{_mandir}/man1/*

%files devel
%{_docdir}/%{oldname}-devel-%{version}
%{_includedir}/%{oldname}/
%{_libdir}/pkgconfig/%{oldname}.pc
%{_libdir}/lib%{oldname}.so
%{_mandir}/man3/%{oldname}*

%changelog
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
