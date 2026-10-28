%define _unpackaged_files_terminate_build 1

Name: alsa-ucm-conf-sm7125
Version: 1.2.13
Release: alt1

Summary: ALSA UCM configuration for Qualcomm sm7125 based devices
License: BSD-3-Clause
Group: System/Configuration/Hardware

URL: https://github.com/sm7125-mainline/alsa-ucm-conf
VCS: https://github.com/sm7125-mainline/alsa-ucm-conf.git

ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: alsa-ucm-conf

%description
ALSA Use Case Manager configuration files for Qualcomm sm7125 based devices

This package contains ALSA Use Case Manager configuration files needed to get
sound on any sm7125 based phone.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/alsa/ucm2/

cd ucm2/
cp -rv --parents \
  Qualcomm/sm8250/Qualcomm-RB5-WSA8815-Speakers-DMIC0.conf \
  Xiaomi/miatoll/miatoll.conf \
  conf.d/sm8250/Galaxy\ A52.conf \
  Samsung/a52q \
  %buildroot%_datadir/alsa/ucm2/

%files
%_datadir/alsa/ucm2

%changelog
* Thu Oct 22 2026 David Sultaniiazov <x1z53@altlinux.org> 1.2.13-alt1
- Initial build for ALT.
