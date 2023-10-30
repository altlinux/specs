%define pypi_name pyproject-api

# need tox >= 4.2
%def_without check

Name:    python3-module-%pypi_name
Version: 1.6.1
Release: alt1

Summary: API to interact with the python pyproject.toml based projects
License: MIT
Group:   Development/Python3
URL:     https://github.com/tox-dev/pyproject-api

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-vcs)

%if_with check
BuildRequires: python3(covdefaults)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(pytest_cov)
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

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
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject -- -m "not internet"

%files
%python3_sitelibdir/pyproject_api/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 27 2023 Alexander Burmatov <thatman@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
