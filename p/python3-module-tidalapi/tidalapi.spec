Name: python3-module-tidalapi
Version: 0.7.3
Release: alt1

Summary: Python API for TIDAL music streaming service
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/tidalapi

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/tidalapi
%python3_sitelibdir/tidalapi-%version.dist-info

%changelog
* Tue Sep 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt1
- 0.7.3 released
