%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.test

%def_with check

Name: python3-module-%pypi_name
Version: 5.3.0
Release: alt1
Summary: Testing support by jaraco
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.test
VCS: https://github.com/jaraco/jaraco.test.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(jaraco.functools)
BuildRequires: python3(jaraco.context)

BuildRequires: python3(pytest)
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
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
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/jaraco/test/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
