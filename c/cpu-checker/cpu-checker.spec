Summary: Userspace tools for helping to evaluate the CPU (or BIOS) support for various features
Name: cpu-checker
Version: 0.6
Release: alt1
License: GPLv3
Group: System/Kernel and hardware
URL: https://launchpad.net/cpu-checker
BuildArch: noarch

Source: %name-%version.tar.gz

%description
Userspace tools for helping to evaluate the CPU (or BIOS) support for various features.

%prep
%setup

%build
%make_build DESTDIR=%buildroot

%install
%makeinstall_std

%files
%_sbindir/check-bios-nx
%_sbindir/kvm-ok
%_man1dir/check-bios-nx.1.xz
%_man1dir/kvm-ok.1.xz

%changelog
* Sat Jun 10 2023 Anton Kurachenko <srebrov@altlinux.org> 0.6-alt1
- Initial build for ALT
