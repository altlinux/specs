Name: mokutil
Version: 0.5.0
Release: alt1
Epoch: 1

Summary: Tool to manage UEFI Secure Boot MoK Keys
License: GPLv3+
Group: System/Kernel and hardware
Url: https://github.com/lcp/mokutil
#Git: https://github.com/lcp/mokutil.git
Source: %name-%version.tar

BuildRequires: gnu-efi
BuildRequires: efivar-devel
BuildRequires: efivar
BuildRequires: openssl-devel
BuildRequires: openssl
BuildRequires: libkeyutils-devel
Conflicts: shim0.4-unsigned

ExclusiveArch: x86_64

%description
mokutil provides a tool to manage keys for Secure Boot through the MoK
("Machine's Own Keys") mechanism.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
make PREFIX=%prefix LIBDIR=%_libdir DESTDIR=%buildroot install

%files
%doc README COPYING
%_bindir/mokutil
%_mandir/man1/*
%_datadir/bash-completion/completions/mokutil

%changelog
* Tue Jul 27 2021 Nikolai Kostrigin <nickel@altlinux.org> 1:0.5.0-alt1
- new version
  + spec: add libkeyutils-devel to BR

* Fri Jun 28 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:0.4.0-alt1
- new version
  + spec: remove rpm-build-ubt from BR

* Fri Jun 14 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:0.3.0-alt3.dev.git20180724
- remove ubt

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1:0.3.0-alt2.dev.git20180724
- rebuilt with openssl-1.1

* Tue Jul 31 2018 Nikolai Kostrigin <nickel@altlinux.org> 1:0.3.0-alt1.dev.git20180724
- first independent package for ALT Linux
  + raise epoch due to package unbundling from shim-unsigned-0.4

* Mon Oct 06 2014 Peter Jones <pjones@redhat.com> - 0.2.0-1
- First independent package.

