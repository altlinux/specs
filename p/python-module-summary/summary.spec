%define oname summary

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150209.1.1.1
Summary: Extractor to get main content from the web page
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/summary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/after12am/summary.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-chardet python-module-lxml
#BuildPreReq: python-module-nltk python-module-numpy
#BuildPreReq: python-module-networkx
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-chardet python3-module-lxml
#BuildPreReq: python3-module-nltk python3-module-numpy
#BuildPreReq: python3-module-networkx
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires chardet lxml nltk numpy networkx

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cssselect python-module-future python-module-genshi python-module-lxml python-module-matplotlib python-module-mpmath python-module-numpy python-module-pyparsing python-module-pytest python-module-scipy python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cssselect python3-module-genshi python3-module-lxml python3-module-matplotlib python3-module-numpy python3-module-pyparsing python3-module-pytest python3-module-scipy python3-module-setuptools python3-module-yaml
BuildRequires: python-module-chardet python-module-html5lib python-module-networkx-core python-module-nltk python-module-pydot python-module-pygraphviz python-module-setuptools python3-module-chardet python3-module-html5lib python3-module-networkx-core python3-module-nltk python3-module-pydot python3-module-pygraphviz python3-module-setuptools rpm-build-python3 time

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150209.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150209
- Initial build for Sisyphus

