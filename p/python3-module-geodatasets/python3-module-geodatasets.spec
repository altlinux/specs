%define _unpackaged_files_terminate_build 1
%define pypi_name geodatasets
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2026.5.1
Release: alt1
Summary: Geodatasets for GeoPandas
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/geodatasets/
VCS: https://github.com/geopandas/geodatasets
BuildArch: noarch
Source: %name-%version.tar

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pooch
BuildRequires: python3-module-geopandas
%endif

%description
%summary

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
Tests for geodatasets

%prep
%setup
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
     git init
     git config user.email author@example.com
     git config user.name author
     git add .
     git commit -m 'release'
     git tag '%version'
fi

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -m 'not request'

%files
%doc *.md LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/test*

%changelog
* Tue May 19 2026 Nikita Panov <nexxy@altlinux.org> 2026.5.1-alt1
- New version 2026.5.1.

* Sun Feb 01 2026 Nikita Panov <nexxy@altlinux.org> 2026.1.0-alt1
- New version 2026.1.0.

* Tue Sep 23 2025 Nikita Panov <nexxy@altlinux.org> 2024.8.0-alt1
- Initial build for Sisyphus

