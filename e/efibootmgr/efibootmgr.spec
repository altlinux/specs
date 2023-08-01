Name: efibootmgr
Version: 18
Release: alt1

Summary: EFI Boot Manager
Group: System/Kernel and hardware
License: GPLv2+
URL: https://github.com/rhboot/efibootmgr
ExclusiveArch: %ix86 x86_64 aarch64 riscv64
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: libpci-devel zlib-devel libefivar-devel libpopt-devel

%description
efibootmgr displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about EFI can be found at
http://developer.intel.com/technology/efi/efi.htm and http://uefi.org/.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS='%{optflags}'  LDFLAGS="$RPM_LD_FLAGS" EFIDIR='altlinux'

%install
%makeinstall_std EFIDIR='altlinux'

%files
%doc AUTHORS README
%_sbindir/*
%_man8dir/*.*

%changelog
* Sat Jul 08 2023 Anton Farygin <rider@altlinux.ru> 18-alt1
- 17 -> 18

* Mon Mar 15 2021 Nikita Ermakov <arei@altlinux.org> 17-alt2
- add riscv64 to ExclusiveArch list

* Mon Oct 22 2018 Anton Farygin <rider@altlinux.ru> 17-alt1
- 16->17

* Fri Apr 27 2018 Anton Farygin <rider@altlinux.ru> 16-alt1
- 15 -> 16

* Tue Jun 20 2017 Anton Farygin <rider@altlinux.ru> 15-alt1
- new version from new upstream

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 0.6.0-alt2
- FTBFS workaround: use gcc4.7

* Tue Feb 05 2013 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- 0.5.4 -> 0.6.0

* Fri Apr 11 2008 Igor Zubkov <icesik@altlinux.org> 0.5.4-alt1
- build for Sisyphus

* Thu Jan  3 2008 Matt Domsch <Matt_Domsch@dell.com> 0.5.4-1
- split efibootmgr into its own RPM for Fedora/RHEL.

* Thu Aug 24 2004 Matt Domsch <Matt_Domsch@dell.com>
- new home linux.dell.com

* Fri May 18 2001 Matt Domsch <Matt_Domsch@dell.com>
- See doc/ChangeLog
