Name: cmake-modules-liri
Version: 1.1.0
Release: alt4

Summary: Liri-specific cmake modules
License: BSD
Group: Development/Other
Url: https://github.com/lirios/cmake-shared

Source: %name-%version-%release.tar
BuildRequires: gcc-c++ cmake >= 3.10
BuildArch: noarch

Requires: extra-cmake-modules >= 5.48.0

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README*
%_datadir/LiriCMakeShared

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt4
- v1.1.0-32-g8122f2b

* Fri Aug 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt3
- updated from git.11c53a1

* Thu Oct 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt2
- rebuilt as arch-independent

* Thu Oct 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
