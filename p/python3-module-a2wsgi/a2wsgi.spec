Name: python3-module-a2wsgi
Version: 1.10.4
Release: alt1

Summary: Convert WSGI app from/to ASGI app
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/a2wsgi/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(pytest)
BuildRequires: python3(httpx)

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

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/a2wsgi
%python3_sitelibdir/a2wsgi-%version.dist-info

%changelog
* Tue May 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.4-alt1
- 1.10.4 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released
