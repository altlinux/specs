%define oname jsonlib
Name: python-module-%oname
Version: 1.6.1
Release: alt1.1.1
Summary: JSON serializer/deserializer for Python
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/jsonlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
JSON is a lightweight data-interchange format. It is often used for
exchanging data between a web server and user agent.

This module aims to produce a library for serializing and deserializing
JSON that conforms strictly to RFC 4627.

%package test
Summary: Test for jsonlib
Group: Development/Python
Requires: %name = %version-%release

%description test
JSON is a lightweight data-interchange format. It is often used for
exchanging data between a web server and user agent.

This module aims to produce a library for serializing and deserializing
JSON that conforms strictly to RFC 4627.

This package contains test for jsonlib.

%prep
%setup

%build
%python_build

%install
%python_install

install -p -m644 test_jsonlib.py %buildroot%python_sitelibdir/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/test_jsonlib.py*

%files test
%python_sitelibdir/test_jsonlib.py*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.1-alt1.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus

