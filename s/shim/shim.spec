%define _unpackaged_files_terminate_build 1

%def_with check

Name: shim
Version: 15.7
Release: alt2

Summary: First-stage UEFI bootloader
License: BSD
Group: System/Kernel and hardware

Url: https://github.com/rhboot/shim
Source: %name-%version.tar
Source1: altlinux-ca.cer
Source2: %name-%version-gnu-efi.tar

Patch0: shim-15.7-upstream-Enable-the-NX-compatibility-flag-by-default.patch

BuildRequires(pre): rpm-macros-uefi
BuildRequires: pesign >= 0.106
BuildRequires: libelf-devel
BuildRequires: dos2unix

%if_with check
BuildRequires: xxd
BuildRequires: libefivar-devel
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
%patch0 -p1

echo "shim.altlinux,%alt_gen_number,ALT Linux,shim,%version-%release,http://git.altlinux.org/gears/s/shim.git" > data/sbat.altlinux.csv

%build
MAKEFLAGS="DISABLE_REMOVABLE_LOAD_OPTIONS=1"
if [ -f "%SOURCE1" ]; then
	MAKEFLAGS="VENDOR_CERT_FILE=%SOURCE1 $MAKEFLAGS"
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
* Tue Feb 28 2023 Egor Ignatov <egori@altlinux.org> 15.7-alt2
- add shim-15.7-upstream-Enable-the-NX-compatibility-flag-by-default patch
- remove obsolete Make.defaults-skip-Werror-restrict-and-Werror-string patch

* Wed Nov 30 2022 Egor Ignatov <egori@altlinux.org> 15.7-alt1
- new version

* Mon Feb 21 2022 Nikolai Kostrigin <nickel@altlinux.org> 15.5-alt1
- new version
- remove all previously added upstream patches contained in this version
- spec: update check section
- spec: build with DISABLE_REMOVABLE_LOAD_OPTIONS

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
