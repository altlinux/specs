%define SVNDATE 20150616
%define SVNREV 17642
%define TOOL_CHAIN_TAG GCC48

# More subpackages to come once licensing issues are fixed
Name: edk2
Version: %{SVNDATE}svn%{SVNREV}
Release: alt2
Summary: EFI Development Kit II

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

#Vcs-Git: https://github.com/tianocore/edk2-FatPkg.git
Source1: FatPkg.tar

Source2: https://www.openssl.org/source/openssl-1.0.2c.tar.gz

License: BSD
Group: Emulators
Url: http://www.tianocore.org

BuildRequires: gcc-c++-x86_64-linux-gnu gcc4.8-c++
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
(cd CryptoPkg/Library/OpensslLib/openssl-1.0.2c;
 patch -p0 < ../EDKII_openssl-1.0.2c.patch)
(cd CryptoPkg/Library/OpensslLib; ./Install.sh)

# add fat
tar -xf %SOURCE1

# fix build target.txt
sed -i \
	"s|^TARGET[ ]*=.*|TARGET = RELEASE|; \
	 s|^TOOL_CHAIN_TAG[ ]*=.*|TOOL_CHAIN_TAG = %TOOL_CHAIN_TAG|; \
	 s|^TARGET_ARCH[ ]*=.*|TARGET_ARCH = IA32 X64|; \
	 s|^ACTIVE_PLATFORM[[ ]*=.*|ACTIVE_PLATFORM = MdeModulePkg/MdeModulePkg.dsc|" \
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
export GCC48_BIN=x86_64-linux-gnu-
source ./edksetup.sh
# prepare
#cp /usr/share/seabios/bios-csm.bin OvmfPkg/Csm/Csm16/Csm16.bin
#cp /usr/share/seabios/bios-csm.bin corebootPkg/Csm/Csm16/Csm16.bin
%make \
	 -C BaseTools


(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

#source ./edksetup.sh
#%ifarch x86_64
build -p FatPkg/FatPkg.dsc -m FatPkg/EnhancedFatDxe/Fat.inf -b RELEASE -a X64
#%endif
build -p FatPkg/FatPkg.dsc -m FatPkg/EnhancedFatDxe/Fat.inf -b RELEASE -a IA32
mkdir -p FatBinPkg/EnhancedFatDxe/{X64,Ia32}
#%ifarch x86_64
cp -a Build/Fat/RELEASE_%{TOOL_CHAIN_TAG}/X64/Fat.efi FatBinPkg/EnhancedFatDxe/X64/Fat.efi
#%endif
cp -a Build/Fat/RELEASE_%{TOOL_CHAIN_TAG}/IA32/Fat.efi FatBinPkg/EnhancedFatDxe/Ia32/Fat.efi
#%ifarch x86_64
build -p OvmfPkg/OvmfPkgX64.dsc -D BUILD_NEW_SHELL -D SECURE_BOOT_ENABLE=TRUE -D FD_SIZE_2MB -b RELEASE -a X64
#%endif
build -p OvmfPkg/OvmfPkgIa32.dsc -D BUILD_NEW_SHELL -D SECURE_BOOT_ENABLE=TRUE -D FD_SIZE_2MB -b RELEASE -a IA32

%install
# install BaseTools
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name/Conf
mkdir -p %buildroot%_datadir/%name/Scripts

pushd BaseTools
install --strip \
	Source/C/bin/BootSectImage \
	Source/C/bin/EfiLdrImage \
	Source/C/bin/EfiRom \
	Source/C/bin/GenCrc32 \
	Source/C/bin/GenFfs \
	Source/C/bin/GenFv \
	Source/C/bin/GenFw \
	Source/C/bin/GenPage \
	Source/C/bin/GenSec \
	Source/C/bin/GenVtf \
	Source/C/bin/GnuGenBootSector \
	Source/C/bin/LzmaCompress \
	Source/C/bin/Split \
	Source/C/bin/TianoCompress \
	Source/C/bin/VfrCompile \
	Source/C/bin/VolInfo \
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
	Conf/build_rule.template \
	Conf/tools_def.template \
	Conf/target.template \
	%buildroot%_datadir/%name/Conf

install \
	Scripts/gcc4.9-ld-script \
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
mkdir -p %buildroot%_datadir/ovmf
install -D -m644 Build/OvmfIa32/RELEASE_%{TOOL_CHAIN_TAG}/FV/OVMF.fd %buildroot%_datadir/ovmf/ovmf-ia32.bin
install -D -m644 Build/OvmfIa32/RELEASE_%{TOOL_CHAIN_TAG}/FV/OVMF_CODE.fd %buildroot%_datadir/ovmf/ovmf_code-ia32.bin
install -D -m644 Build/OvmfIa32/RELEASE_%{TOOL_CHAIN_TAG}/FV/OVMF_VARS.fd %buildroot%_datadir/ovmf/ovmf_vars-ia32.bin
#%ifarch x86_64
install -D -m644 Build/OvmfX64/RELEASE_%{TOOL_CHAIN_TAG}/FV/OVMF.fd %buildroot%_datadir/ovmf/ovmf-x64.bin
install -D -m644 Build/OvmfX64/RELEASE_%{TOOL_CHAIN_TAG}/FV/OVMF_CODE.fd %buildroot%_datadir/ovmf/ovmf_code-x64.bin
install -D -m644 Build/OvmfX64/RELEASE_%{TOOL_CHAIN_TAG}/FV/OVMF_VARS.fd %buildroot%_datadir/ovmf/ovmf_vars-x64.bin
#%endif

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
%_datadir/ovmf/*

%changelog
* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt2
- buils ovmf as noarch

* Wed Jun 17 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt1
- svn snapshot r17642
- add ovmf package

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 20140722svn2674-alt1
- svn snapshot r2674

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1.svn2594
- initial build
