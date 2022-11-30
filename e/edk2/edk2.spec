%global optflags_lto %nil
%define tool_chain_tag GCC5
%define openssl_ver 1.1.1s
%def_disable skip_enroll

# More subpackages to come once licensing issues are fixed
Name: edk2
Version: 20221117
Release: alt1
Summary: EFI Development Kit II

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

# ALT-specific JSON "descriptor files"
Source14: 40-edk2-ovmf-x64-sb-enrolled.json
Source15: 50-edk2-ovmf-x64-sb.json
Source16: 60-edk2-ovmf-x64.json
Source17: 40-edk2-ovmf-ia32-sb-enrolled.json
Source18: 50-edk2-ovmf-ia32-sb.json
Source19: 60-edk2-ovmf-ia32.json
Source20: 60-edk2-ovmf-x64-microvm.json
Source21: 60-edk2-ovmf-x64-amdsev.json
Source22: 60-edk2-ovmf-x64-inteltdx.json

Patch1: %name-%version.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-python3
BuildRequires: iasl nasm gcc-c++
BuildRequires: python3-devel python3-modules-sqlite3
BuildRequires: libuuid-devel
BuildRequires: xorriso dosfstools mtools
BuildRequires: /proc /dev/pts
BuildRequires: bc
BuildRequires: python3-module-virt-firmware

%description
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.

%package ovmf
Summary: Open Virtual Machine Firmware
Group: Emulators
License: BSD-2-Clause and OpenSSL
BuildArch: noarch
Provides: edk2-ovmf-x86_64 = %EVR
Requires: ipxe-roms-qemu
Requires: seavgabios

%description ovmf
EFI Development Kit II
Open Virtual Machine Firmware

%package ovmf-ia32
Summary: Open Virtual Machine Firmware
Group: Emulators
License: BSD-2-Clause and OpenSSL
BuildArch: noarch
Requires: ipxe-roms-qemu
Requires: seavgabios

%description ovmf-ia32
EFI Development Kit II
Open Virtual Machine Firmware (ia32)

%package efi-shell
Summary: EFI Development Kit II
Group: System/Kernel and hardware
Provides: efi-shell = 2.2
Obsoletes: efi-shell < 2.2

%description efi-shell
EFI Development Kit II implementation of UEFI Shell 2.0+

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

%build
export PYTHON_COMMAND=%__python3
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
CC_FLAGS="${CC_FLAGS} -D TPM2_ENABLE=TRUE"
CC_FLAGS="${CC_FLAGS} -D TPM1_ENABLE=TRUE"

# ovmf features
OVMF_2M_FLAGS="${CC_FLAGS} -D FD_SIZE_2MB=TRUE"
OVMF_4M_FLAGS="${CC_FLAGS} -D FD_SIZE_4MB=TRUE"

# secure boot features
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SECURE_BOOT_ENABLE=TRUE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SMM_REQUIRE=TRUE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D EXCLUDE_SHELL_FROM_FD=TRUE -D BUILD_SHELL=FALSE"
#OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D EXCLUDE_SHELL_FROM_FD=TRUE"

# arm firmware features
#ARM_FLAGS="-t %%tool_chain_tag -b DEBUG --cmd-len=65536"
ARM_FLAGS="${CC_FLAGS}"

unset MAKEFLAGS

%make_build \
        -C BaseTools


#(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

#mkdir -p FatBinPkg/EnhancedFatDxe/{X64,Ia32}
#source ./edksetup.sh

build_iso() {
  dir="$1"
  UEFI_SHELL_BINARY=${dir}/Shell.efi
  ENROLLER_BINARY=${dir}/EnrollDefaultKeys.efi
  UEFI_SHELL_IMAGE=uefi_shell.img
  ISO_IMAGE=${dir}/UefiShell.iso
 
  UEFI_SHELL_BINARY_BNAME=$(basename -- "$UEFI_SHELL_BINARY")
  UEFI_SHELL_SIZE=$(stat --format=%%s -- "$UEFI_SHELL_BINARY")
  ENROLLER_SIZE=$(stat --format=%%s -- "$ENROLLER_BINARY")
 
  # add 1MB then 10 percent for metadata
  UEFI_SHELL_IMAGE_KB=$((
    (UEFI_SHELL_SIZE + ENROLLER_SIZE + 1 * 1024 * 1024) * 11 / 10 / 1024
  ))
 
  # create non-partitioned FAT image
  rm -f -- "$UEFI_SHELL_IMAGE"
  mkdosfs -C "$UEFI_SHELL_IMAGE" -n UEFI_SHELL -- "$UEFI_SHELL_IMAGE_KB"
 
  # copy the shell binary into the FAT image
  export MTOOLS_SKIP_CHECK=1
  mmd   -i "$UEFI_SHELL_IMAGE"                       ::efi
  mmd   -i "$UEFI_SHELL_IMAGE"                       ::efi/boot
  mcopy -i "$UEFI_SHELL_IMAGE"  "$UEFI_SHELL_BINARY" ::efi/boot/bootx64.efi
  mcopy -i "$UEFI_SHELL_IMAGE"  "$ENROLLER_BINARY"   ::
  mdir  -i "$UEFI_SHELL_IMAGE"  -/                   ::
 
  # build ISO with FAT image file as El Torito EFI boot image
  xorrisofs -input-charset ASCII -J -rational-rock \
    -e "$UEFI_SHELL_IMAGE" -no-emul-boot \
    -o "$ISO_IMAGE" "$UEFI_SHELL_IMAGE"
}

