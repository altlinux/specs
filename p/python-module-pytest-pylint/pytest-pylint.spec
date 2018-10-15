%define _unpackaged_files_terminate_build 1
%define oname pytest-pylint

%def_with check

Name: python-module-%oname
Version: 0.12.3
Release: alt2
Summary: pytest plugin to check source code with pylint
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-pylint/

# https://github.com/carsongee/pytest-pylint.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: pylint
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-pep8
BuildRequires: python-module-mock
BuildRequires: python-module-tox
BuildRequires: python-module-coverage
BuildRequires: python3-module-pylint
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-pep8
BuildRequires: python3-module-mock
BuildRequires: python3-module-tox
BuildRequires: python3-module-coverage
%endif

%description
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.

%package -n python3-module-%oname
Summary: pytest plugin to check source code with pylint
Group: Development/Python3

%description -n python3-module-%oname
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.

%prep
%setup

# ignore pytest warnings as they are not expected on stdout and mess the results
sed -i '/^\[pytest\][[:space:]]*/{$!N;/\naddopts[[:space:]]*=/{s/$/ -p no:warnings/}}' \
tox.ini
rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export PIP_INDEX_URL=http://host.invalid./

# copy necessary exec deps
export PYTHONPATH=`pwd`
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages \
-e py%{python_version_nodots python} --notest
cp -T %_bindir/coverage .tox/py%{python_version_nodots python}/bin/coverage
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages \
-e py%{python_version_nodots python} -v -- -v

pushd ../python3
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages \
-e py%{python_version_nodots python3} --notest
cp -T %_bindir/coverage3 .tox/py%{python_version_nodots python3}/bin/coverage
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages \
-e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc *.rst pylintrc
%python_sitelibdir/pytest_pylint.py*
%python_sitelibdir/pytest_pylint-*.egg-info/

%files -n python3-module-%oname
%doc *.rst pylintrc
%python3_sitelibdir/pytest_pylint.py
%python3_sitelibdir/pytest_pylint-*.egg-info/
%python3_sitelibdir/__pycache__/

%changelog
* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 0.12.3-alt2
- Fixed tests with new pytest-3.8.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 0.12.3-alt1
- 0.7.1 -> 0.12.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1
- Updated to upstream version 0.7.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20150423.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150423
- Initial build for Sisyphus

