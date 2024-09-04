%define TOOL_CHAIN_TAG GCC5

# More subpackages to come once licensing issues are fixed
Name: edk2-tools
Version: 20240811
Release: alt1
Summary: EFI Development Kit II Tools

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

Source2: openssl.tar
Source3: berkeley-softfloat-3.tar
Source4: Logo.bmp

Patch1: %name-%version.patch

License: BSD-2-Clause-Patent
Group: Emulators
Url: http://www.tianocore.org

ExclusiveArch:  %ix86 x86_64 %arm aarch64 loongarch64

BuildRequires(pre): rpm-build-python3
BuildRequires: iasl nasm gcc-c++
BuildRequires: python3-devel python3-modules-sqlite3
BuildRequires: libuuid-devel
BuildRequires: bc

%description
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package python
Summary: EFI Development Kit II Tools
Group: Development/Python3
BuildArch: noarch

%description python
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.  You do not need to install this package;
you probably want to install edk2-tools only.

%package doc
Summary: Documentation for EFI Development Kit II Tools
Group: Development/Documentation
BuildArch: noarch

%description doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

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

# add /berkeley-softfloat-3
mkdir -p ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %SOURCE3 --strip-components 1 --directory ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3

%build
export PYTHON_COMMAND=%__python3
source ./edksetup.sh

# compiler
CC_FLAGS="-t %TOOL_CHAIN_TAG"

# common features
#CC_FLAGS="${CC_FLAGS} --cmd-len=65536 -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} -b RELEASE"
#CC_FLAGS="${CC_FLAGS} -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} --cmd-len=65536"
ARM_FLAGS="${CC_FLAGS}"

unset MAKEFLAGS

%make_build \
        -C BaseTools

%install
# install BaseTools
mkdir -p %buildroot%_bindir \
         %buildroot%_datadir/edk2/Conf \
         %buildroot%_datadir/edk2/Scripts

pushd BaseTools
install \
        Source/C/bin/* \
        %buildroot%_bindir

install \
        BinWrappers/PosixLike/LzmaF86Compress \
        %buildroot%_bindir

install \
        BuildEnv \
        %buildroot%_datadir/edk2

install \
        Conf/*.template \
        %buildroot%_datadir/edk2/Conf

install \
        Scripts/GccBase.lds \
        %buildroot%_datadir/edk2/Scripts

cp -R Source/Python %buildroot%_datadir/edk2/Python

find %buildroot%_datadir/edk2/Python -name "*.pyd" | xargs rm -f

for i in BPDG Ecc GenDepex GenFds GenPatchPcdTable PatchPcdValue TargetTool Trim UPT; do
  echo '#!/bin/sh
export PYTHONPATH=%_datadir/edk2/Python
exec python3 '%_datadir/edk2/Python/$i/$i.py' "$@"' > %buildroot%_bindir/$i
  chmod +x %buildroot%_bindir/$i
done

popd

%files
%_bindir/DevicePath
%_bindir/EfiRom
%_bindir/GenCrc32
%_bindir/GenFfs
%_bindir/GenFv
%_bindir/GenFw
%_bindir/GenSec
%_bindir/LzmaCompress
%_bindir/LzmaF86Compress
%_bindir/TianoCompress
%_bindir/VfrCompile
%_bindir/VolInfo
%_datadir/edk2/BuildEnv
%_datadir/edk2/Conf
%_datadir/edk2/Scripts

%files python
%_bindir/BPDG
%_bindir/Ecc
%_bindir/GenDepex
%_bindir/GenFds
%_bindir/GenPatchPcdTable
%_bindir/PatchPcdValue
%_bindir/TargetTool
%_bindir/Trim
%_bindir/UPT
%_datadir/edk2/Python/

%files doc
%doc BaseTools/UserManuals/*.rtf

%changelog
* Wed Sep 04 2024 Alexey Shabalin <shaba@altlinux.org> 20240811-alt1
- edk2-stable202408

* Thu Jul 25 2024 Alexey Shabalin <shaba@altlinux.org> 20240524-alt1
- edk2-stable202405

* Thu Jan 25 2024 Alexey Shabalin <shaba@altlinux.org> 20231115-alt1
- edk2-stable202311

* Mon Oct 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20221117-alt2
- NMU: build on LoongArch

* Wed Nov 30 2022 Alexey Shabalin <shaba@altlinux.org> 20221117-alt1
- edk2-stable202211 (Fixes: CVE-2021-38578)

* Thu Aug 11 2022 Alexey Shabalin <shaba@altlinux.org> 20220526-alt1
- edk2-stable202205
- update BaseALT logo

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 20220221-alt1
- edk2-stable202202

* Tue Dec 28 2021 Alexey Shabalin <shaba@altlinux.org> 20211125-alt1
- edk2-stable202111

* Wed Dec 23 2020 Alexey Shabalin <shaba@altlinux.org> 20201127-alt1
- edk2-stable202011 (Fixes: CVE-2019-14584, CVE-2019-11098)

* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 20200229-alt1
- edk2-stable202002 (Fixes: CVE-2019-14575, CVE-2019-14559, CVE-2019-14587, CVE-2019-14558, CVE-2019-14586, CVE-2019-14563)

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 20191122-alt1
- edk2-stable201911 (Fixes: CVE-2019-14553, CVE-2019-13224, CVE-2019-13225)

* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt2
- build as edk2-tools package

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