# Build with neither SB nor SMM; include UEFI shell.
mkdir -p OVMF
build ${OVMF_2M_FLAGS} -a X64 -p OvmfPkg/OvmfPkgX64.dsc
cp -p Build/OvmfX64/*/FV/OVMF_CODE.fd OVMF/OVMF_CODE.fd
cp -p Build/OvmfX64/*/FV/OVMF_VARS.fd OVMF/OVMF_VARS.fd
# Build 4MB with neither SB nor SMM; include UEFI shell.
build ${OVMF_4M_FLAGS} -a X64 -p OvmfPkg/OvmfPkgX64.dsc
cp -p Build/OvmfX64/*/FV/OVMF_CODE.fd OVMF/OVMF_CODE_4M.fd
cp -p Build/OvmfX64/*/FV/OVMF_VARS.fd OVMF/OVMF_VARS_4M.fd
rm -rf Build/OvmfX64
# Build with SB and SMM; exclude UEFI shell.
build ${OVMF_2M_FLAGS} ${OVMF_SB_FLAGS} -a IA32 -a X64 -p OvmfPkg/OvmfPkgIa32X64.dsc
cp -p Build/Ovmf3264/*/FV/OVMF_CODE.fd OVMF/OVMF_CODE.secboot.fd
# Build 4MB with SB and SMM; exclude UEFI shell.
build ${OVMF_4M_FLAGS} ${OVMF_SB_FLAGS} -a IA32 -a X64 -p OvmfPkg/OvmfPkgIa32X64.dsc
cp -p Build/Ovmf3264/*/FV/OVMF_CODE.fd OVMF/OVMF_CODE_4M.secboot.fd
# Build AmdSev and IntelTdx variants
touch OvmfPkg/AmdSev/Grub/grub.efi   # dummy
build ${OVMF_2M_FLAGS} -a X64 -p OvmfPkg/AmdSev/AmdSevX64.dsc
cp -p Build/AmdSev/*/FV/OVMF.fd OVMF/OVMF.amdsev.fd
build ${OVMF_2M_FLAGS} -a X64 -p OvmfPkg/IntelTdx/IntelTdxX64.dsc
cp -p Build/IntelTdx/*/FV/OVMF.fd OVMF/OVMF.inteltdx.fd

# build shell
build ${OVMF_2M_FLAGS} -a X64 -p ShellPkg/ShellPkg.dsc

# build ovmf (x64) shell iso with EnrollDefaultKeys
#cp Build/Ovmf3264/*/X64/Shell.efi OVMF/
cp -p Build/Shell/*/X64/ShellPkg/Application/Shell/Shell/OUTPUT/Shell.efi OVMF/
cp -p Build/Ovmf3264/*/X64/EnrollDefaultKeys.efi OVMF/
build_iso OVMF

%if_disabled skip_enroll
virt-fw-vars --input OVMF/OVMF_VARS.fd \
             --output OVMF/OVMF_VARS.secboot.fd \
             --distro-keys alt --secure-boot

virt-fw-vars --input OVMF/OVMF_VARS.fd \
             --output OVMF/OVMF_VARS.ms.fd \
             --distro-keys windows --secure-boot

virt-fw-vars --input OVMF/OVMF_VARS_4M.fd \
             --output OVMF/OVMF_VARS_4M.secboot.fd \
             --distro-keys alt --secure-boot

virt-fw-vars --input OVMF/OVMF_VARS_4M.fd \
             --output OVMF/OVMF_VARS_4M.ms.fd \
             --distro-keys windows --secure-boot

%else
# This isn't going to actually give secureboot, but makes json files happy
# if we need to test disabling ovmf-vars-generator
cp -p OVMF/OVMF_VARS.fd OVMF/OVMF_VARS.secboot.fd
cp -p OVMF/OVMF_VARS.fd OVMF/OVMF_VARS.ms.fd
cp -p OVMF/OVMF_VARS_4M.fd OVMF/OVMF_VARS_4M.secboot.fd
cp -p OVMF/OVMF_VARS_4M.fd OVMF/OVMF_VARS_4M.ms.fd
%endif

