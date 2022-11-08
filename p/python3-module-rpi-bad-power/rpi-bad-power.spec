Name: python3-module-rpi-bad-power
Version: 0.1.0
Release: alt1

Summary: A Python library to detect bad power supply on Raspberry Pi
License: MIT
Group: Development/Python
Url: https://pypi.org/project/rpi-bad-power/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/rpi_bad_power
%python3_sitelibdir/rpi_bad_power-%version.dist-info

%changelog
* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.0-alt1
- 0.1.0 released

