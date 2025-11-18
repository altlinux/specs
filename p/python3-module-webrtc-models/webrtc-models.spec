Name: python3-module-webrtc-models
Version: 0.3.0
Release: alt2

Summary: Data classes for the WebRTC spec
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/webrtc-models
VCS: https://github.com/home-assistant-libs/python-webrtc-models

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

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

%check
# no substantial tests yet 

%files
%python3_sitelibdir/webrtc_models
%python3_sitelibdir/webrtc_models-%version.dist-info

%changelog
* Tue Nov 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.0-alt2
- fixed runtime dependencies (closes: 56896)

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.0-alt1
- 0.3.0 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
