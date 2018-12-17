%define _unpackaged_files_terminate_build 1

Summary: JaCarta PKCS#11 Tool
Name: jacarta-tool
Version: 0.0.6
Release: alt1
License: GPLv2
Url: http://git.altlinux.org/people/krash/public/jacarta-tool.git
Group: Development/Tools
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake boost-program-options-devel openssl-devel

Requires: libjcpkcs11 >= 2.1.3

%description
JaCarta PKCS#11 Tool.

%prep
%setup

%build
%cmake

%install
%cmakeinstall_std

%files
%_bindir/*

%changelog
* Mon Dec 17 2018 Leonid Krashenko <krash@altlinux.org> 0.0.6-alt1
- Updated to jacarta-tool 0.0.6.

* Mon Dec 03 2018 Leonid Krashenko <krash@altlinux.org> 0.0.5-alt1
- Updated to jacarta-tool 0.0.5.

* Thu Nov 30 2018 Leonid Krashenko <krash@altlinux.org> 0.0.4-alt1
- Initial build.
