%define _unpackaged_files_terminate_build 1
%define oname pytest-multihost

%def_with check

Name: python3-module-%oname
Version: 3.0
Release: alt2

Summary: Utility for writing multi-host tests for pytest
License: GPLv3
Group: Development/Python3
# Source-git: https://github.com/encukou/pytest-multihost.git
Url: https://pypi.python.org/pypi/pytest-multihost

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(paramiko)
BuildRequires: python3(tox)
%endif

%set_python3_req_method strict
%py3_provides pytest-multihost

BuildArch: noarch

%description
A pytest plugin for multi-host testing.

%prep
%setup
# skip tests which require SSH connection
sed -i '/commands = python -m pytest/s/$/ -m "not needs_ssh"/g' tox.ini

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%doc README.rst COPYING
%python3_sitelibdir/pytest_multihost/
%python3_sitelibdir/pytest_multihost-*.egg-info/

%changelog
* Fri Dec 06 2019 Stanislav Levin <slev@altlinux.org> 3.0-alt2
- Dropped Python2 subpackage.

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

