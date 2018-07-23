%define _unpackaged_files_terminate_build 1
%define oname pytest-multihost

%def_with check

Name: python-module-%oname
Version: 3.0
Release: alt1

Summary: Utility for writing multi-host tests for pytest
License: GPLv3
Group: Development/Python
# Source-git: https://github.com/encukou/pytest-multihost.git
Url: https://pypi.python.org/pypi/pytest-multihost

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-paramiko
BuildRequires: python3-module-tox
BuildRequires: python3-module-paramiko
%endif
%py_requires yaml paramiko

BuildArch: noarch

%description
A pytest plugin for multi-host testing.

%package -n python3-module-%oname
Summary: Utility for writing multi-host tests for pytest
Group: Development/Python3
%py3_requires yaml paramiko

%description -n python3-module-%oname
A pytest plugin for multi-host testing.

%prep
%setup
# skip tests which require SSH connection
sed -i '/commands = python -m pytest/s/$/ -m "not needs_ssh"/g' tox.ini
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
tox --sitepackages -e py%{python_version_nodots python} -v

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v
popd

%files
%doc README.rst COPYING
%python_sitelibdir/pytest_multihost/
%python_sitelibdir/pytest_multihost-*.egg-info/

%files -n python3-module-%oname
%doc README.rst COPYING
%python3_sitelibdir/pytest_multihost/
%python3_sitelibdir/pytest_multihost-*.egg-info/

%changelog
* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1
- 1.1 -> 3.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20141209.1
- NMU: Use buildreq for BR.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141209
- Version 0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141126
- Initial build for Sisyphus

