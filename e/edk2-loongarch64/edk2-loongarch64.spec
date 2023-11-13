%global optflags_lto %nil

# More subpackages to come once licensing issues are fixed
Name: edk2-loongarch64
Version: 202308
Release: alt1
Summary: UEFI firmware for loongarch virtual machines

License: BSD-2-Clause-Patent
Group: Emulators
Url: http://www.tianocore.org

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: edk2.tar
#Vcs-Git: https://github.com/tianocore/edk2-platforms.git
Source2: edk2-platforms.tar
#Vcs-Git: https://github.com/tianocore/edk2-non-osi.git
Source3: edk2-non-osi.tar
Source4: 80-edk2-loongarch64.json

Patch1: 0001-BaseTools-GenFw-Add-support-for-LOONGARCH64-relax-re.patch

ExclusiveArch: x86_64 loongarch64
BuildArch: noarch

BuildRequires: acpica
BuildRequires: bc
BuildRequires: gcc
BuildRequires: gcc-c++
%if %_build_cpu != loongarch64
BuildRequires: gcc-loongarch64-linux-gnu
%endif
BuildRequires: libuuid-devel
BuildRequires: python3 python3-base

%description
UEFI firmware for LoongArch virtual machines

%prep
%setup -cT
rm -rf Build
find edk2/BaseTools/Source -type f -name '*.o' -or -name '*.d' -delete 2>/dev/null || :
rm -rf edk2/BaseTools/Source/C/bin
find edk2/BaseTools/Source/Python -type d -name '__pycache__' -print0 2>/dev/null | xargs -0 -r rm -rf

mkdir -p -m 755 edk2 edk2-platforms edk2-non-osi
mkdir -p edk2/Conf

tar -x -f %SOURCE0 --strip-components=1 -C edk2
tar -x -f %SOURCE2 --strip-components=1 -C edk2-platforms
tar -x -f %SOURCE3 --strip-components=1 -C edk2-non-osi

cd edk2
%patch1 -p1
cd ..

%build
export PYTHON_COMMAND=%__python3
export WORKSPACE=`pwd`
export PACKAGES_PATH=`pwd`/edk2:`pwd`/edk2-platforms:`pwd`/edk2-non-osi
%if %_build_cpu != loongarch64
export GCC5_LOONGARCH64_PREFIX=loongarch64-linux-gnu-
%endif

source ./edk2/edksetup.sh
make -C edk2/BaseTools

build \
	--arch=LOONGARCH64 \
	--platform=edk2-platforms/Platform/Loongson/LoongArchQemuPkg/Loongson.dsc \
	--tagname=GCC5 \
	--buildtarget=DEBUG \
	-n %__nprocs \
	--pcd gEfiMdeModulePkgTokenSpaceGuid.PcdFirmwareVendor=L"https://basealt.ru" \
	--pcd gEfiMdeModulePkgTokenSpaceGuid.PcdFirmwareVersionString=L"UEFI Firmware %version" \
	%nil

%install
mkdir -p %buildroot%_datadir/LA64VMF
install -pm 644 -t %buildroot%_datadir/LA64VMF Build/LoongArchQemu/DEBUG_GCC5/FV/QEMU_EFI.fd
install -pm 644 -t %buildroot%_datadir/LA64VMF Build/LoongArchQemu/DEBUG_GCC5/FV/QEMU_VARS.fd
mkdir -p %buildroot%_datadir/qemu/firmware
install -pm 644 -t %buildroot%_datadir/qemu/firmware %SOURCE4

%files
%_datadir/LA64VMF/QEMU_EFI.fd
%_datadir/LA64VMF/QEMU_VARS.fd
%_datadir/qemu/firmware/*edk2-loongarch*.json

%changelog
* Mon Nov 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 202308-alt1
- Initial build
