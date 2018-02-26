%define oname pymta

%def_with python3

Name: python-module-%oname
Version: 0.5.2
Release: alt2
Summary: Library to build a custom SMTP server
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pymta/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
pymta is a library to build a custom SMTP server in Python. This is
useful if you want to...

* test mail-sending code against a real SMTP server even in your unit
  tests.
* build a custom SMTP server with non-standard behavior without
  reimplementing the whole SMTP protocol.
* have a low-volume SMTP server which can be easily extended using
  Python.

%if_with python3
%package -n python3-module-%oname
Summary: Library to build a custom SMTP server (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
pymta is a library to build a custom SMTP server in Python. This is
useful if you want to...

* test mail-sending code against a real SMTP server even in your unit
  tests.
* build a custom SMTP server with non-standard behavior without
  reimplementing the whole SMTP protocol.
* have a low-volume SMTP server which can be easily extended using
  Python.

%package -n python3-module-%oname-tests
Summary: Tests for pymta (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pymta is a library to build a custom SMTP server in Python. This is
useful if you want to...

* test mail-sending code against a real SMTP server even in your unit
  tests.
* build a custom SMTP server with non-standard behavior without
  reimplementing the whole SMTP protocol.
* have a low-volume SMTP server which can be easily extended using
  Python.

This package contains tests for pymta.
%endif

%package tests
Summary: Tests for pymta
Group: Development/Python
Requires: %name = %version-%release

%description tests
pymta is a library to build a custom SMTP server in Python. This is
useful if you want to...

* test mail-sending code against a real SMTP server even in your unit
  tests.
* build a custom SMTP server with non-standard behavior without
  reimplementing the whole SMTP protocol.
* have a low-volume SMTP server which can be easily extended using
  Python.

This package contains tests for pymta.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/*.txt examples
%python_sitelibdir/*
%exclude %python_sitelibdir/examples
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files tests
%doc tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/examples
%exclude %python3_sitelibdir/tests
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/examples
%python3_sitelibdir/tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

