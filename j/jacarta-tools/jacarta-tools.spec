%define _unpackaged_files_terminate_build 1

Summary: JaCarta PKCS#11 Tools
Name: jacarta-tools
Version: 0.0.8
Release: alt2
License: MIT
Url: http://git.altlinux.org/people/krash/public/jacarta-tools.git
Group: Development/Tools
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
JaCarta PKCS#11 Tools.

%prep
%setup -q

%build
%cmake

%install
%cmakeinstall_std

%files
%_bindir/*

%changelog
* Mon Feb 11 2019 Leonid Krashenko <krash@altlinux.org> 0.0.8-alt2
- ix86 arch support.

* Wed Jan 30 2019 Leonid Krashenko <krash@altlinux.org> 0.0.8-alt1
- Initial build.
