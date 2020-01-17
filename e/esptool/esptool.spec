Name: esptool
Version: 2.8
Release: alt1

Summary: Flasher for Espressif ESP8266 & ESP32 chips
License: GPLv2
Group: Development/Other
Url: https://github.com/espressif/esptool

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

Source: %name-%version-%release.tar

%description
A Python-based, open source, platform independent, utility to communicate with
the ROM bootloader in Espressif ESP8266 & ESP32 chips.

%prep
%setup

%build
%python3_build

%install
%python3_install
PYS=%buildroot%python3_sitelibdir/*.py
sed -ri '/env python$/ s,$,3,' $PYS; chmod 0755 $PYS
for f in $PYS; do
	F=${f##*/}; ln -srv $f %buildroot%_bindir/${F%*.py}
done
rm -vf %buildroot%_bindir/*.py

%set_python3_req_method strict

%files
%doc LICENSE README.md
%_bindir/espefuse
%_bindir/espsecure
%_bindir/esptool
%python3_sitelibdir/*.py
%python3_sitelibdir/esptool-%version-*-info

%changelog
* Sat Nov 09 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8-alt1
- initial
