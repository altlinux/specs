%define _unpackaged_files_terminate_build 1
%define oname python_utils

%def_with check

Name: python3-module-%oname
Version: 3.1.0
Release: alt1

Summary: A module with some convenient utilities not included with the standard Python install
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-utils/

BuildArch: noarch

# https://github.com/WoLpH/python-utils.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:

BuildRequires: python3(pytest)
BuildRequires: python3(pytest_asyncio)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

Provides: python3-module-python-utils = %EVR
%py3_provides python-utils

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false --develop

%files
%doc *.rst
%python3_sitelibdir/python_utils/
%python3_sitelibdir/python_utils-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.5.6 -> 3.1.0.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 2.5.6-alt1
- 2.2.0 -> 2.5.6.

* Wed Apr 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.
- Enabled build for python-3.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.git20150209
- Version 1.6.2

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141015
- Initial build for Sisyphus

