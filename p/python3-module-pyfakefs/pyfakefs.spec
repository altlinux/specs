%define _unpackaged_files_terminate_build 1
%define oname pyfakefs

%def_with check

Name: python3-module-%oname
Version: 4.5.5
Release: alt1

Summary: Implements a fake file system that mocks the Python file system modules
License: Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/jmcgeheeiv/pyfakefs.git
Url: https://pypi.org/project/pyfakefs/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
%endif

BuildArch: noarch

%description
%oname implements a fake file system that mocks the Python file system
modules. Using pyfakefs, your tests operate on a fake file system in memory
without touching the real disk. The software under test requires no
modification to work with pyfakefs.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install
# don't package tests (useless)
rm -r %buildroot%python3_sitelibdir/%oname/{tests,pytest_tests}

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr -s false

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Feb 24 2022 Stanislav Levin <slev@altlinux.org> 4.5.5-alt1
- 3.7.1 -> 4.5.5.

* Wed Feb 12 2020 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- Initial build.
