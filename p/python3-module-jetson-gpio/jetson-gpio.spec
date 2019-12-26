Name: python3-module-jetson-gpio
Version: 2.0.4
Release: alt1.20191217

Summary: A Python 3 library that enables the use of Jetson's GPIOs
License: MIT
Group: Development/Python3

Url: https://github.com/NVIDIA/jetson-gpio

ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

Requires: jetson-gpio-udev-rules = %EVR
Conflicts: python3-module-rpi-gpio

%description
%summary

%package -n jetson-gpio-udev-rules
Summary: udev rules for using GPIOs on Nvidia Jetson's
Group: System/Configuration/Hardware

%description -n jetson-gpio-udev-rules
udev rules for using GPIOs on Nvidia Jetson's

%prep
%setup
# fix python shebangs
find samples/ -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%__python3|' {} \;

%build
%python3_build

%install
%python3_install
install -pD -m 0644 debian/jetson-gpio-common.udev \
  %buildroot%_udevrulesdir/99-gpio-jetson.rules

%post
groupadd -f -r gpio

%files
%doc README.md samples
%python3_sitelibdir_noarch/Jetson
%python3_sitelibdir_noarch/RPi
%python3_sitelibdir_noarch/*.egg-info

%files -n jetson-gpio-udev-rules
%_udevrulesdir/99-gpio-jetson.rules

%changelog
* Thu Dec 26 2019 Anton Midyukov <antohami@altlinux.org> 2.0.4-alt1.20191217
- Initial build
