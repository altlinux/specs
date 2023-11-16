%define pypi_name pytest-metadata
%define mod_name pytest_metadata

%def_with check

Name:    python3-module-%pypi_name
Version: 3.0.0
Release: alt1

Summary: Plugin for accessing test session metadata
License: MPL-2.0
Group:   Development/Python3
URL:     https://github.com/pytest-dev/pytest-metadata

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
pytest-metadata is a plugin for pytest that provides access to test session
metadata.

%prep
%setup -n %pypi_name-%version
# hatch-vcs can use setuptools_scm which implements a file_finders entry point
# which returns all files tracked by SCM. Though that is version detection usage
# only (at least for now), it's safer to provide a real git tree.
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
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 15 2023 Alexander Burmatov <thatman@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus.
