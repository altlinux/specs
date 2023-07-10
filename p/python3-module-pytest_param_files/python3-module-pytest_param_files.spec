%define pypi_name pytest_param_files

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3.5
Release: alt1

Summary: Create pytest parametrize decorators from external files
License: MIT
Group:   Development/Python3
URL:     https://github.com/chrisjsewell/pytest-param-files

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3(flit_core)

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A small package to generate parametrized pytests from external files.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus
