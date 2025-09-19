Name: python3-module-rtmixer
Version: 0.1.7
Release: alt3

Summary: Realtime Audio Mixer for Python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/rtmixer/

Source: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cffi)
BuildRequires: python3(pa_ringbuffer)
BuildRequires: pkgconfig(portaudio-2.0)

%description
Reliable low-latency audio playback and recording with Python, using
PortAudio via the sounddevice module.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# extensions built against stable API, drop versioned ABI req
%filter_from_requires /%python3_ABI_dep/d

%files
%python3_sitelibdir/_rtmixer.*
%python3_sitelibdir/rtmixer.py
%python3_sitelibdir/*/*rtmixer.*
%python3_sitelibdir/rtmixer-%version.dist-info

%changelog
* Fri Sep 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.7-alt3
- drop versioned python abi req

* Thu Jan 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.7-alt2
- ftbfs fixed

* Thu Sep 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.7-alt1
- 0.1.7 released

* Fri Jan 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.4-alt1
- 0.1.4 released
