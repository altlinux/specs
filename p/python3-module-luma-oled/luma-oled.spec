Name: python3-module-luma-oled
Version: 3.10.0
Release: alt1

Summary: Small OLED display library
License: MIT
Group: Development/Python
Url: https://pypi.org/project/luma.oled/

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Python 3 library interfacing OLED matrix displays with the SSD1306, SSD1309,
SSD1322, SSD1325, SSD1327, SSD1331, SSD1351, SH1106 or WS0010 driver
using I2C/SPI/Parallel on any linux-based single-board computer.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/luma
%python3_sitelibdir/luma.oled-%version.dist-info

%changelog
* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- 3.10.0 released

