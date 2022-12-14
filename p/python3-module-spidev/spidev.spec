Name: python3-module-spidev
Version: 3.6
Release: alt1

Summary: Python SPI devices Extension
License: MIT
Group: Development/Python
Url: https://pypi.org/project/spidev/

Source0: %name-%version-%release.tar

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
%python3_sitelibdir/spidev.*.so
%python3_sitelibdir/spidev-%version.dist-info

%changelog
* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.6-alt1
- initial

