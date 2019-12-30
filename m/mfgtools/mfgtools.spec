Name: mfgtools
Version: 1.3.124
Release: alt2

Summary: Freescale/NXP I.MX Chip image deploy tools
License: BSD
Group: System/Kernel and hardware

Url: https://github.com/NXPmicro/mfgtools
Source: %name.tar
Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Patch0: alt-avoid-gen_vers-call.patch
Patch1: allow-true-dynamic-linking-for-Linux-build.patch
Patch2: add-built-in-script-emmc_img-to-flash-image-to-eMMC-.patch
Patch3: alt-fix-progress-indicator.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libzip-devel bzip2-devel zlib-devel libusb-devel libssl-devel

Provides: uuu

%description
Freescale/NXP I.MX Chip image deploy tools:
- uuu (universal update utility)

%prep
%setup -n %name
%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1

mkdir -p libuuu/gen
echo "#define GIT_VERSION \"lib%version\"" > libuuu/gen/gitversion.h

%ifarch %e2k
# unsupported as of lcc 1.23.20
sed -i 's,-no-pie,,' uuu/CMakeLists.txt
%endif

%build
%cmake
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

mkdir -p %buildroot%_sysconfdir/udev/rules.d/
cat <<EOT >> %buildroot%_sysconfdir/udev/rules.d/99-uuu.rules
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="012f", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0129", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="004f", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="013e", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0076", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0054", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0061", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0063", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0071", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="007d", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0080", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0128", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0126", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0135", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0134", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="012b", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="b4a4", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="b4a4", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="b4a4", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="066f", ATTRS{idProduct}=="9afe", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="066f", ATTRS{idProduct}=="9bff", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="a4a5", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="18d1", ATTRS{idProduct}=="0d02", MODE="0666"
EOT

%files
%_bindir/*
%_sysconfdir/udev/rules.d/*

%changelog
* Mon Dec 30 2019 Michael Shigorin <mike@altlinux.org> 1.3.124-alt2
- E2K: avoid lcc-unsupported option
- minor spec cleanup

* Wed Dec 25 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.124-alt1
- updated to 1.3.124

* Mon Jun 17 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.135-alt1
- initial build for Sisyphus