# build microvm
build ${OVMF_2M_FLAGS} -a X64 -p OvmfPkg/Microvm/MicrovmX64.dsc
cp -p Build/MicrovmX64/*/FV/MICROVM.fd OVMF

# build ovmf-ia32
mkdir -p ovmf-ia32
build ${OVMF_2M_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc
cp -p Build/OvmfIa32/*/FV/OVMF_CODE.fd ovmf-ia32/
rm -rf Build/OvmfIa32
# build ovmf-ia32 with secure boot
build ${OVMF_2M_FLAGS} ${OVMF_SB_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc
cp -p Build/OvmfIa32/*/FV/OVMF_CODE.fd ovmf-ia32/OVMF_CODE.secboot.fd
# cp VARS files from from ovmf/, which are all we need
cp -p OVMF/OVMF_VARS*.fd ovmf-ia32/
# build ovmf-ia32 shell iso with EnrollDefaultKeys
build ${OVMF_2M_FLAGS} -a IA32 -p ShellPkg/ShellPkg.dsc
cp -p Build/Shell/*/IA32/ShellPkg/Application/Shell/Shell/OUTPUT/Shell.efi ovmf-ia32/Shell.efi
cp -p Build/OvmfIa32/*/IA32/EnrollDefaultKeys.efi ovmf-ia32/EnrollDefaultKeys.efi
build_iso ovmf-ia32

%install
# For distro-provided firmware packages, the specification
# (https://git.qemu.org/?p=qemu.git;a=blob;f=docs/interop/firmware.json)
# says the JSON "descriptor files" to be searched in this directory:
# `/usr/share/firmware/`.  Create it.
mkdir -p %buildroot%_datadir/qemu/firmware

# shell
mkdir -p %buildroot%_prefix/lib64/efi
cp -p Build/Shell/*/X64/ShellPkg/Application/Shell/Shell/OUTPUT/Shell.efi \
        %buildroot%_prefix/lib64/efi/shell.efi

#install OVMF
mkdir -p %buildroot%_datadir/edk2
cp -a OVMF %buildroot%_datadir/
ln -r -s %buildroot%_datadir/OVMF %buildroot%_datadir/edk2/ovmf

cp -a ovmf-ia32 %buildroot%_datadir/edk2/

for f in %_sourcedir/*edk2-ovmf*.json; do
    install -pm 644 $f %buildroot%_datadir/qemu/firmware
done

%check
%if_disabled skip_enroll
virt-fw-vars --input OVMF/OVMF_VARS.secboot.fd \
             --print | grep "SecureBootEnable.*ON"
%endif

%files ovmf
%doc OvmfPkg/License.txt
%_datadir/OVMF
%dir %_datadir/edk2
%_datadir/edk2/ovmf
%_datadir/qemu/firmware/*edk2-ovmf-x64*.json

%files ovmf-ia32
%doc OvmfPkg/License.txt
%_datadir/edk2/ovmf-ia32
%_datadir/qemu/firmware/*edk2-ovmf-ia32*.json

%files efi-shell
%_prefix/lib64/efi/shell.efi

%changelog
* Wed Nov 30 2022 Alexey Shabalin <shaba@altlinux.org> 20221117-alt1
- edk2-stable202211 (Fixes: CVE-2021-38578)
- add 4M builds

* Wed Aug 10 2022 Alexey Shabalin <shaba@altlinux.org> 20220526-alt1
- edk2-stable202205
- build with openssl-1.1.1q
- switch to virt-firmware for secure boot key enrollment
- add amdsev and inteltdx builds
- update BaseALT logo

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 20220221-alt1
- edk2-stable202202

* Tue Dec 28 2021 Alexey Shabalin <shaba@altlinux.org> 20211125-alt1
- edk2-stable202111

* Sat Feb 13 2021 Alexey Shabalin <shaba@altlinux.org> 20201127-alt2
- build with -b DEBUG

* Sun Jan 17 2021 Alexey Shabalin <shaba@altlinux.org> 20201127-alt1
- edk2-stable202011 (Fixes: CVE-2019-14584, CVE-2019-11098)

* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 20200229-alt1
- edk2-stable202002 (Fixes: CVE-2019-14575, CVE-2019-14559, CVE-2019-14587, CVE-2019-14558, CVE-2019-14586, CVE-2019-14563)

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 20191122-alt1
- edk2-stable201911 (Fixes: CVE-2019-14553, CVE-2019-13224, CVE-2019-13225)

* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt2
- build ovmf and efi-shell only

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
