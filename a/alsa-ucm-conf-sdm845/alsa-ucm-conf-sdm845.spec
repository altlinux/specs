%define _unpackaged_files_terminate_build 1

Name: alsa-ucm-conf-sdm845
Version: 1.2.10
Release: alt1
Summary: ALSA UCM configuration for Qualcomm sdm845 based devices
License: BSD-3-Clause
Group: System/Configuration/Hardware
Url: https://gitlab.com/sdm845-mainline/alsa-ucm-conf
VCS: https://gitlab.com/sdm845-mainline/alsa-ucm-conf.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: alsa-ucm-conf

%description
ALSA Use Case Manager configuration files for Qualcomm sdm845 based devices

This package contains ALSA Use Case Manager configuration files needed to get
sound on any sdm845 based phone.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/alsa/ucm2/conf.d/sdm845
mkdir -p %buildroot%_datadir/alsa/ucm2/Samsung
cp -rv ucm2/Google %buildroot%_datadir/alsa/ucm2
cp -rv ucm2/OnePlus %buildroot%_datadir/alsa/ucm2
cp -rv ucm2/Samsung/starqltechn %buildroot%_datadir/alsa/ucm2/Samsung
cp -rv ucm2/SHIFT %buildroot%_datadir/alsa/ucm2
cp -rv ucm2/Xiaomi %buildroot%_datadir/alsa/ucm2
cp -v ucm2/conf.d/sdm845/Google* %buildroot%_datadir/alsa/ucm2/conf.d/sdm845
cp -v ucm2/conf.d/sdm845/OnePlus* %buildroot%_datadir/alsa/ucm2/conf.d/sdm845
cp -v ucm2/conf.d/sdm845/oneplus* %buildroot%_datadir/alsa/ucm2/conf.d/sdm845
cp -v ucm2/conf.d/sdm845/Samsung* %buildroot%_datadir/alsa/ucm2/conf.d/sdm845
cp -v ucm2/conf.d/sdm845/SHIFT* %buildroot%_datadir/alsa/ucm2/conf.d/sdm845
cp -v ucm2/conf.d/sdm845/Xiaomi* %buildroot%_datadir/alsa/ucm2/conf.d/sdm845

%files
%_datadir/alsa/ucm2

%changelog
* Mon Apr 20 2026 Vasiliy Doylov <neko@altlinux.org> 1.2.10-alt1
- Initial package
