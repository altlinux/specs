%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.envs

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.0
Release: alt1

Summary: Classes for orchestrating Python virtual environments
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/jaraco.envs.git
Url: https://pypi.org/project/jaraco.envs/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# dependencies=
BuildRequires: python3(path)
BuildRequires: python3(virtualenv)
BuildRequires: python3(tox)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name
%py3_requires virtualenv
%py3_requires tox

%description
%pypi_name provides classes for orchestrating Python virtual environments.

%prep
%setup
%autopatch -p1

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/jaraco/__pycache__/envs.cpython-*.py*
%python3_sitelibdir/jaraco/envs.py
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.1 -> 2.2.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus.
