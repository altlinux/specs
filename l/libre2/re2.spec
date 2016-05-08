# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname re2
%global longver 2016-04-01
%global shortver %(echo %{longver}|sed 's|-||g')

Name:           libre2
Version:        %{shortver}
Release:        alt1_2
Summary:        C++ fast alternative to backtracking RE engines
Group:          System/Libraries
License:        BSD
URL:            http://github.com/google/%{oldname}/
Source0:        https://github.com/google/re2/archive/%{longver}.tar.gz
Source44: import.info
Provides: re2 = %{version}-%{release}

%description
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g back references and generalized assertions).

%package        devel
Summary:        C++ header files and library symbolic links for %{oldname}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}
Provides: re2-devel = %{version}-%{release}

%description    devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{oldname}. If you would like to develop programs using %{oldname},
you will need to install %{oldname}-devel.

%prep
%setup -q -n %{oldname}-%{longver}

%build
# The -pthread flag issue has been submitted upstream:
# http://groups.google.com/forum/?fromgroups=#!topic/re2-dev/bkUDtO5l6Lo
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
CXXFLAGS="${CXXFLAGS:-%optflags} -pthread -std=c++11"
LDFLAGS="${LDFLAGS:-%__global_ldflags} -pthread"
make %{?_smp_mflags} CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" includedir=%{_includedir} libdir=%{_libdir}

%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir} libdir=%{_libdir}

# Suppress the static library
find $RPM_BUILD_ROOT -name 'lib%{oldname}.a' -exec rm -f {} \;

%check
make %{?_smp_mflags} shared-test

%files
%doc LICENSE
%doc AUTHORS CONTRIBUTORS README
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/%{oldname}.pc

%changelog
* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_5
- update to new release by fcimport

* Sun Dec 21 2014 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_3
- new version

