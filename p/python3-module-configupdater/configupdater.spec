%define _unpackaged_files_terminate_build 1
%define pypi_name configupdater

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.1
Release: alt1

Summary: Parser like ConfigParser but for updating configuration files
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pyscaffold/configupdater.git
Url: https://pypi.org/project/configupdater

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
The sole purpose of ConfigUpdater is to easily update an INI config file with no
changes to the original file except the intended ones. This means comments, the
ordering of sections and key/value-pairs as wells as their cases are kept as in
the original file. Thus ConfigUpdater provides complementary functionality to
Python's ConfigParser which is primarily meant for reading config files and
writing new ones.

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
export TOXENV=py3-all
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/configupdater/
%python3_sitelibdir/ConfigUpdater-%version.dist-info/

%changelog
* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 3.1 -> 3.1.1.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 3.1-alt1
- Initial build for Sisyphus.
