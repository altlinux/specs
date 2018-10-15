%define _unpackaged_files_terminate_build 1
%define oname pytest-flake8

%def_with check

Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: pytest plugin for efficiently checking PEP8 compliance
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-flake8

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: pytest
BuildRequires: python-module-tox
BuildRequires: python-module-flake8
BuildRequires: pytest3
BuildRequires: python3-module-flake8
BuildRequires: python3-module-tox
%endif

%description
pytest plugin for efficiently checking PEP8 compliance

%package -n python3-module-%oname
Summary: pytest plugin for efficiently checking PEP8 compliance
Group: Development/Python3

%description -n python3-module-%oname
pytest plugin for efficiently checking PEP8 compliance

%prep
%setup

# due to tox issue https://github.com/tox-dev/tox/issues/1020
sed -i '/basepython=python/d' tox.ini
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
export PYTHONPATH=%buildroot%python_sitelibdir
# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox \
--sitepackages -e py%{python_version_nodots python} --notest

cp -f %_bindir/pytest .tox/py%{python_version_nodots python}/bin/

TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox \
--sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox.py3 \
--sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/pytest3 .tox/py%{python_version_nodots python3}/bin/pytest

TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox.py3 \
--sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc LICENSE CHANGELOG README.rst
%python_sitelibdir/pytest_flake8-*.egg-info/
%python_sitelibdir/pytest_flake8.py*
%python_sitelibdir/__pycache__/

%files -n python3-module-%oname
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/pytest_flake8-*.egg-info/
%python3_sitelibdir/pytest_flake8.py
%python3_sitelibdir/__pycache__/

%changelog
* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 0.9.1 -> 1.0.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.1-alt1
- Initial build for ALT.
