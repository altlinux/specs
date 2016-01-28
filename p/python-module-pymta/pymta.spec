%define oname pymta

%def_with python3

Name: python-module-%oname
Version: 0.5.2
Release: alt3.1
Summary: Library to build a custom SMTP server
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pymta/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
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
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt3.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt3
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.2-alt2.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

