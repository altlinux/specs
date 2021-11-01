Name: firmware-brcmfmac43456
Version: 1.0
Release: alt1
Summary: This file is needed to WiFi working on Paspberry Pi 400
License: LICENCE.cypress
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://github.com/RPi-Distro/firmware-nonfree/raw/master/brcm/
BuildArch: noarch
Source0: brcmfmac43456-sdio.txt
Source1: brcmfmac43456-sdio.bin
Source2: brcmfmac43456-sdio.clm_blob
Source3: LICENCE.broadcom_bcm43xx
Source4: LICENCE.cypress

%description
%summary

%install
%define fw_brcm /lib/firmware/brcm
%__install -d %buildroot%fw_brcm
%__install -m644 %SOURCE0 %buildroot%fw_brcm
%__install -m644 %SOURCE1 %buildroot%fw_brcm
%__install -m644 %SOURCE2 %buildroot%fw_brcm
%__install -d %buildroot/%_docdir/%name
%__install -m644 %SOURCE3 %buildroot/%_docdir/%name
%__install -m644 %SOURCE4 %buildroot/%_docdir/%name

%files
%fw_brcm/brcmfmac43456-sdio.txt
%fw_brcm/brcmfmac43456-sdio.bin
%fw_brcm/brcmfmac43456-sdio.clm_blob
%doc %_docdir/%name

%changelog
* Tue Jul 27 2021 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Initial build
