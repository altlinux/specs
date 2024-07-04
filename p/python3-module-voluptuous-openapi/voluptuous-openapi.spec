Name: python3-module-voluptuous-openapi
Version: 0.0.4 
Release: alt1

Summary: Convert voluptuous schemas to OpenAPI Schema object
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/voluptuous-openapi/

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
%python3_sitelibdir/voluptuous_openapi
%python3_sitelibdir/voluptuous_openapi-%version.dist-info

%changelog
* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.4-alt1
- 0.0.4 released
