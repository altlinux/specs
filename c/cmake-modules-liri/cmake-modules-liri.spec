Name: cmake-modules-liri
Version: 1.1.0
Release: alt1

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
* Thu Oct 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
