Name: alsa-ucm-conf-pinephone-pro-workaround
Version: 0.1
Release: alt1

Summary: Workaround for enable sound on Pinephone Pro
License: BSD-3-Clause
Group: System/Libraries

Url: https://www.altlinux.org

ExclusiveArch: aarch64

Requires: alsa-ucm-conf

%description
%summary.

%install
mkdir -p %buildroot%_datadir/alsa/ucm2/conf.d/simple-card
ln -s ../../PinePhonePro/PINE64-PinePhonePro-.conf %buildroot%_datadir/alsa/ucm2/conf.d/simple-card/simple-card.conf

%files
%_datadir/alsa/ucm2/conf.d/simple-card/simple-card.conf

%changelog
* Fri Mar 22 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
