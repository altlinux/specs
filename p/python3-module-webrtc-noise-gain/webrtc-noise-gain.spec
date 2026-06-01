Name: python3-module-webrtc-noise-gain
Version: 1.3.0
Release: alt1

Summary: Python interface to the WebRTC
License: MIT
Group: Development/Python
URL: https://pypi.org/project/webrtc-noise-gain
VCS: https://github.com/OHF-voice/webrtc-noise-gain

Source0: %name-%version.tar
Source1: pyproject_deps.json

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%python3_set_limited_api 3.9

%description
Tiny Python wrapper around webrtc-audio-processing for
noise suppression and auto gain only.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rf webrtc_noise_gain
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/webrtc_noise_gain
%python3_sitelibdir/webrtc_noise_gain-%version.dist-info

%changelog
* Fri May 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released

* Thu Apr 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.5-alt1
- 1.2.5 released

* Wed Apr 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.3-alt3
- fixed build with gcc15

* Sat Jun 08 2024 Michael Shigorin <mike@altlinux.org> 1.2.3-alt2
- E2K: ftbfs workaround (ilyakurdyukov@)

* Thu Nov 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released
