%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-localserver

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: pytest plugin to test server connections locally
License: MIT
Group: Development/Python3
VCS: https://github.com/pytest-dev/pytest-localserver.git
Url: https://pypi.org/project/pytest-localserver

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# deps
BuildRequires: python3(werkzeug)

BuildRequires: python3(pytest)
BuildRequires: python3(requests)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
%pypi_name is a plugin for the pytest testing framework which enables
you to test server connections locally.

%prep
%setup
%autopatch -p1

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
%tox_check_pyproject -- -vra

%files
%doc README.rst
%python3_sitelibdir/pytest_localserver/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
