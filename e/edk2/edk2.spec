%define TOOL_CHAIN_TAG GCC49
%define openssl_ver 1.0.2g
%def_disable aarch64

# More subpackages to come once licensing issues are fixed
Name: edk2
Version: 20160518
Release: alt1
Summary: EFI Development Kit II

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

Source2: https://www.openssl.org/source/openssl-%openssl_ver.tar.gz

Patch1: %name-%version-%release.patch

License: BSD
Group: Emulators
Url: http://www.tianocore.org
BuildRequires: gcc-c++-x86_64-linux-gnu gcc-c++
%{?_enable_aarch64:BuildRequires: gcc-c++-aarch64-linux-gnu}
BuildRequires: iasl nasm
BuildRequires: python-devel python-modules-sqlite3
BuildRequires: libuuid-devel

%description
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.

%package tools
Summary: EFI Development Kit II Tools
Group: Emulators

%description tools
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package tools-python
Summary: EFI Development Kit II Tools
Group: Development/Python
BuildArch: noarch

%description tools-python
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.  You do not need to install this package;
you probably want to install edk2-tools only.

%package tools-doc
Summary: Documentation for EFI Development Kit II Tools
Group: Development/Documentation
BuildArch: noarch

%description tools-doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package ovmf
Summary: Open Virtual Machine Firmware
Group: Emulators
Requires: ipxe-roms-qemu
Requires: seavgabios
License: BSD License (no advertising) with restrictions on use and redistribution
BuildArch: noarch

%description ovmf
EFI Development Kit II
Open Virtual Machine Firmware

%prep
%setup -q
%patch1 -p1

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
	BaseTools/Source/Python/UPT/Dll/sqlite3.dll

# add openssl
tar -C CryptoPkg/Library/OpensslLib -xf %SOURCE2
(cd CryptoPkg/Library/OpensslLib/openssl-%openssl_ver;
 patch -p1 < ../EDKII_openssl-%openssl_ver.patch)
(cd CryptoPkg/Library/OpensslLib; ./Install.sh)

# fix build target.txt
sed -i \
	"s|^TOOL_CHAIN_TAG[ ]*=.*|TOOL_CHAIN_TAG = %TOOL_CHAIN_TAG|; \
	 s|^TARGET[ ]*=.*|TARGET = RELEASE|; \
	 s|^ACTIVE_PLATFORM[[ ]*=.*|ACTIVE_PLATFORM = MdeModulePkg/MdeModulePkg.dsc|; \
	 s|^TARGET_ARCH[ ]*=.*|TARGET_ARCH = IA32 X64|" \
	 BaseTools/Conf/target.template

sed -i \
	"s|^DEFINE UNIXGCC_X64_PETOOLS_PREFIX|DEFINE UNIXGCC_X64_PETOOLS_PREFIX = x86_64-linux-gnu-|; \
	 s|^DEFINE UNIXGCC_IA32_PETOOLS_PREFIX|DEFINE UNIXGCC_IA32_PETOOLS_PREFIX = x86_64-linux-gnu-|; \
	 s|DEF(GCC48_X64_PREFIX)make|make|; \
	 s|DEF(GCC48_IA32_PREFIX)make|make|; \
	 s|DEF(GCC49_X64_PREFIX)make|make|; \
	 s|DEF(GCC49_IA32_PREFIX)make|make|" \
	 BaseTools/Conf/tools_def.template

%build
export GCC49_BIN=x86_64-linux-gnu-
source ./edksetup.sh

# compiler
CC_FLAGS="-t GCC49"

# common features
#CC_FLAGS="${CC_FLAGS} -b DEBUG"
CC_FLAGS="${CC_FLAGS} -b RELEASE"
CC_FLAGS="${CC_FLAGS} --cmd-len=65536"

# ovmf features
OVMF_FLAGS="${CC_FLAGS}"
OVMF_FLAGS="${OVMF_FLAGS} -D HTTP_BOOT_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_IP6_ENABLE"

# ovmf + secure boot features
OVMF_SB_FLAGS="${OVMF_FLAGS}"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SECURE_BOOT_ENABLE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SMM_REQUIRE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D EXCLUDE_SHELL_FROM_FD"

# arm firmware features
ARM_FLAGS="-t GCC49 -b DEBUG --cmd-len=65536"
ARM_FLAGS="${ARM_FLAGS} -D DEBUG_PRINT_ERROR_LEVEL=0x8040004F"

# prepare
#cp /usr/share/seabios/bios-csm.bin OvmfPkg/Csm/Csm16/Csm16.bin
#cp /usr/share/seabios/bios-csm.bin corebootPkg/Csm/Csm16/Csm16.bin
%make \
	 -C BaseTools


#(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

#mkdir -p FatBinPkg/EnhancedFatDxe/{X64,Ia32}
#source ./edksetup.sh

