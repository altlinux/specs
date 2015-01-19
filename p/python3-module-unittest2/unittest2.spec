%define oname unittest2
Name: python3-module-%oname
Version: 0.5.1
Release: alt2.hg20100714
Summary: Extensions to the Python standard library module 'unittest'
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/unittest2py3k
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.google.com/p/unittest-ext/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
Requires: python3-module-discover

%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7 and 3.2.

This is a Python 3 compatible version of unittest2. Tested with Python
3.0, 3.1 and 3.2.

%prep
%setup

%build
%python3_build
pushd unittest2-py3k
%python3_build
popd

%install
%python3_install
pushd unittest2-py3k
%python3_install
popd

pushd %buildroot%_bindir
mv discover discover.py3
mv unit2 unit2-3
mv unit2.py unit2.py3
popd

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/discover.py
%exclude %python3_sitelibdir/__pycache__/discover.*
%exclude %python3_sitelibdir/discover*.egg-info

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2.hg20100714
- Deleted discover.py

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.hg20100714
- Initial build for Sisyphus

