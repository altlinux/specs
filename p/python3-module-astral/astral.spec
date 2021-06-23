Name: python3-module-astral
Version: 2.2
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
%python3_sitelibdir/astral
%python3_sitelibdir/astral-%version-*-info

%changelog
* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt1
- initial
