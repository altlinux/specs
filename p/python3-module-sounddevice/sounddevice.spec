Name: python3-module-sounddevice
Version: 0.5.0
Release: alt1

Summary: Python PortAudio bindings
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sounddevice/

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cffi)
BuildRequires: pkgconfig(portaudio-2.0)

%description
This Python module provides bindings for the PortAudio library and a few
convenience functions to play and record NumPy_ arrays containing audio signals

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/_sounddevice.py
%python3_sitelibdir/sounddevice.py
%python3_sitelibdir/*/*sounddevice.*
%python3_sitelibdir/sounddevice-%version.dist-info

%changelog
* Thu Sep 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Tue Jun 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.6-alt1
- 0.4.6 released

* Fri Jan 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.5-alt1
- 0.4.5 released
