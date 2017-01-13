%define _unpackaged_files_terminate_build 1
%define shortname simplejson

%def_with python3

Name: python-module-simplejson
Version: 3.10.0
Release: alt1

Summary: Simplejson is a simple, fast, extensible JSON encoder/decoder for Python
License: MIT/X Consortium
Group: Development/Python

Url: http://undefined.org/python/#simplejson

Source0: https://pypi.python.org/packages/40/ad/52c1f3a562df3b210e8f165e1aa243a178c454ead65476a39fa3ce1847b6/simplejson-%{version}.tar.gz
Patch: simplejson-3.5.3-alt-python3.patch

BuildRequires: python-module-setuptools python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif


%description
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

%package -n python3-module-simplejson
Summary: Simplejson is a simple, fast, extensible JSON encoder/decoder for Python
Group: Development/Python3

%description -n python3-module-simplejson
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

%package doc
Summary: Documentation for %name
Group: Development/Python
BuildArch: noarch

%description doc
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

This package contains documentation for simplejson.


%prep
%setup -q -n simplejson-%{version}

%if_with python3
cp -fR . ../python3
pushd ../python3
%patch -p2
popd
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

./scripts/make_docs.py

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%shortname/
%exclude %python_sitelibdir/%shortname/tests
%python_sitelibdir/*.egg-info

%check
python setup.py check
%if_with python3
pushd ../python3
python3 setup.py check
popd
%endif

%files doc
%doc docs/*

%if_with python3
%files -n python3-module-simplejson
%python3_sitelibdir/%shortname/
%exclude %python3_sitelibdir/%shortname/tests
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.8.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.5-alt1
- Version 3.6.5

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Version 3.5.3
- Added module for Python 3

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1
- Version 3.3.1

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Version 3.3.0

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1
- Version 2.5.0

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1
- 2.1.3
- enable tests

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.2-alt2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt2
- Rebuilt for debuginfo

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.1
- Rebuilt with python 2.6

* Fri May 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.9-alt1
- 2.0.9
- numerous spec fixes
- package documentation
- don't package tests

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.7.4-alt1.1
- Rebuilt with python-2.5.

* Thu Nov 15 2007 Gennady Kovalev <gik@altlinux.ru> 1.7.4-alt1
- 1.7.4 release

* Wed Mar 22 2006 Gennady Kovalev <gik@altlinux.ru> 1.1-alt1
- Initial build
