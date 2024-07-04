Name: python3-module-aiozoneinfo
Version: 0.2.1
Release: alt1

Summary: Tools to fetch zoneinfo with asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiozoneinfo/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup
%pyproject_deps_resync_build

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aiozoneinfo
%python3_sitelibdir/aiozoneinfo-%version.dist-info

%changelog
* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released
