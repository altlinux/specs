%define oname 9ML

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt4.1.1

Summary: A tool for reading, writing and generally working with 9ML files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/9ML

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-sphinx-devel
#BuildPreReq: python-module-sphinxcontrib-spelling
#BuildPreReq: libenchant-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-enchant python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxcontrib python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base
BuildRequires: libenchant python-module-alabaster python-module-html5lib python-module-sphinxcontrib-spelling python3-module-setuptools rpm-build-gir rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%add_python_req_skip testing_utils

%description
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

%package tests
Summary: Tests for NineML
Group: Development/Python
Requires: %name = %EVR

%description tests
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

This package contains tests for NineML.

%package examples
Summary: Examples for NineML
Group: Development/Documentation
Requires: %name = %EVR

%description examples
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

This package contains examples for NineML.

%package pickles
Summary: Pickles for NineML
Group: Development/Python

%description pickles
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

This package contains pickles for NineML.

%package docs
Summary: Documentation for NineML
Group: Development/Documentation
BuildArch: noarch

%description docs
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

This package contains documentation for NineML.

%if_with python3
%package -n python3-module-%oname
Summary: A tool for reading, writing and generally working with 9ML files
Group: Development/Python3

%description -n python3-module-%oname
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

%package -n python3-module-%oname-tests
Summary: Tests for NineML
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
NineML (http://nineml.incf.org) is a simulator independent language
which aims to provide unambiguous descriptions of neuronal network
models for efficient model sharing and reusability. This package
provides a Python library for reading, writing, validating and
manipulating NineML models.

This package contains tests for NineML.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '._*' -exec rm -f '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
#for i in $(find ./ -type f -name '*.py'); do
#	2to3 -w -n $i
#done
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

pushd doc/python_nineml_api
%make pickle
%make html
popd

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/python_nineml_api/build/pickle \
	%buildroot%python_sitelibdir/nineml/

%files
%doc AUTHORS README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/testing_utils
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/*/testing_utils

%files examples
%python_sitelibdir/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/python_nineml_api/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/testing_utils
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/testing_utils
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt4.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt4
- Excluded examples from python3-module-%oname

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Added module for Python 3

* Sun Dec 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Extracted examples as separate package

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

