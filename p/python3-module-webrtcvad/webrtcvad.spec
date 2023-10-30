Name: python3-module-webrtcvad
Version: 2.0.10
Release: alt2

Summary: Python interface to the WebRTC Voice Activity Detector
License: MIT
Group: Development/Python
Url: https://pypi.org/project/webrtcvad/

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

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
* Mon Oct 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.0.10-alt2
- NMU: support LoongArch architecture

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt1
- initial
