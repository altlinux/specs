Name: python3-module-webrtc-models
Version: 0.2.0
Release: alt1

Summary: Data classes for the WebRTC spec
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/webrtc-models/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(hatchling)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# no substantial tests yet 

%files
%python3_sitelibdir/webrtc_models
%python3_sitelibdir/webrtc_models-%version.dist-info

%changelog
* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
