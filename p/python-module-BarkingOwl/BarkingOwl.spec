%define _unpackaged_files_terminate_build 1
%define oname BarkingOwl

%def_without python3

Name: python-module-%oname
Version: 0.8.1
Release: alt2.1
Summary: Scalable web scraper framework for finding documents on websites
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/BarkingOwl/

# https://github.com/thequbit/BarkingOwl.git
Source0: https://pypi.python.org/packages/a2/6d/f3d53fbbc1f616835345dfce105f2a33e556dae0b6b6cf6e5ed8ebeca17b/%{oname}-%{version}.tar.gz
Patch1: %oname-%version-alt-build.patch

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-BeautifulSoup4 python-module-libmagic
BuildRequires: python-module-pika python-module-six
BuildRequires: python-module-tldextract python-modules-wsgiref
BuildRequires: python-module-requests python-modules-json
BuildRequires: python2.7(daemon) python2.7(pymongo) python2.7(sqlalchemy) python2.7(docutils)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-BeautifulSoup4 python3-module-libmagic
BuildRequires: python3-module-pika python3-module-six
BuildRequires: python3-module-tldextract python3-module-requests
BuildRequires: python-tools-2to3
BuildRequires: python3(daemon) python3(pymongo) python3(sqlalchemy) python3(docutils)
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

%if_with python3
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
%endif

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p2

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
%doc PKG-INFO
%python_sitelibdir/*
#exclude %python_sitelibdir/*/*/tests.*

#files tests
#python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/*/tests.*
#exclude %python3_sitelibdir/*/*/*/tests.*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*/tests.*
#python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20150209
- Version 0.6.5

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4.1-alt1.git20150125
- Version 0.6.4.1

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20150122
- Version 0.6.0

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150119
- Initial build for Sisyphus

