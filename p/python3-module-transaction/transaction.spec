%define _unpackaged_files_terminate_build 1
%define oname transaction

%def_with check

Name: python3-module-%oname
Version: 3.0.1
Release: alt1
Summary: Transaction management for Python
License: ZPL-2.1
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/transaction/

# https://github.com/zopefoundation/transaction.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(zope.interface)

BuildRequires: python3(mock)
BuildRequires: python3(zope.testrunner)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
This package contains a generic transaction implementation for Python.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    zope-testrunner --test-path=src -vv
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr --develop

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%exclude %python3_sitelibdir/%oname/tests

%changelog
* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 2.1.2 -> 3.0.1.

* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.2-alt1
- Update to upstream version 2.1.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.5-alt1.dev0.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.5-alt1.dev0.git20150807.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1.dev0.git20150807
- Version 1.4.5.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.dev.git20140404
- Version 1.4.4dev
- Enables testing

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.0-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added module for Python 3

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

