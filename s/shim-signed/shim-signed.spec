Name: shim-signed
Version: 16.1
Release: alt2

Summary: UEFI Secure Boot shim signed by Microsoft
License: BSD-2-Clause-Patent
Group: System/Kernel and hardware

Url: https://github.com/rhboot/shim
VCS: https://github.com/rhboot/shim.git
Source: %name-%version.tar

BuildRequires: pesign
BuildRequires: rpm-macros-uefi
ExclusiveArch: x86_64 aarch64

Requires: shim-signed-compat = %EVR
Requires: shim-signed-dualsign = %EVR

%description
This package contains shim binaries signed by "Microsoft Corporation UEFI CA
2011" and "Microsoft UEFI CA 2023" keys for x64, ia32 and aa64 efi
architectures. MokManager (as mm*.efi) and fallback (as fb*.efi) utilities
signed by "ALT Linux Secure Boot Signer" are provided as well.

# temporarily needed for compatibility with grub <= 2.12-alt16
%package compat
Summary: Compatibility symlinks to signed shim binaries
Group: System/Kernel and hardware

%description compat
This package makes signed shim binaries accessible by debian'ish paths
under %_libexecdir/shim (as *.efi.signed symlinks) and provides
BOOT<efi_arch>.CSV files for fallback boot variable creation.

%package dualsign
Summary: Shim binaries carrying both Microsoft UEFI CA 2011 and 2023 signatures
Group: System/Kernel and hardware
Requires: shim-signed = %EVR

%description dualsign
Shim binaries with two signatures in a single PE certificate table:
"Microsoft Corporation UEFI CA 2011" first and "Microsoft UEFI CA 2023"
second, merged with pesign from the Microsoft-signed binaries.

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

# dual-signed binaries for shim-signed-dualsign: "Microsoft Corporation
# UEFI CA 2011" signature goes first because some firmware validates only
# the first certificate table entry, "Microsoft UEFI CA 2023" goes second
sign2011=%buildroot%_efi_bindir/msuefica2011
sign2023=%buildroot%_efi_bindir/msuefica2023
dualsign=%buildroot%_efi_bindir/dualsign
mkdir -p "$dualsign"
for pefile in "$sign2011"/*.efi; do
    name="${pefile##*/}"

    # both signatures must cover the same PE image
    pesign -i "$sign2011/$name" --hash > "$name".h2011
    pesign -i "$sign2023/$name" --hash > "$name".h2023
    read hash2011 _ < "$name".h2011
    read hash2023 _ < "$name".h2023
    [ "$hash2011" = "$hash2023" ]

    # export the 2023 signature and append it to the 2011-signed binary
    pesign -i "$sign2023/$name" -u 0 --export-signature "$name".sig2023
    pesign -i "$sign2011/$name" -u 1 --import-signature "$name".sig2023 \
       -o "$dualsign/$name"

    # verify both slots byte-for-byte against the source signatures
    pesign -i "$sign2011/$name" -u 0 --export-signature "$name".sig2011
    pesign -i "$dualsign/$name" -u 0 --export-signature "$name".v0
    pesign -i "$dualsign/$name" -u 1 --export-signature "$name".v1
    cmp "$name".v0 "$name".sig2011
    cmp "$name".v1 "$name".sig2023
done

# compat symlinks for shim-signed-compat
for pefile in %buildroot%_efi_bindir/*.efi; do
    pefile="${pefile##*/}"
    ln -sv %_efi_bindir/"$pefile" \
       %buildroot%_libexecdir/shim/"$pefile".signed
done

%files
%attr(0644,root,root) %_efi_bindir/*.efi
%dir %attr(0755,root,root) %_efi_bindir/msuefica2011
%attr(0644,root,root) %_efi_bindir/msuefica2011/*.efi
%dir %attr(0755,root,root) %_efi_bindir/msuefica2023
%attr(0644,root,root) %_efi_bindir/msuefica2023/*.efi

%files compat
%dir %attr(0755,root,root) %_libexecdir/shim
%_libexecdir/shim/*.efi.signed
%attr(0644,root,root) %_libexecdir/shim/BOOT*.CSV

%files dualsign
%dir %attr(0755,root,root) %_efi_bindir/dualsign
%attr(0644,root,root) %_efi_bindir/dualsign/*.efi

%changelog
* Wed Jul 08 2026 Egor Ignatov <egori@altlinux.org> 16.1-alt2
- restore *.efi.signed under %%_libexecdir/shim as symlinks
- move %%_libexecdir/shim to new compat subpackage
- add dualsign subpackage with both Microsoft signatures

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
