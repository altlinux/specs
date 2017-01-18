%define _unpackaged_files_terminate_build 1
%define oname webob

%def_with python3

Name: python-module-%oname
Version: 1.7.1
Release: alt1
Summary: WSGI request and response object
License: MIT
Group: Development/Python
Url: http://webob.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# https://github.com/Pylons/webob.git
Source0: https://pypi.python.org/packages/c3/6f/fc168ab701ab8f3741ed0b1377edda676c3e7db61858cef1f72969413968/WebOb-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires tempita json wsgiref

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including header
parsing and accessors for other standard parts of the environment.

%if_with python3
%package -n python3-module-%oname
Summary: WSGI request and response object (Python 3)
Group: Development/Python3
%py3_requires tempita wsgiref

%description -n python3-module-%oname
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including header
parsing and accessors for other standard parts of the environment.
%endif

%prep
%setup -q -n WebOb-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
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
%doc docs/* CHANGES.txt HISTORY.txt PKG-INFO README.rst contributing.md rtd.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc docs/* CHANGES.txt HISTORY.txt PKG-INFO README.rst contributing.md rtd.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.a0.git20150731.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.a0.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.a0.git20150731
- Version 1.5.0a0

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.dev.git20150127
- Version 1.4.1dev

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.3-alt1
- Version 1.2.3

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b3.git20120504
- Version 1.2b3
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b2.git20111206
- Version 1.2b2

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.hg20110917
- Version 1.1.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt1.hg20110430.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.hg20110430
- Version 1.0.7

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20101031
- Version 1.0

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.post1-alt1.hg20100714
- Version 0.9.8.post1

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.svn20090902.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.svn20090902
- Initial build for Sisyphus

