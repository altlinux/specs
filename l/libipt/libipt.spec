# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/pandoc ctest
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major 2
%define libname libipt%{major}
%define devname libipt-devel

Name: libipt
Version: 2.0.5
Release: alt1_1
SummarY: Intel Processor Trace Decoder Library
Group:	 Development/Tools
License: BSD
URL: https://github.com/intel/libipt
Source0: https://github.com/intel/libipt/archive/v%{version}.tar.gz
Patch0: libipt-gcc11.patch
# c++ is required only for -DPTUNIT test "ptunit-cpp".
# pandoc is for -DMAN.
BuildRequires: gcc-c++ cmake
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
%setup -q -n libipt-%{version}
%patch0 -p1

%build
%{mageia_cmake} \
       -DPTUNIT:BOOL=ON \
       -DMAN:BOOL=OFF \
       -DDEVBUILD:BOOL=ON
%mageia_cmake_build

%install
%mageia_cmake_install

%global develdocs howto_libipt.md
(cd doc;cp -p %{develdocs} ..)

%check
%{mageia_ctest}

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
* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 2.0.5-alt1_1
- update by mgaimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 2.0.4-alt1_1
- update by mgaimport

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_1
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- fixed build

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_2
- new version

