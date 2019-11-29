Name: python3-module-astral
Version: 1.10.1
Release: alt1

Summary: Python calculations for the position of the sun and moon.
License: APL
Group: Development/Python
Url: https://pypi.org/project/astral/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
This is astral -- a Python module which calculates:
* times for various positions of the sun: dawn, sunrise, solar noon, sunset,
  dusk, solar elevation, solar azimuth and rahukaalam.
* the phase of the moon.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/astral.py
%python3_sitelibdir/astral-%version-*-info
%python3_sitelibdir/__pycache__/astral.*

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt1
- initial
