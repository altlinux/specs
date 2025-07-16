
%global target_arch loongarch64

%if %target_arch == loongarch64
%global efi_target LOONGARCH64
%global efi_platform OvmfPkg/LoongArchVirt/LoongArchVirtQemu.dsc
%global install_dir %_datadir/LA64VMF
%endif
%global efi_platform_name %(basename %efi_platform .dsc)

%global optflags_lto %nil

# More subpackages to come once licensing issues are fixed
Name: edk2-%target_arch
Version: 20250521
Release: alt1
Summary: UEFI firmware for %target_arch virtual machines

License: BSD-2-Clause-Patent
Group: Emulators
Url: http://www.tianocore.org

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: edk2.tar
Source1: 80-edk2-loongarch64.json


Source10: openssl-snapshot.tar
Source11: pylibfdt-snapshot.tar

Source100: Alt_linux_logo.bmp

# https://github.com/tianocore/edk2/pull/11309
Patch1: edk2-alt-sata-for-loongarchvirt.patch

# one primary architecture should be enough
ExcludeArch: aarch64 %ix86
BuildArch: noarch

BuildRequires: gcc
BuildRequires: gcc-c++
%if %_build_cpu != %target_arch
BuildRequires: gcc-%target_arch-linux-gnu
%endif
BuildRequires: libuuid-devel
BuildRequires: python3 python3-base

%description
EFI Development Kit II.

UEFI firmware for %target_arch virtual machines.

%prep
%setup -c
pushd edk2

# replace the boot logo
cp -f "%SOURCE100" MdeModulePkg/Logo/Logo.bmp

# don't build BrotliCompress
sed -i '/BrotliCompress/d' BaseTools/Source/C/GNUmakefile

tar --strip-components=1 -xf %SOURCE10 -C CryptoPkg/Library/OpensslLib/openssl
tar --strip-components=1 -xf %SOURCE11 -C MdePkg/Library/BaseFdtLib/libfdt

# now we can patch anything
%autopatch -p1

# include paths pointing to unused submodules
mkdir -p MdePkg/Library/MipiSysTLib/mipisyst/library/include
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/include
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/include/mbedtls
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/library
mkdir -p SecurityPkg/DeviceSecurity/SpdmLib/libspdm/include
mkdir -p Library/BrotliCustomDecompressLib/brotli/c/include
popd

%build
export PYTHON_COMMAND=%__python3
export WORKSPACE=`pwd`
export PACKAGES_PATH=$WORKSPACE/edk2
export EDK_TOOLS_PATH=$WORKSPACE/edk2/BaseTools
export EXTRA_OPTFLAGS="%optflags"
%if %_build_cpu != %target_arch
export GCC5_%{efi_target}_PREFIX='%target_arch-linux-gnu-'
%endif

make -C edk2/BaseTools

source ./edk2/edksetup.sh

build \
    --arch=%efi_target \
    --platform=%efi_platform \
    --tagname=GCC5 \
    --buildtarget=DEBUG \
    -n %__nprocs \
    --pcd gEfiMdeModulePkgTokenSpaceGuid.PcdFirmwareVendor=L"https://www.altlinux.org" \
    --pcd gEfiMdeModulePkgTokenSpaceGuid.PcdFirmwareVersionString=L"%EVR" \
    %nil


%install
mkdir -p %buildroot%install_dir
install -pm 644 -t %buildroot%install_dir \
    Build/%efi_platform_name/DEBUG_GCC5/FV/*.fd

mkdir -p %buildroot%_datadir/qemu/firmware
for f in %_sourcedir/*edk2-%{target_arch}*.json; do
    install -pm 644 $f %buildroot%_datadir/qemu/firmware
done

%files
%install_dir
%_datadir/qemu/firmware/*edk2-%{target_arch}*.json

%changelog
* Wed Jul 16 2025 Ivan A. Melnikov <iv@altlinux.org> 20250521-alt1
- edk2-stable202505;
- build virt platform from the main edk2 repo;
- replace tianocore logo with ALT Linux Team logo;
- enable SATA support (it boots from SATA CD-ROMs now).

* Thu Nov 21 2024 Ivan A. Melnikov <iv@altlinux.org> 20240430-alt2
- make sure firmwire sizes are multiples of 256 Kb,
  as required by qemu 9.1.0+

* Thu May 02 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 20240430-alt1
- edk2 stable20402-231-g0c74aa2073 (commit 0c74aa2073e48b21)
- edk2-platforms commit 73cfdc4afff3e641:
  + Support loading UEFI code from flash (like other architectures do).
    Note: qemu commit c6e9847fc4becba5 is required to actually load UEFI
    from a (virtual) flash device.
- edk2-non-osi commit 054cacf8819f82c9
- spec:
  + dropped GenFW patch (applied upstream)

* Mon Nov 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 202308-alt1
- Initial build
