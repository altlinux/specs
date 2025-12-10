Name: python3-module-webrtcvad
Version: 2.0.10
Release: alt3

Summary: Python interface to the WebRTC Voice Activity Detector
License: MIT
Group: Development/Python
Url: https://pypi.org/project/webrtcvad
VCS: https://github.com/wiseman/py-webrtcvad

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%python3_set_limited_api 3.12

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/webrtcvad.*
%python3_sitelibdir/_webrtcvad.*.so
%python3_sitelibdir/*/webrtcvad.*
%python3_sitelibdir/webrtcvad-%version.dist-info

%changelog
* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.10-alt3
- rebuilt for limited api

* Mon Oct 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.0.10-alt2
- NMU: support LoongArch architecture

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt1
- initial
