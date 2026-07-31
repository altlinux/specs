%define _unpackaged_files_terminate_build 1

Name: alsa-ucm-conf-sc7280
Version: 1.2.14
Release: alt1
Summary: ALSA UCM configuration for Qualcomm sc7280 based devices
License: BSD-3-Clause
Group: System/Configuration/Hardware
Url: https://github.com/sc7280-mainline/alsa-ucm-conf
VCS: https://github.com/sc7280-mainline/alsa-ucm-conf.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: alsa-ucm-conf

%description
ALSA Use Case Manager configuration files for Qualcomm sc7280 based devices

This package contains ALSA Use Case Manager configuration files needed to get
sound on any sc7280 based phone.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/alsa/ucm2/conf.d/sm8250/
mkdir -p %buildroot%_datadir/alsa/ucm2/codecs/wcd938x/
cp -rv ucm2/Nothing %buildroot%_datadir/alsa/ucm2
cp -v ucm2/conf.d/sm8250/NP1.conf %buildroot%_datadir/alsa/ucm2/conf.d/sm8250/
cp -v ucm2/codecs/wcd938x/AnalogMic2EnableSeq.conf %buildroot%_datadir/alsa/ucm2/codecs/wcd938x/AnalogMic2EnableSeq.conf
cp -v ucm2/codecs/wcd938x/AnalogMic2DisableSeq.conf %buildroot%_datadir/alsa/ucm2/codecs/wcd938x/AnalogMic2DisableSeq.conf

%files
%_datadir/alsa/ucm2

%changelog
* Thu Jul 09 2026 Vasiliy Doylov <neko@altlinux.org> 1.2.14-alt1
- Initial build for ALT.
