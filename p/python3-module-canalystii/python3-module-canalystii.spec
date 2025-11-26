%define  pypi_name canalystii
Name:    python3-module-%pypi_name
Version: 0.1
Release: alt1
Summary: Unofficial Python userspace driver for the low cost USB analyzer "Canalyst-II"
License: BSD-3-Clause
URL:     https://pypi.org/project/canalystii
VCS:     https://github.com/projectgus/python-canalystii
Source:  %name-%version.tar
Group:   Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Unofficial Python userspace driver for the low cost USB analyzer "Canalyst-II"
by Chuangxin Technology.
Uses pyusb library for USB support on Windows, MacOS and Linux.
This driver is based on black box reverse engineering of the USB behaviour of
the proprietary software, and reading the basic data structure layouts in
the original python-can canalystii source.
Intended for use as a backend driver for python-can.
However it can also be used standalone.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README* LICENSE
%python3_sitelibdir/canalystii
%python3_sitelibdir/canalystii-%version.dist-info

%changelog
* Fri Oct 24 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.1-alt1
- Initial build.
