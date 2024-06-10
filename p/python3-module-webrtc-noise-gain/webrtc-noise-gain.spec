Name: python3-module-webrtc-noise-gain
Version: 1.2.3
Release: alt2

Summary: Python interface to the WebRTC
License: MIT
Group: Development/Python
Url: https://pypi.org/project/webrtc-noise-gain/

Source0: %name-%version-%release.tar
Patch2000: webrtc-e2k.patch

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
%ifarch %e2k
%patch2000 -p1
%endif

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/webrtc_noise_gain
%python3_sitelibdir/webrtc_noise_gain_cpp.*.so
%python3_sitelibdir/webrtc_noise_gain-%version.dist-info

%changelog
* Sat Jun 08 2024 Michael Shigorin <mike@altlinux.org> 1.2.3-alt2
- E2K: ftbfs workaround (ilyakurdyukov@)

* Thu Nov 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released
