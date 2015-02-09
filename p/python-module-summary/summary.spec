%define oname summary

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150209
Summary: Extractor to get main content from the web page
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/summary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/after12am/summary.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-chardet python-module-lxml
BuildPreReq: python-module-nltk python-module-numpy
BuildPreReq: python-module-networkx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-chardet python3-module-lxml
BuildPreReq: python3-module-nltk python3-module-numpy
BuildPreReq: python3-module-networkx
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires chardet lxml nltk numpy networkx

%description
A python script provides content extraction and summarization of the web
page.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip html

%description tests
A python script provides content extraction and summarization of the web
page.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Extractor to get main content from the web page
Group: Development/Python3
%py3_provides %oname
%py3_requires chardet lxml nltk numpy networkx

%description -n python3-module-%oname
A python script provides content extraction and summarization of the web
page.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A python script provides content extraction and summarization of the web
page.

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
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150209
- Initial build for Sisyphus

