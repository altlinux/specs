%define pypi_name pdm

%def_with check

Name:    python3-module-%pypi_name
Version: 2.10.0
Release: alt1

Summary: A modern Python package and dependency manager supporting the latest PEP standards
License: MIT
Group:   Development/Python3
URL:     https://github.com/pdm-project/pdm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-unearth
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-resolvelib
BuildRequires: python3-module-rich
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-pyproject_hooks
BuildRequires: python3-module-installer
BuildRequires: python3-module-cachecontrol
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-blinker
BuildRequires: python3-module-pytest-httpserver
BuildRequires: python3-module-shellingham
BuildRequires: python3-module-findpython
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-first
BuildRequires: python3-module-flaky
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
%pyproject_run_pytest -k 'not network'

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 2.10.0-alt1
- Initial build for Sisyphus.
