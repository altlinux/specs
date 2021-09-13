%define _unpackaged_files_terminate_build 1

%def_with check

Name: shim
Version: 15.4
Release: alt3

Summary: First-stage UEFI bootloader
License: BSD
Group: System/Kernel and hardware

Url: https://github.com/rhboot/shim
#Git: https://github.com/rhboot/shim.git
Source: %name-%version.tar
Source1: altlinux-ca.cer
Source2: %name-%version-gnu-efi.tar

Patch101: shim-15.4-upstream-0001-Fix-handling-of-ignore_db-and-user_insecure_mode.patch
Patch103: shim-15.4-upstream-0003-Fix-a-broken-file-header-on-ia32.patch
Patch104: shim-15.4-upstream-0004-mok-allocate-MOK-config-table-as-BootServicesData.patch
Patch105: shim-15.4-upstream-0005-Don-t-call-QueryVariableInfo-on-EFI-1.10-machines.patch
Patch106: shim-15.4-upstream-0006-Post-process-our-PE-to-be-sure.patch
Patch107: shim-15.4-upstream-0007-Relax-the-check-for-import_mok_state.patch
Patch110: shim-15.4-upstream-0010-shim-another-attempt-to-fix-load-options-handling.patch
Patch120: shim-15.4-upstream-0020-shim-move-the-bulk-of-set_second_stage-to-its-own-fi.patch
Patch122: shim-15.4-upstream-0022-shim-don-t-fail-on-the-odd-LoadOptions-length.patch
Patch123: shim-15.4-upstream-0023-arm-aa64-fix-the-size-of-.rela-sections.patch
Patch124: shim-15.4-upstream-0024-mok-fix-potential-buffer-overrun-in-import_mok_state.patch
Patch125: shim-15.4-upstream-0025-mok-relax-the-maximum-variable-size-check.patch
Patch126: shim-15.4-upstream-0026-Don-t-unhook-ExitBootServices-when-EBS-protection-is.patch
Patch127: shim-15.4-upstream-0027-fallback-find_boot_option-needs-to-return-the-index-.patch
Patch128: shim-15.4-upstream-0028-httpboot-Ignore-case-when-checking-HTTP-headers.patch
Patch129: shim-15.4-upstream-0029-fallback-incorrect-check-after-AllocateZeroPool.patch
Patch130: shim-15.4-upstream-0030-fallback-free-the-right-variable-on-the-read_file-er.patch
Patch131: shim-15.4-upstream-0031-shim-avoid-BOOTx64.EFI-in-message-on-other-architect.patch
Patch132: shim-15.4-upstream-0032-str-remove-duplicate-parameter-check.patch
Patch133: shim-15.4-upstream-0033-fallback-Print-info-on-GetNextVariableName-errors.patch
Patch134: shim-15.4-upstream-0034-fallback-Use-a-dynamic-buffer-when-list-var-names.patch
Patch135: shim-15.4-upstream-0035-fallback-add-compile-option-FALLBACK_NONINTERACTIVE.patch

BuildRequires(pre): rpm-macros-uefi
BuildRequires: pesign >= 0.106
BuildRequires: libelf-devel
BuildRequires: dos2unix

%if_with check
BuildRequires: xxd
%endif

# Shim is only required on platforms implementing the UEFI secure boot
# protocol. The only one of those we currently wish to support is 64-bit x86.
# Adding further platforms will require adding appropriate relocation code.
ExclusiveArch: x86_64

# Figure out the right file path to use
%global efidir altlinux
# SBAT generation number for ALT (refer to SBAT.md)
%global alt_gen_number 1

%description
Initial UEFI bootloader that handles chaining to a trusted
full bootloader under secure boot environments.

%package -n %name-unsigned
Summary: First-stage UEFI bootloader (unsigned data)
Group: System/Kernel and hardware

%description -n %name-unsigned
Initial UEFI bootloader that handles chaining to a trusted
full bootloader under secure boot environments.
Includes both ia32 and x64 EFI binaries.

%prep
%setup -a 2

%patch101 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch110 -p1
%patch120 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1

# fill in SBAT section with ALT data
echo "shim.altlinux,%alt_gen_number,ALT Linux,shim,%version-%release,http://git.altlinux.org/gears/s/shim.git" > data/sbat.altlinux.csv

%build
MAKEFLAGS=""
if [ -f "%SOURCE1" ]; then
	MAKEFLAGS="VENDOR_CERT_FILE=%SOURCE1"
fi

mkdir build-ia32 build-x64
pushd build-ia32
  %make_build ${MAKEFLAGS} TOPDIR=.. ARCH=ia32 -f ../Makefile
popd
pushd build-x64
  %make_build ${MAKEFLAGS} TOPDIR=.. -f ../Makefile
popd

%install
#be aware of installation target options - refer to BUILDING
pushd build-ia32
make TOPDIR=.. ARCH=ia32 \
     DESTDIR=%buildroot EFIDIR=%efidir \
     -f ../Makefile install-as-data
