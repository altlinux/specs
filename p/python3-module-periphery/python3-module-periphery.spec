%define  modulename periphery

Name:    python3-module-%modulename
Version: 1.1.1
Release: alt1

Summary: Library for peripheral I/O in Linux.
License: MIT
Group:   Development/Python3
URL:     https://github.com/vsergeev/python-periphery

Packager: Nikita Ermakov <arei@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
A pure Python 2/3 library for peripheral I/O
(GPIO, LED, PWM, SPI, I2C, MMIO, Serial) in Linux.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Tue Jun 25 2019 Nikita Ermakov <arei@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus.
