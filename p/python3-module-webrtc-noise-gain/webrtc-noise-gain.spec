Name: python3-module-webrtc-noise-gain
Version: 1.2.3
Release: alt1

Summary: Python interface to the WebRTC
License: MIT
Group: Development/Python
Url: https://pypi.org/project/webrtc-noise-gain/

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pybind11)

%description
Tiny Python wrapper around webrtc-audio-processing for
noise suppression and auto gain only.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/webrtc_noise_gain
%python3_sitelibdir/webrtc_noise_gain_cpp.*.so
%python3_sitelibdir/webrtc_noise_gain-%version.dist-info

%changelog
* Thu Nov 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released
