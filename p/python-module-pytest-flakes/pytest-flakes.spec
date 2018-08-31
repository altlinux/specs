%define _unpackaged_files_terminate_build 1
%define oname pytest-flakes

%def_with check

Name: python-module-%oname
Version: 4.0.0
Release: alt1

Summary: pytest plugin to check source code with pyflakes
License: MIT
Group: Development/Python

Url: https://pypi.python.org/pypi/pytest-flakes

# https://github.com/fschulze/pytest-flakes.git
Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-coverage
BuildRequires: python-module-pytest-pep8
BuildRequires: pyflakes
BuildRequires: python3-module-tox
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest-pep8
BuildRequires: python3-pyflakes
%endif

BuildArch: noarch

%description
py.test plugin for efficiently checking python source with pyflakes.

%package -n python3-module-%oname
Summary: pytest plugin to check source code with pyflakes
Group: Development/Python3

%description -n python3-module-%oname
py.test plugin for efficiently checking python source with pyflakes.

%prep
%setup
%patch -p1

rm -rf ../python3
cp -a . ../python3

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
export PYTHONPATH=$PWD
# copy necessary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages \
-e py%{python_version_nodots python} --notest
cp %_bindir/{py.test,coverage} .tox/py%{python_version_nodots python}/bin/
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages \
-e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH=$PWD
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages \
-e py%{python_version_nodots python3} --notest
cp %_bindir/py.test3 .tox/py%{python_version_nodots python3}/bin/py.test
cp %_bindir/coverage3 .tox/py%{python_version_nodots python3}/bin/coverage
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages \
-e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc README.rst
%python_sitelibdir/pytest_flakes.py*
%python_sitelibdir/pytest_flakes-*.egg-info/

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/pytest_flakes.py
%python3_sitelibdir/pytest_flakes-*.egg-info/
%python3_sitelibdir/__pycache__/

%changelog
* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 1.0.1 -> 4.0.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2
- Fixed build spec with pytest3

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20140206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140206
- Initial build for Sisyphus