pesign -h -P -i shimia32.efi -h > shimia32.hash
install -m 0644 shimia32.hash %buildroot%_datadir/shim/%version/ia32/shimia32.hash
install -m 0644 BOOTIA32.CSV %buildroot%_datadir/shim/%version/ia32/BOOTIA32.CSV
popd
pushd build-x64
make TOPDIR=.. DESTDIR=%buildroot EFIDIR=%efidir \
     -f ../Makefile install-as-data
pesign -h -P -i shimx64.efi -h > shimx64.hash
install -m 0644 shimx64.hash %buildroot%_datadir/shim/%version/%_efi_arch/shimx64.hash
install -m 0644 BOOTX64.CSV %buildroot%_datadir/shim/%version/%_efi_arch/BOOTX64.CSV
popd

%check
%make_build ARCH=ia32 test
%make_build test

%files -n %name-unsigned
%doc README.md README.fallback README.tpm COPYRIGHT
%dir %_datadir/shim
%dir %_datadir/shim/%version
%dir %_datadir/shim/%version/ia32
%dir %_datadir/shim/%version/%_efi_arch
%_datadir/shim/%version/%_efi_arch/*
%_datadir/shim/%version/ia32/*

%changelog
* Mon Sep 06 2021 Nikolai Kostrigin <nickel@altlinux.org> 15.4-alt3
- rearrange patch set to include recent upstream commits

* Tue Apr 27 2021 Nikolai Kostrigin <nickel@altlinux.org> 15.4-alt2
- fix critical issues discovered recently
  + add upstream-fix-mokutil--disable-validation-does-not-work patch
  + add upstream-mok-config-table-as-bootservicesdata patch
  + add upstream-don-t-call-queryvariableinfo-on-efi-1.10 patch
  + add upstream-fix-build-with-old-binutils-on-aarch64 patch

* Fri Apr 02 2021 Nikolai Kostrigin <nickel@altlinux.org> 15.4-alt1
- new version
  + introduce SBAT
  + use bundled gnu-efi version from rhboot/gnu-efi
    (git submodule, refer to c61bfdc8 for details)
- add script for submodules update (thanks to darktemplar@)
- remove fix-gcc9-address-of-packed-members patch
- remove upstream-fix-a-typo patch
- add upstream-fix-a-broken-file-header-on-ia32 patch
- spec: add dos2unix to BR:, remove gnu-efi
  + add ALT specific SBAT data
  + add check section
- replace altlinux-ca.cer

* Tue Sep 15 2020 Nikolai Kostrigin <nickel@altlinux.org> 15-alt4
- fix FTBFS against gnu-efi 3.0.10+ due to fixed typo
  + add upstream-fix-a-typo patch

* Tue Mar 31 2020 Nikolai Kostrigin <nickel@altlinux.org> 15-alt3
- fix FTBFS with gcc9
  + add fix-gcc9-address-of-packed-members patch

* Tue Oct 30 2018 Nikolai Kostrigin <nickel@altlinux.org> 15-alt2
- rebuild against gnu-efi 3.0.9
- remove ubt

* Thu Jul 05 2018 Nikolai Kostrigin <nickel@altlinux.org> 15-alt1
- new version
  + unbundle mokutil package
  + remove patches (upstream application)

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 0.4-alt1.3
- FTBFS workaround: use gcc4.7

* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1.2
- rebuilt for Sisyphus

* Thu Aug 01 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1.1
- replaced fedora-ca.cer with altlinux-ca.cer

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- actually built for ALT Linux
  + based on fedora's 0.3-2 spec by pjones@

* Fri Jun 07 2013 Peter Jones <pjones@redhat.com> - 0.3-2
- Require gnu-efi-3.0q for now.
- Don't allow mmx or sse during compilation.
- Re-organize this so all real signing happens in shim-signed instead.
- Split out mokutil

* Wed Dec 12 2012 Peter Jones <pjones@redhat.com> - 0.2-3
- Fix mokutil's idea of signature sizes.

* Wed Nov 28 2012 Matthew Garrett <mjg59@srcf.ucam.org> - 0.2-2
- Fix secure_mode() always returning true

* Mon Nov 26 2012 Matthew Garrett <mjg59@srcf.ucam.org> - 0.2-1
- Update shim
- Include mokutil
- Add debuginfo package since mokutil is a userspace executable

* Mon Oct 22 2012 Peter Jones <pjones@redhat.com> - 0.1-4
- Produce an unsigned shim

* Tue Aug 14 2012 Peter Jones <pjones@redhat.com> - 0.1-3
- Update how embedded cert and signing work.

* Mon Aug 13 2012 Josh Boyer <jwboyer@redhat.com> - 0.1-2
- Add patch to fix image size calculation

* Mon Aug 13 2012 Matthew Garrett <mjg@redhat.com> - 0.1-1
- initial release
