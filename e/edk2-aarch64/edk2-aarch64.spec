%global optflags_lto %nil
%define tool_chain_tag GCC5
%define openssl_ver 3.0.9

# More subpackages to come once licensing issues are fixed
Name: edk2-aarch64
Version: 20240524
Release: alt1
Summary: AARCH64 Virtual Machine Firmware

License: BSD-2-Clause-Patent
Group: Emulators
Url: http://www.tianocore.org

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar
#Vcs-Git: https://github.com/openssl/openssl
Source2: openssl.tar
#Vcs-Git: https://github.com/ucb-bar/berkeley-softfloat-3.git
Source3: berkeley-softfloat-3.tar
Source4: Logo.bmp

# json description files
Source10: 50-edk2-aarch64-qcow2.json
Source11: 51-edk2-aarch64-raw.json
Source12: 52-edk2-aarch64-verbose-qcow2.json
Source13: 53-edk2-aarch64-verbose-raw.json

Patch1: %name-%version.patch

ExclusiveArch: aarch64 loongarch64 x86_64
BuildArch: noarch

Provides: edk2-ovmf-aarch64 = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: iasl nasm gcc-c++
BuildRequires: python3-devel python3-modules-sqlite3
BuildRequires: libuuid-devel
BuildRequires: qemu-img
BuildRequires: bc
# openssl configure
BuildRequires: /usr/bin/pod2man bc zlib-devel perl-PathTools perl-IPC-Cmd perl-JSON
%if %_build_cpu != aarch64
BuildRequires: gcc-aarch64-linux-gnu
%define gcc_triplet aarch64-linux-gnu-
%else
%define gcc_triplet %nil
%endif

Requires: ipxe-roms-qemu

%description
EFI Development Kit II
AARCH64 UEFI Firmware

%prep
%setup -q
%patch1 -p1

cp -f %SOURCE4 MdeModulePkg/Logo/

