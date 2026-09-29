Name: python3-module-luma-oled
Version: 3.15.0
Release: alt1

Summary: Small OLED display library
License: MIT
Group: Development/Python
URL: https://pypi.org/project/luma.oled
VCS: https://github.com/rm-hull/luma.oled

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
Python 3 library interfacing OLED matrix displays with the SSD1306, SSD1309,
SSD1322, SSD1325, SSD1327, SSD1331, SSD1351, SH1106 or WS0010 driver
using I2C/SPI/Parallel on any linux-based single-board computer.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/luma
%python3_sitelibdir/luma_oled-%version.dist-info

%changelog
* Tue Sep 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.15.0-alt1
- 3.15.0 released

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- 3.10.0 released
