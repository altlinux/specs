Name: ryzenadj
Version: 0.19.0
Release: alt1

Summary: Adjust power management settings for Ryzen Mobile Processors
License: LGPLv3
Group: System/Configuration/Hardware
Url: https://github.com/FlyGoat/RyzenAdj/
Vcs: https://github.com/FlyGoat/RyzenAdj.git

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libpci-devel

ExclusiveArch: %ix86 x86_64

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_bindir/%name

%changelog
* Wed May 13 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.19.0-alt1
- 0.19.0

* Thu May 29 2025 Andrew A. Vasilyev <andy@altlinux.org> 0.17.0-alt1
- 0.17.0

* Fri Feb 21 2025 Andrew A. Vasilyev <andy@altlinux.org> 0.16.0-alt1
- Initial build for ALT.