# cleanup
find . -name '*.efi' -print0 | xargs -0 rm -f
rm -rf BaseTools/Bin \
        UefiCpuPkg/ResetVector/Vtf0/Bin/*.raw \
        EdkCompatibilityPkg/Other \
        AppPkg \
        DuetPkg/BootSector/bin \
        StdLib/LibC/Main/Ia32/ftol2.obj \
        BeagleBoardPkg/Debugger_scripts/rvi_dummy.axf \
        BaseTools/Source/Python/*/*.pyd \
        BaseTools/Source/Python/UPT/Dll/sqlite3.dll \
        Vlv2TbltDevicePkg/GenBiosId \
        Vlv2TbltDevicePkg/*.exe \
        ArmPkg/Library/GccLto/liblto-*.a

# Ensure old shell and binary packages are not used
rm -rf EdkShellBinPkg
rm -rf EdkShellPkg
rm -rf FatBinPkg
rm -rf ShellBinPkg

# add openssl
mkdir -p CryptoPkg/Library/OpensslLib/openssl
tar -xf %SOURCE2 --strip-components 1 --directory CryptoPkg/Library/OpensslLib/openssl

# add berkeley-softfloat-3
mkdir -p ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %SOURCE3 --strip-components 1 --directory ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3

# include paths pointing to unused submodules
mkdir -p MdePkg/Library/MipiSysTLib/mipisyst/library/include
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/include
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/include/mbedtls
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/library
mkdir -p SecurityPkg/DeviceSecurity/SpdmLib/libspdm/include

%build
export PYTHON_COMMAND=%__python3
export EXTRA_OPTFLAGS="%optflags"
%if %_build_cpu != aarch64
export GCC5_AARCH64_PREFIX=aarch64-linux-gnu-
%endif
python3 CryptoPkg/Library/OpensslLib/configure.py

# for mkdosfs
export PATH=/sbin:$PATH

source ./edksetup.sh

# compiler
CC_FLAGS="-t %tool_chain_tag"

# common features
#CC_FLAGS="${CC_FLAGS} --cmd-len=65536 -b DEBUG --hash"
#CC_FLAGS="${CC_FLAGS} -b RELEASE"
CC_FLAGS="${CC_FLAGS} -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} --cmd-len=65536"
CC_FLAGS="${CC_FLAGS} -D NETWORK_IP6_ENABLE=TRUE"
CC_FLAGS="${CC_FLAGS} -D NETWORK_TLS_ENABLE=TRUE"
CC_FLAGS="${CC_FLAGS} -D NETWORK_HTTP_BOOT_ENABLE=TRUE"
CC_FLAGS="${CC_FLAGS} -D NETWORK_ISCSI_ENABLE=TRUE"
CC_FLAGS="${CC_FLAGS} -D NETWORK_ALLOW_HTTP_CONNECTIONS=TRUE"
CC_FLAGS="${CC_FLAGS} -D TPM1_ENABLE=FALSE"
CC_FLAGS="${CC_FLAGS} -D CAVIUM_ERRATUM_27456=TRUE"

VERBOSE_FLAGS="-D DEBUG_PRINT_ERROR_LEVEL=0x8040004F"
SILENT_FLAGS="-D DEBUG_PRINT_ERROR_LEVEL=0x80000000"
TPM_FLAGS="-D TPM2_ENABLE=TRUE"
NO_TPM_FLAGS="-D TPM2_ENABLE=FALSE"

# grub.efi uses EfiLoaderData for code
NX_BROKEN_SHIM_GRUB_DATA="--pcd PcdDxeNxMemoryProtectionPolicy=0xC000000000007FD1"
# shim.efi has broken MemAttr code
NX_BROKEN_SHIM_GRUB_MEM="--pcd PcdUninstallMemAttrProtocol=TRUE"
PCD_FLAGS="${NX_BROKEN_SHIM_GRUB_DATA} ${NX_BROKEN_SHIM_GRUB_MEM}"

# arm firmware features
#ARM_FLAGS="-t %%tool_chain_tag -b DEBUG --cmd-len=65536"
ARM_FLAGS="${CC_FLAGS}"


unset MAKEFLAGS

# prepare
#cp /usr/share/seabios/bios-csm.bin OvmfPkg/Csm/Csm16/Csm16.bin
#cp /usr/share/seabios/bios-csm.bin corebootPkg/Csm/Csm16/Csm16.bin
%make_build \
        -C BaseTools

#(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

# build aarch64 firmware
mkdir -p AAVMF
%{gcc_triplet}gcc -c -fpic ArmPkg/Library/GccLto/liblto-aarch64.s -o ArmPkg/Library/GccLto/liblto-aarch64.a

# Build with a verbose debug mask first, and stash the binary.
build ${ARM_FLAGS} ${VERBOSE_FLAGS} ${TPM_FLAGS} ${PCD_FLAGS} -a AARCH64 -p ArmVirtPkg/ArmVirtQemu.dsc
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_EFI.fd AAVMF/QEMU_EFI.verbose.fd
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_EFI.fd AAVMF/QEMU_EFI-pflash.raw
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_VARS.fd AAVMF/QEMU_VARS.fd
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_VARS.fd AAVMF/vars-template-pflash.raw
truncate --size 64m AAVMF/QEMU_EFI-pflash.raw
truncate --size 64m AAVMF/vars-template-pflash.raw

# Build with a silent (errors only) debug mask.
build ${ARM_FLAGS} ${SILENT_FLAGS} ${TPM_FLAGS} ${PCD_FLAGS} -a AARCH64 -p ArmVirtPkg/ArmVirtQemu.dsc
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_EFI.fd AAVMF/QEMU_EFI.silent.fd
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_EFI.fd AAVMF/QEMU_EFI-silent-pflash.raw
truncate --size 64m AAVMF/QEMU_EFI-silent-pflash.raw

# Build with a silent (errors only) debug mask and without TPM
build ${ARM_FLAGS} ${SILENT_FLAGS} ${NO_TPM_FLAGS} ${PCD_FLAGS} -a AARCH64 -p ArmVirtPkg/ArmVirtQemu.dsc
cp -a Build/ArmVirtQemu-AARCH64/*/FV/QEMU_EFI.fd AAVMF/QEMU_EFI.kernel.fd

