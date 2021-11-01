Name: firmware-bcm4345
Version: 3.0
Release: alt1
Summary: Firmware bluetooth and WiFi for Paspberry Pi 4 and 400
License: LICENCE.cypress
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://github.com/RPi-Distro/
BuildArch: noarch
Source0: BCM4345C0.hcd
Source1: BCM4345C5.hcd
Source2: brcmfmac43456-sdio.txt
Source3: brcmfmac43456-sdio.bin
Source4: brcmfmac43456-sdio.clm_blob
Source5: LICENCE.cypress
Source6: LICENCE.broadcom_bcm43xx

%description
%summary

%install
%define bt_rpi4 /lib/firmware/brcm
%__install -d %buildroot%bt_rpi4
%__install -m644 %SOURCE0 %buildroot%bt_rpi4
%__install -m644 %SOURCE1 %buildroot%bt_rpi4
%__install -m644 %SOURCE2 %buildroot%bt_rpi4
%__install -m644 %SOURCE3 %buildroot%bt_rpi4
%__install -m644 %SOURCE4 %buildroot%bt_rpi4
%__install -d %buildroot/%_docdir/%name
%__install -m644 %SOURCE5 %buildroot/%_docdir/%name
%__install -m644 %SOURCE6 %buildroot/%_docdir/%name

%files
%bt_rpi4/BCM4345C0.hcd
%bt_rpi4/BCM4345C5.hcd
%bt_rpi4/brcmfmac43456-sdio.txt
%bt_rpi4/brcmfmac43456-sdio.bin
%bt_rpi4/brcmfmac43456-sdio.clm_blob
%doc %_docdir/%name

%changelog
* Mon Nov 01 2021 Dmitry Terekhin <jqt4@altlinux.org> 3.0-alt1
- Add BCM4345C5.hcd for RPi400
  from https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/
- Add brcmfmac43456-sdio.* for RPi400
  from https://github.com/RPi-Distro/firmware-nonfree/raw/master/brcm/
- Update LICENCEs from https://github.com/RPi-Distro/firmware-nonfree
  as in package linux-firmware-raspi2 in Ubuntu
  https://packages.ubuntu.com/impish/arm64/linux-firmware-raspi2/filelist

* Wed Feb 24 2021 Dmitry Terekhin <jqt4@altlinux.org> 2.0-alt1
- Firmware updated

* Fri Mar 27 2020 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Initial build