# build ovmf
build ${OVMF_FLAGS} -a X64 -p OvmfPkg/OvmfPkgX64.dsc
#build ${OVMF_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc

# build ovmf with secure boot
build ${OVMF_SB_FLAGS} -a IA32 -a X64 -p OvmfPkg/OvmfPkgIa32X64.dsc

%if_enabled aarch64
# build arm/aarch64 firmware
export GCC49_AARCH64_PREFIX="aarch64-linux-gnu-"
mkdir -p aarch64
build ${ARM_FLAGS} -a AARCH64 -p ArmVirtPkg/ArmVirtQemu.dsc
cp Build/ArmVirtQemu-AARCH64/*/FV/*.fd aarch64
dd of="aarch64/QEMU_EFI-pflash.raw" if="/dev/zero" bs=1M count=64
dd of="aarch64/QEMU_EFI-pflash.raw" if="aarch64/QEMU_EFI.fd" conv=notrunc
dd of="aarch64/vars-template-pflash.raw" if="/dev/zero" bs=1M count=64
unset GCC49_AARCH64_PREFIX
%endif

%install
# install BaseTools
mkdir -p %buildroot%_bindir \
         %buildroot%_datadir/%name/Conf \
         %buildroot%_datadir/%name/Scripts

pushd BaseTools
install --strip \
	Source/C/bin/* \
	%buildroot%_bindir

ln -f %buildroot%_bindir/GnuGenBootSector \
	%buildroot%_bindir/GenBootSector

install \
	BinWrappers/PosixLike/LzmaF86Compress \
	%buildroot%_bindir

install \
	BuildEnv \
	%buildroot%_datadir/%name

install \
	Conf/*.template \
	%buildroot%_datadir/%name/Conf

install \
	Scripts/GccBase.lds \
	%buildroot%_datadir/%name/Scripts

cp -R Source/Python %buildroot%_datadir/%name/Python

find %buildroot%_datadir/%name/Python -name "*.pyd" | xargs rm -f

for i in BPDG Ecc GenDepex GenFds GenPatchPcdTable PatchPcdValue TargetTool Trim UPT; do
  echo '#!/bin/sh
PYTHONPATH=%_datadir/%name/Python
export PYTHONPATH
exec python '%_datadir/%name/Python/$i/$i.py' "$@"' > %buildroot%_bindir/$i
  chmod +x %buildroot%_bindir/$i
done

popd

#install OVMF
mkdir -p %buildroot%_datadir/OVMF
#install -D -m644 Build/OvmfIa32/*/FV/OVMF.fd %buildroot%_datadir/OVMF/ovmf-ia32/
#install -D -m644 Build/OvmfIa32/*/FV/OVMF_CODE.fd %buildroot%_datadir/OVMF/ovmf-ia32/
#install -D -m644 Build/OvmfIa32/*/FV/OVMF_VARS.fd %buildroot%_datadir/OVMF/ovmf-ia32/
install -D -m644 Build/OvmfX64/*/FV/OVMF.fd %buildroot%_datadir/OVMF/
install -D -m644 Build/OvmfX64/*/FV/OVMF_CODE.fd %buildroot%_datadir/OVMF/
install -D -m644 Build/OvmfX64/*/FV/OVMF_VARS.fd %buildroot%_datadir/OVMF/
install -D -m644 Build/Ovmf3264/*/FV/OVMF_CODE.fd %buildroot%_datadir/OVMF/OVMF_CODE.secboot.fd
%if_enabled aarch64
install -D -m644 Build/ArmVirtQemu-AARCH64/*/FV/QEMU_EFI.fd %buildroot%_datadir/AAVMF/
%endif

%files tools
%_bindir/BootSectImage
%_bindir/EfiLdrImage
%_bindir/EfiRom
%_bindir/GenBootSector
%_bindir/GenCrc32
%_bindir/GenFfs
%_bindir/GenFv
%_bindir/GenFw
%_bindir/GenPage
%_bindir/GenSec
%_bindir/GenVtf
%_bindir/GnuGenBootSector
%_bindir/LzmaCompress
%_bindir/LzmaF86Compress
%_bindir/Split
%_bindir/TianoCompress
%_bindir/VfrCompile
%_bindir/VolInfo
%_datadir/%name/BuildEnv
%_datadir/%name/Conf
%_datadir/%name/Scripts

#%files tools-python
#%_bindir/BPDG
#%_bindir/Ecc
#%_bindir/GenDepex
#%_bindir/GenFds
#%_bindir/GenPatchPcdTable
#%_bindir/PatchPcdValue
#%_bindir/TargetTool
#%_bindir/Trim
#%_bindir/UPT
#%_datadir/%name/Python/

%files tools-doc
%doc BaseTools/UserManuals/*.rtf

%files ovmf
#%doc FatBinPkg/License.txt
%doc OvmfPkg/License.txt
%_datadir/OVMF
%if_enabled aarch64
%_datadir/AAVMF/
%endif

%changelog
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
