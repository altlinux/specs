%define oname BarkingOwl

%def_without python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1.git20150122
Summary: Scalable web scraper framework for finding documents on websites
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/BarkingOwl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thequbit/BarkingOwl.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-BeautifulSoup4 python-module-libmagic
BuildPreReq: python-module-pika python-module-six
BuildPreReq: python-module-tldextract python-modules-wsgiref
BuildPreReq: python-module-requests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-BeautifulSoup4 python3-module-libmagic
BuildPreReq: python3-module-pika python3-module-six
BuildPreReq: python3-module-tldextract python3-module-requests
BuildPreReq: python-tools-2to3
%endif

%py_provides barking_owl
Requires: python-module-libmagic
%py_requires bs4 magic pika six wsgiref tldextract requests json

%description
BarkingOwl is a scalable web crawler intended to be used to find
specific document types on websites, such as PDFs, XLS, TXT, HTML, etc.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip scraper

%description tests
BarkingOwl is a scalable web crawler intended to be used to find
specific document types on websites, such as PDFs, XLS, TXT, HTML, etc.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Scalable web scraper framework for finding documents on websites
Group: Development/Python3
%py3_provides barking_owl
Requires: python3-module-libmagic
%py3_requires bs4 magic pika six wsgiref tldextract requests

%description -n python3-module-%oname
BarkingOwl is a scalable web crawler intended to be used to find
specific document types on websites, such as PDFs, XLS, TXT, HTML, etc.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip scraper

%description -n python3-module-%oname-tests
BarkingOwl is a scalable web crawler intended to be used to find
specific document types on websites, such as PDFs, XLS, TXT, HTML, etc.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *.md plugins
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md plugins
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20150122
- Version 0.6.0

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150119
- Initial build for Sisyphus

