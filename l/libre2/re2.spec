# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ swig
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname re2
Name:           libre2
Version:        20131024
Release:        alt1_3
Summary:        C++ fast alternative to backtracking RE engines
Group:          System/Libraries
License:        BSD
URL:            http://code.google.com/p/%{oldname}/
Source0:        http://re2.googlecode.com/files/%{oldname}-%{version}.tgz
Patch0:		re2-symbols-fix.patch
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
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides: re2-devel = %{version}-%{release}

%description    devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{oldname}. If you would like to develop programs using %{oldname},
you will need to install %{oldname}-devel.


%prep
%setup -q -n %{oldname}
%patch0 -p1 -b .fix

%build
# The -pthread flag issue has been submitted upstream:
# http://groups.google.com/forum/?fromgroups=#!topic/re2-dev/bkUDtO5l6Lo
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
CXXFLAGS="${CXXFLAGS:-%optflags} -pthread"
LDFLAGS="${LDFLAGS:-%__global_ldflags} -pthread"
make %{?_smp_mflags} CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" includedir=%{_includedir} libdir=%{_libdir}

%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir} libdir=%{_libdir}

# Suppress the static library
find $RPM_BUILD_ROOT -name 'lib%{oldname}.a' -exec rm -f {} \;

%check
make %{?_smp_mflags} shared-test

%files
%doc AUTHORS CONTRIBUTORS LICENSE README
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so

%changelog
* Sun Dec 21 2014 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_3
- new version