for raw in AAVMF/*.raw; do
    qcow2="${raw%%.raw}.qcow2"
    qemu-img convert -f raw -O qcow2 -o cluster_size=4096 -S 4096 "$raw" "$qcow2"
done

%install
# For distro-provided firmware packages, the specification
# (https://git.qemu.org/?p=qemu.git;a=blob;f=docs/interop/firmware.json)
# says the JSON "descriptor files" to be searched in this directory:
# `/usr/share/firmware/`.  Create it.

mkdir -p %buildroot%_datadir/qemu/firmware
mkdir -p %buildroot%_datadir/{edk2,AAVMF}

cp -a AAVMF %buildroot%_datadir/
ln -r -s %buildroot%_datadir/AAVMF %buildroot%_datadir/edk2/aarch64

for f in %_sourcedir/*edk2-aarch64*.json; do
    install -pm 644 $f %buildroot%_datadir/qemu/firmware
done

%files
%_datadir/AAVMF
%_datadir/edk2/aarch64
%_datadir/qemu/firmware/*edk2-aarch64*.json

%changelog
* Thu Jul 25 2024 Alexey Shabalin <shaba@altlinux.org> 20240524-alt1
- edk2-stable202405
- Fixes:
  + CVE-2022-36763
  + CVE-2022-36764
  + CVE-2022-36765
  + CVE-2023-45229
  + CVE-2023-45230
  + CVE-2023-45231
  + CVE-2023-45232
  + CVE-2023-45233
  + CVE-2023-45234
  + CVE-2023-45235
  + CVE-2023-45236
  + CVE-2023-45237
  + CVE-2024-25742

* Tue Mar 05 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 20231115-alt2
- Make it possible to cross-compile the thing. Useful for ports
  (in particular loongarch64). Also the package can be built
  on an x86_64 machine (without resorting to qemu-user).

* Fri Feb 02 2024 Alexey Shabalin <shaba@altlinux.org> 20231115-alt1
- edk2-stable202311

* Wed Nov 30 2022 Alexey Shabalin <shaba@altlinux.org> 20221117-alt1
- edk2-stable202211 (Fixes: CVE-2021-38578)

* Thu Aug 11 2022 Alexey Shabalin <shaba@altlinux.org> 20220526-alt1
- edk2-stable202205
- update BaseALT logo

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 20220221-alt1
- edk2-stable202202

* Thu Jan 06 2022 Alexey Shabalin <shaba@altlinux.org> 20211125-alt1
- edk2-stable202111

* Sat Feb 13 2021 Alexey Shabalin <shaba@altlinux.org> 20201127-alt2
- build with -b DEBUG

* Sun Jan 17 2021 Alexey Shabalin <shaba@altlinux.org> 20201127-alt1
- edk2-stable202011 (Fixes: CVE-2019-14584, CVE-2019-11098)

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 20191122-alt1
- edk2-stable201911

* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt2
- build as edk2-aarch64 package

* Wed Jun 19 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt1
- edk2-stable201905 (Fixes: CVE-2018-12182)

* Tue Apr 02 2019 Alexey Shabalin <shaba@altlinux.org> 20190308-alt1
- edk2-stable201903 (Fixes: CVE-2018-12178, CVE-2018-12180, CVE-2018-12181, CVE-2018-3630)

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 20181113-alt1
- edk2-stable201811

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt3
- snapshot of UDK2017 branch

* Mon Sep 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 20170720-alt2
- added efi-shell subpackage

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt1
- snapshot of UDK2017 branch

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 20161227-alt1
- UDK2017 branch

* Wed May 25 2016 Alexey Shabalin <shaba@altlinux.ru> 20160518-alt1
- master snapshot 855743f7177459bea95798e59b6b18dab867710c

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 20151225-alt1.svn19549
- build from branche UDK2015

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt2
- buils ovmf as noarch

* Wed Jun 17 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt1
- svn snapshot r17642
- add ovmf package

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 20140722svn2674-alt1
- svn snapshot r2674

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1.svn2594
- initial build
