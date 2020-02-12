%define _unpackaged_files_terminate_build 1
%define oname pyfakefs

%def_with check

Name: python3-module-%oname
Version: 3.7.1
Release: alt1

Summary: Implements a fake file system that mocks the Python file system modules
License: Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/jmcgeheeiv/pyfakefs.git
Url: https://pypi.org/project/pyfakefs/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
%oname implements a fake file system that mocks the Python file system
modules. Using pyfakefs, your tests operate on a fake file system in memory
without touching the real disk. The software under test requires no
modification to work with pyfakefs.

%prep
%setup
# remove extra deps
grep -qsF '-rextra_requirements.txt' tox.ini || exit 1
sed -i '/-rextra_requirements\.txt/d' tox.ini

%build
%python3_build

%install
%python3_install
# don't package tests (useless)
rm -r %buildroot%python3_sitelibdir/%oname/{tests,pytest_tests}

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vv

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Feb 12 2020 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- Initial build.
