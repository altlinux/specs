Name: shim-signed
Version: 16.1
Release: alt1

Summary: UEFI Secure Boot shim signed by Microsoft
License: BSD-2-Clause-Patent
Group: System/Kernel and hardware

Url: https://github.com/rhboot/shim
VCS: https://github.com/rhboot/shim.git
Source: %name-%version.tar

BuildRequires: rpm-macros-uefi
ExclusiveArch: x86_64 aarch64

%description
This package contains shim binaries signed by "Microsoft Corporation UEFI CA
2011" and "Microsoft UEFI CA 2023" keys for x64, ia32 and aa64 efi
architectures. MokManager (as mm*.efi) and fallback (as fb*.efi) utilities
signed by "ALT Linux Secure Boot Signer" are provided as well.

%prep
%setup

%install
mkdir -p %buildroot%_efi_bindir %buildroot%_libexecdir/shim

install -Dpm 0644 {fb,mm}%_efi_arch.efi -t %buildroot%_efi_bindir/
install -Dpm 0644 msuefica2011/shim%_efi_arch.efi -t %buildroot%_efi_bindir/msuefica2011
install -Dpm 0644 msuefica2023/shim%_efi_arch.efi -t %buildroot%_efi_bindir/msuefica2023
ln -svf msuefica2011/shim%_efi_arch.efi %buildroot%_efi_bindir/shim%_efi_arch.efi

install -Dpm 0644 BOOT%_efi_arch_upper.CSV -t %buildroot%_libexecdir/shim/

%ifarch x86_64
install -Dpm 0644 {fb,mm}ia32.efi -t %buildroot%_efi_bindir/
install -Dpm 0644 msuefica2011/shimia32.efi -t %buildroot%_efi_bindir/msuefica2011
install -Dpm 0644 msuefica2023/shimia32.efi -t %buildroot%_efi_bindir/msuefica2023
ln -svf msuefica2011/shimia32.efi %buildroot%_efi_bindir/shimia32.efi

install -Dpm 0644 BOOTIA32.CSV -t %buildroot%_libexecdir/shim/
%endif

%files
%dir %attr(0755,root,root) %_libexecdir/shim
%attr(0644,root,root) %_efi_bindir/*.efi
%dir %attr(0755,root,root) %_efi_bindir/msuefica2011
%attr(0644,root,root) %_efi_bindir/msuefica2011/*.efi
%dir %attr(0755,root,root) %_efi_bindir/msuefica2023
%attr(0644,root,root) %_efi_bindir/msuefica2023/*.efi
%attr(0644,root,root) %_libexecdir/shim/BOOT*.CSV

%changelog
* Tue Jun 09 2026 Egor Ignatov <egori@altlinux.org> 16.1-alt1
- new shim version
- add aarch64 build

* Mon Apr 29 2024 Egor Ignatov <egori@altlinux.org> 15.8-alt1
- new shim version

* Thu Feb 10 2022 Nikolai Kostrigin <nickel@altlinux.org> 15.4-alt2
- replace with binaries rebuilt with multiple upstream fixes
  + address https://github.com/fwupd/firmware-lenovo/issues/129

* Thu Jul 08 2021 Nikolai Kostrigin <nickel@altlinux.org> 15.4-alt1
- new shim version

* Mon Dec 21 2020 Nikolai Kostrigin <nickel@altlinux.org> 15-alt2
- add BOOT<efi_arch>.CSV files for fallback boot variable creation

* Mon Mar 18 2019 Nikolai Kostrigin <nickel@altlinux.org> 15-alt1
- new shim version
  + add EFI ia32 binaries as well
  + MokManager and fallback are now renamed to mm<efi_arch>.efi and
    fb<efi_arch>.efi respectively
- adjust spec accordingly to new upstream

* Fri Jun 09 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt6
- built for sisyphus

* Wed Jun 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt5
- made shim binaries accessible also by debian'ish paths

* Sat Apr 01 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt4
- removed ALT signature (closes: #33314)

* Tue Dec 10 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt3
- added ALT signature

* Fri Nov 22 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt2
- added fallback.efi
- signed supplementary binaries with ALT key for versatility

* Tue Nov 19 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- ALT build

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- only makes sense for x86_64

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- initial release
