%define _unpackaged_files_terminate_build 1
%define kflavours 6.12 6.13 6.14
%define inst_dir %_sysconfdir/apt/sources.list.d
%define alt_url https://lakostis.unsafe.ru/RPMS/ALTLinux

Name: apt-repo-lakostis-kmodules
Version: 0.0.1
Release: alt5

Summary: kernel modules from alt-lakostis repo

License: MIT
Group: System/Configuration/Other
Url: https://alt-lakostis.gitlab.io/kmodules

ExclusiveArch: x86_64
Requires: apt-https ca-certificates

%description
This is an apt repo configuration to install additional kernel modules
maintained at %url.

WARNING! Those kernel modules are not supported by ALTLinux/Basealt,
use at own risk!

%prep

%build

%install
mkdir -p %buildroot%inst_dir
for flavour in %kflavours; do
    printf 'rpm %url/%s/repo x86_64 hasher\n' "$flavour" > %buildroot%inst_dir/alt-lakostis-kmodules-"$flavour".list
    printf '#rpm %alt_url/%s/repo x86_64 hasher\n' "$flavour" > %buildroot%inst_dir/lakostis-unsafe-ru-kmodules-"$flavour".list
done

%files
%inst_dir/*.list

%changelog
* Tue Apr 08 2025 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt5
- Added unsafe.ru mirror.

* Tue Feb 25 2025 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt4
- add 6.14.

* Tue Feb 25 2025 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt3
- remove 6.6.

* Sat Jan 11 2025 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt2
- add 6.13.
- remove 6.11 (EOL).

* Sat Nov 23 2024 L.A. Kostis <lakostis@altlinux.ru> 0.0.1-alt1
- Initial build for ALTLinux.
