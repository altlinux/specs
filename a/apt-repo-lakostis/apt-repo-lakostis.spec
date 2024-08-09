%define _unpackaged_files_terminate_build 1

Name: apt-repo-lakostis
Version: 0.0.1
Release: alt1

Summary: lakostis.unsafe.ru package repo

License: MIT
Group: System/Configuration/Other
Url: https://lakostis.unsafe.ru/RPMS/ALTLinux

Source0: lakostis-unsafe-ru.list

ExclusiveArch: x86_64 noarch

%description
This is an apt repo configuration to ease switch to lakostis.unsafe.ru
packages. Those packages have extra functionality and more recent than version
in Sisyphus/branch.

WARNING! packages from lakostis.unsafe.ru are not supported by
ALTLinux/Basealt, use at own risk!

%prep

%build

%install
install -pDm644 %SOURCE0 %buildroot%_sysconfdir/apt/sources.list.d/lakostis-unsafe-ru.list

%files
%_sysconfdir/apt/sources.list.d/lakostis-unsafe-ru.list

%changelog
* Thu Aug 08 2024 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt1
- Initial build for ALTLinux.
