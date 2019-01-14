%define _unpackaged_files_terminate_build 1
%define oname pluggy

%def_with check

Name: python-module-%oname
Version: 0.8.1
Release: alt1

Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pluggy.git
Url: https://pypi.python.org/pypi/pluggy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python-module-tox
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
%endif

BuildArch: noarch

%description
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%package -n python3-module-%oname
Summary: Plugin and hook calling mechanisms for python
Group: Development/Python3

%description -n python3-module-%oname
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%prep
%setup

# there is a file with name CHANGELOG.rst, not CHANGELOG
# a wrong reference leads to broken install via pip
sed -i '/^include CHANGELOG$/{s/$/.rst/}' MANIFEST.in
rm -rf ../python3
cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
%python3_install
popd

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_INDEX_URL=http://host.invalid./

# copy nessecary exec deps
export PYTHONPATH="$(pwd)"
export TOX_TESTENV_PASSENV='PYTHONPATH'
%_bindir/tox --sitepackages -e py%{python_version_nodots python} --notest
cp -T %_bindir/py.test .tox/py%{python_version_nodots python}/bin/pytest
sed -i "1c #!$(pwd)/.tox/py%{python_version_nodots python}/bin/python" \
.tox/py%{python_version_nodots python}/bin/pytest

%_bindir/tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH="$(pwd)"
%_bindir/tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -T %_bindir/py.test3 .tox/py%{python_version_nodots python3}/bin/pytest
sed -i "1c #!$(pwd)/.tox/py%{python_version_nodots python3}/bin/python3" \
.tox/py%{python_version_nodots python3}/bin/pytest

%_bindir/tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc LICENSE CHANGELOG.rst README.rst
%python_sitelibdir/pluggy/
%python_sitelibdir/pluggy-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE CHANGELOG.rst README.rst
%python3_sitelibdir/pluggy/
%python3_sitelibdir/pluggy-*.egg-info/

%changelog
* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Sat Oct 20 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.6.0 -> 0.7.1.

* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.3.0 -> 0.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150528.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1.git20150528.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150528
- Initial build for Sisyphus

