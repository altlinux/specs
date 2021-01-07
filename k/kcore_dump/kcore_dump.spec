Name: kcore_dump
Version: 0.0.0.2.507ad
Release: alt1

Summary: A simple tool to create a physical memory dump from userland
License: GPLv3
Group: System/Kernel and hardware
Url: https://schlafwandler.github.io/posts/dumping-/proc/kcore/
Vcs: https://github.com/schlafwandler/kcore_dump
ExclusiveArch: x86_64

Packager: Anna Khrustova <khab@altlinux.org>
Source: %name-%version.tar

%description
kcore_dump is a simple tool to create a physical memory dump
of a running x86-64 Linux system from userland.
It does so by extracting the relevant memory ranges from /proc/kcore.
The dump is written to disk in the LiME file format.

THIS TOOL HAS NOT UNDERGONE MUCH TESTING!

USE IT AT YOUR OWN RISK!

%prep
%setup

%build
gcc %optflags -o %name %name.c

%install
install -pD -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md

%changelog
* Thu Jan 07 2021 Anna Khrustova <khab@altlinux.org> 0.0.0.2.507ad-alt1
- Initial build for Sisyphus.
