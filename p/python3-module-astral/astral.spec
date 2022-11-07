Name: python3-module-astral
Version: 3.2
Release: alt1

Summary: Python calculations for the position of the sun and moon.
License: APL
Group: Development/Python
Url: https://pypi.org/project/astral/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
This is astral -- a Python module which calculates:
* times for various positions of the sun: dawn, sunrise, solar noon, sunset,
  dusk, solar elevation, solar azimuth and rahukaalam.
* the phase of the moon.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/astral
%python3_sitelibdir/astral-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2-alt1
- 3.2 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt1
- initial
