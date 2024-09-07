%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global sover 2

Name: libipt
Version: 2.1.1
Release: alt1
Summary: Intel Processor Trace Decoder Library
Group: System/Kernel and hardware
License: BSD-3-Clause
Url: https://github.com/intel/libipt
ExclusiveArch: %ix86 x86_64

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: /usr/bin/pandoc
%{?!_without_check:%{?!_disable_check:
BuildRequires: ctest
}}

%description
The Intel Processor Trace (Intel PT) Decoder Library is Intel's reference
implementation for decoding Intel PT. It can be used as a standalone
library or it can be partially or fully integrated into your tool.

%package -n libipt-devel
Group: Development/Tools
Summary: Header files and libraries for Intel Processor Trace Decoder Library
Requires: libipt%sover = %EVR

%description -n libipt-devel
The %name-devel package contains the header files and libraries needed
to develop programs that use the Intel Processor Trace (Intel PT)
Decoder Library.

%package -n libipt%sover
Summary: Intel Processor Trace Decoder Library
Group: System/Libraries

%description -n libipt%sover
The Intel Processor Trace (Intel PT) Decoder Library is Intel's reference
implementation for decoding Intel PT. It can be used as a standalone
library or it can be partially or fully integrated into your tool.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
       -DPTUNIT:BOOL=ON \
       -DMAN:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libipt%sover
%doc LICENSE
%_libdir/libipt.so.%sover
%_libdir/libipt.so.%sover.*

%files -n libipt-devel
%doc README doc/*.md
%_includedir/intel-pt.h
%_libdir/libipt.so
%_man3dir/pt*.3*

%changelog
* Sat Sep 07 2024 Vitaly Chikunov <vt@altlinux.org> 2.1.1-alt1
- Build changed from mgaimport to git.
- Update to v2.1.1 (2024-02-28).

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

