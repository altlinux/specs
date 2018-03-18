# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/pandoc gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major 1
%define libname libipt%{major}
%define devname libipt-devel

Name: libipt
Version: 1.4.4
Release: alt1_2
Summary: Intel Processor Trace Decoder Library
Group:	 Development/Tools
License: BSD
URL: https://github.com/01org/processor-trace
Source0: https://github.com/01org/processor-trace/archive/v%{version}.tar.gz
BuildRequires: ccmake cmake ctest
ExclusiveArch: %{ix86} x86_64
Source44: import.info

%description
The Intel Processor Trace (Intel PT) Decoder Library is Intel's reference
implementation for decoding Intel PT.  It can be used as a standalone library
or it can be partially or fully integrated into your tool.


%package -n %devname
Group: Development/Tools
Summary: Header files and libraries for Intel Processor Trace Decoder Library
Requires: %{libname} = %{version}-%{release}
ExclusiveArch: %{ix86} x86_64
Provides: ipt-devel, libipt-devel

%description -n %devname
The %{name}-devel package contains the header files and libraries needed to
develop programs that use the Intel Processor Trace (Intel PT) Decoder Library.

%package -n %libname
Summary: Intel Processor Trace Decoder Library
Group:	Development/C
Requires: %{libname} = %{version}-%{release}
ExclusiveArch: %{ix86} x86_64
# temp cauldron fix:
Obsoletes: libipt0
Provides: libipt0

%description -n %libname
The Intel Processor Trace (Intel PT) Decoder Library is Intel's reference
implementation for decoding Intel PT.  It can be used as a standalone library
or it can be partially or fully integrated into your tool.

%prep
%setup -q -n processor-trace-%{version}

%build
# -DPTUNIT:BOOL=ON has no effect on ctest.
%{mageia_cmake} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPTUNIT:BOOL=OFF \
       -DFEATURE_THREADS:BOOL=ON \
       -DDEVBUILD:BOOL=ON \
       ..
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} -C build
%global develdocs howto_libipt.md
(cd doc;cp -p %{develdocs} ..)

%check
ctest -V %{?_smp_mflags}

%files -n %libname
%doc README
%doc --no-dereference LICENSE
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %devname
%doc %{develdocs}
%{_includedir}/*
%{_libdir}/%{name}.so



%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_2
- new version

