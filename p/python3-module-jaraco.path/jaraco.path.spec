%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.path

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.1
Release: alt1
Summary: Cross platform hidden file detection
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.path/
VCS: https://github.com/jaraco/jaraco.path
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
%pypi_name provides cross platform hidden file detection.

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
%pyproject_run_pytest -ra

%files
%doc README.rst
%python3_sitelibdir/jaraco/__pycache__/path.cpython-*.py*
%python3_sitelibdir/jaraco/path.py
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.4.0 -> 3.4.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus.
