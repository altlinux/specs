%define _unpackaged_files_terminate_build 1
%define oname hatch_tryton

%def_with check

Name: python3-module-hatch-tryton
Version: 0.1.1
Release: alt1

Summary: A hatchling plugin
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-tryton

Source0: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%description
A hatchling plugin to manage Tryton dependencies.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A hatchling plugin to manage Tryton dependencies.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE README.rst COPYRIGHT
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Apr 23 2026 Nikita Panov <nexxy@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
