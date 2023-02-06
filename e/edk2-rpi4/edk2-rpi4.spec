%global optflags_lto %nil

Name: edk2-rpi4
Version: 20220307
Release: alt1
Summary: Raspberry pi 4/400 UEFI firmware

License: BSD-2-Clause-Patent
Group: Emulators
Url: http://www.tianocore.org

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar
#Vcs-Git: https://github.com/tianocore/edk2-platforms.git
Source2: edk2-platforms.tar
#Vcs-Git: https://github.com/tianocore/edk2-non-osi.git
Source3: edk2-non-osi.tar
#Vcs-Git: https://github.com/openssl/openssl
Source4: openssl.tar
#Vcs-Git: https://github.com/ucb-bar/berkeley-softfloat-3.git
Source5: berkeley-softfloat-3.tar
#Vcs-Git: https://github.com/google/brotli.git
Source6: brotli.tar
Source99: config.txt.sample

ExclusiveArch: x86_64
BuildArch: noarch

BuildRequires: acpica 
BuildRequires: bc
BuildRequires: gcc10
BuildRequires: gcc10-c++
BuildRequires: gcc-aarch64-linux-gnu
BuildRequires: libuuid-devel
BuildRequires: python3 python3-base

%description
Raspberry pi 4B/400 UEFI firmware

%prep
%setup -cT
rm -rf Build

mkdir -p -m 755 edk2 edk2-platforms edk2-non-osi

tar -x -f %SOURCE0 --strip-components=1 -C edk2
find edk2/BaseTools/Source -type f -name '*.o' -or -name '*.d' -delete
rm -rf edk2/BaseTools/Source/C/bin
find edk2/BaseTools/Source/Python -type d -name '__pychache' -print0 | xargs -0 -r rm -rf

mkdir -p edk2/CryptoPkg/Library/OpensslLib/openssl
tar -x -f %SOURCE4 --strip-components=1 -C edk2/CryptoPkg/Library/OpensslLib/openssl
mkdir -p edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %SOURCE5 --strip-components=1 -C edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
mkdir -p edk2/BaseTools/Source/C/BrotliCompress/brotli
tar -xf %SOURCE6 --strip-components=1 -C edk2/BaseTools/Source/C/BrotliCompress/brotli
mkdir -p edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/brotli
# edk2 wants brotli sources in two different directories
tar -xf %SOURCE6 --strip-components=1 -C edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/brotli

tar -x -f %SOURCE2 --strip-components=1 -C edk2-platforms
tar -x -f %SOURCE3 --strip-components=1 -C edk2-non-osi

%build
export PYTHON_COMMAND=%__python3
export WORKSPACE=`pwd`
export PACKAGES_PATH=`pwd`/edk2:`pwd`/edk2-platforms:`pwd`/edk2-non-osi
export GCC5_AARCH64_PREFIX=aarch64-linux-gnu-
export BUILD_FLAGS="-D SECURE_BOOT_ENABLE=FALSE -D INCLUDE_TFTP_COMMAND=TRUE -D NETWORK_ISCSI_ENABLE=TRUE -D SMC_PCI_SUPPORT=1"

%make_build -C edk2/BaseTools BUILD_CC=gcc-10 BUILD_CXX=g++-10
source ./edk2/edksetup.sh

# Disable "secure" boot
# do NOT limit RAM to 3GB by default
# Use devicetree by default

build -a AARCH64 -t GCC5 -n %__nprocs -b RELEASE \
	-p edk2-platforms/Platform/RaspberryPi/RPi4/RPi4.dsc \
	--pcd gRaspberryPiTokenSpaceGuid.PcdRamMoreThan3GB=1 \
	--pcd gRaspberryPiTokenSpaceGuid.PcdRamLimitTo3GB=0 \
	--pcd gRaspberryPiTokenSpaceGuid.PcdSystemTableMode=2 \
	--pcd gEfiMdeModulePkgTokenSpaceGuid.PcdFirmwareVendor=L"https://basealt.ru" \
	--pcd gEfiMdeModulePkgTokenSpaceGuid.PcdFirmwareVersionString=L"UEFI Firmware %version" \
	${BUILD_FLAGS}

cp $WORKSPACE/Build/RPi4/RELEASE_GCC5/FV/RPI_EFI.fd RPI4_EFI.fd 

%install
mkdir -p %buildroot%_datadir/edk2/rpi4
install -pm 644 RPI4_EFI.fd %buildroot%_datadir/edk2/rpi4
cp -a %SOURCE99 %buildroot%_datadir/edk2/rpi4

%files
%_datadir/edk2/rpi4
%_datadir/edk2/rpi4/RPI4_EFI.fd
%_datadir/edk2/rpi4/config.txt.sample

%changelog
* Sun Dec 18 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 20220307-alt1
- Revived edk2-rpi4
- Linux friendly by default
- Use device tree as a system tables
- No stupid 3GB RAM limit
- No "secure" boot at all (yes, this is a feature)
