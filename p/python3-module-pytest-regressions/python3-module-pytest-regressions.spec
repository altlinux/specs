%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-regressions

# unstable tests
%def_without check

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1

Summary: Pytest plugin for regression testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-regressions/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools-scm)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(yaml)
BuildRequires: python3(numpy)
BuildRequires: python3(pandas)
BuildRequires: python3(packaging)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
Fixtures to write regression tests.

%prep
%setup
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/pytest_regressions/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 2.4.1-alt1
- initial build for Sisyphus

