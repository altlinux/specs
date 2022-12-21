Name: python3-module-smbus2
Version: 0.4.2
Release: alt1

Summary: Python implementation of of the python-smbus package
License: MIT
Group: Development/Python
Url: https://pypi.org/project/smbus2/

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary
smbus2 is drop-in replacement of lm-sensors smbus package

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/smbus2
%python3_sitelibdir/smbus2-%version.dist-info

%changelog
* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released

