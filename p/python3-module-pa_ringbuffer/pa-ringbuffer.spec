Name: python3-module-pa_ringbuffer
Version: 0.1.4
Release: alt1

Summary: Python PortAudio bindings
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pa_ringbuffer/

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
%python3_sitelibdir/pa_ringbuffer.*
%python3_sitelibdir/*/pa_ringbuffer.*
%python3_sitelibdir/pa_ringbuffer-%version.dist-info

%changelog
* Fri Jan 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.4-alt1
- 0.1.4 released
