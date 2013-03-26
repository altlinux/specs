# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname sord
%global maj 0

Name:       libsord
Version:    0.10.4
Release:    alt1_3
Summary:    A lightweight Resource Description Framework (RDF) C library

Group:      System/Libraries
License:    ISC
URL:        http://drobilla.net/software/sord/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires: boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: glib2-devel
BuildRequires: serd-devel >= 0.14.0
Source44: import.info
Provides: sord = %{version}-%{release}

%description
%{oldname} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory. %{oldname} and parent library serd form 
a lightweight RDF tool-set for resource limited or performance critical 
applications.

%package devel
Summary:    Development libraries and headers for %{oldname}
Group:      Development/C
Requires:   %{name} = %{version}-%{release}
Provides: sord-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory.

This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
# we'll run ldconfig, and add our optflags 
sed -i -e "s|bld.add_post_fun(autowaf.run_ldconfig)||" \
       -e "s|cflags          = [ '-DSORD_INTERNAL' ]\
|cflags          = [ '-DSORD_INTERNAL' ] + '%optflags'.split(' ') |" wscript

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir} \
    --docdir=%{_docdir}/%{oldname}-devel-%{version} \
    --test \
    --docs 
./waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-%{maj}.so.*

%files
%doc AUTHORS NEWS README COPYING
%{_libdir}/lib%{oldname}-%{maj}.so.*
%{_bindir}/sordi
%{_bindir}/sord_validate
%{_mandir}/man1/sordi.1*

%files devel
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
%{_docdir}/%{oldname}-devel-%{version}
%{_mandir}/man1/%{oldname}*.1.*
%{_mandir}/man3/%{oldname}*.3.*

%changelog
* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.4-alt1_3
- fc import

