Name: mfgtools
Version: 1.5.179
Release: alt1

Summary: Freescale/NXP I.MX Chip image deploy tools
License: BSD
Group: System/Kernel and hardware

Url: https://github.com/nxp-imx/mfgtools
Source: %name.tar
Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Patch0: alt-avoid-gen_vers-call.patch
Patch1: allow-true-dynamic-linking-for-Linux-build.patch
Patch2: add-built-in-script-emmc_img-to-flash-image-to-eMMC-.patch
Patch3: alt-fix-progress-indicator.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: bzip2-devel zlib-devel libusb-devel libssl-devel libzstd-devel libtinyxml2-devel

Provides: uuu

%description
Freescale/NXP I.MX Chip image deploy tools:
- uuu (universal update utility)

%prep
%setup -n %name
#%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1

echo "%version" > .tarball-version

%ifarch %e2k
# unsupported as of lcc 1.23.20
sed -i 's,-no-pie,,' uuu/CMakeLists.txt
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

mkdir -p %buildroot%_udevrulesdir
# the rules below are produced by the tool itself: `uuu -udev`
cat <<EOT >> %buildroot%_udevrulesdir/99-uuu.rules
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="012f", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0129", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0147", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="004f", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="013e", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0146", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="014a", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="014b", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="014e", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0159", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="015d", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0076", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0054", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0061", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0063", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0071", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="007d", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="15a2", ATTRS{idProduct}=="0080", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0128", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0126", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0135", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0134", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="012b", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="b4a4", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="b4a4", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0151", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="b4a4", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="3016", ATTRS{idProduct}=="1001", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="3016", ATTRS{idProduct}=="1001", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="066f", ATTRS{idProduct}=="9afe", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="066f", ATTRS{idProduct}=="9bff", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0153", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0525", ATTRS{idProduct}=="a4a5", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="18d1", ATTRS{idProduct}=="0d02", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="3016", ATTRS{idProduct}=="0001", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0152", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="0afb", TAG+="uaccess"
EOT

%files
%_bindir/*
%_udevrulesdir/*

%changelog
* Wed Apr 24 2024 Pavel Nakonechnyi <zorg@altlinux.org> 1.5.179-alt1
- updated to 1.5.179

* Sun Jun 25 2023 Pavel Nakonechnyi <zorg@altlinux.org> 1.5.109-alt1
- updated to 1.5.109

* Sun Apr 09 2023 Pavel Nakonechnyi <zorg@altlinux.org> 1.5.21-alt1
- updated to 1.5.21

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.4.43-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Oct 29 2020 Pavel Nakonechnyi <zorg@altlinux.org> 1.4.43-alt1
- updated to 1.4.43

* Mon Dec 30 2019 Michael Shigorin <mike@altlinux.org> 1.3.124-alt2
- E2K: avoid lcc-unsupported option
- minor spec cleanup

* Wed Dec 25 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.124-alt1
- updated to 1.3.124

* Mon Jun 17 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.135-alt1
- initial build for Sisyphus
