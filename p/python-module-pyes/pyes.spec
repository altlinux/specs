%define oname pyes

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.99.6
Release: alt1.dev.git20150201.1.1
Summary: Python Elastic Search driver
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aparo/pyes.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-urllib3 python-module-six
#BuildPreReq: python-module-nose python-module-nose-cover3
#BuildPreReq: python-module-unittest2 python-module-thrift
#BuildPreReq: python-modules-json python-modules-multiprocessing
#BuildPreReq: python-modules-logging
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-urllib3 python3-module-six
#BuildPreReq: python3-module-nose python3-module-nose-cover3
#BuildPreReq: python3-module-unittest2 python3-module-thrift
%endif

%py_provides %oname
%py_requires urllib3 six json multiprocessing logging thrift

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-nose python3-module-ntlm python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pytest python3-module-serial python3-module-setuptools python3-module-zope python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose-cover3 python-module-objects.inv python-module-setuptools-tests python-module-thrift python-module-unittest2 python-module-urllib3 python3-module-nose-cover3 python3-module-setuptools-tests python3-module-thrift python3-module-unittest2 python3-module-urllib3 rpm-build-python3 time

%description
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Elastic Search driver
Group: Development/Python3
%py3_provides %oname
%py3_requires urllib3 six json multiprocessing logging thrift

%description -n python3-module-%oname
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python connector for ElasticSearch - the pythonic way to use
ElasticSearch.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
./pyes_coverage.sh
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' pyes_coverage.sh
./pyes_coverage.sh
popd
%endif

%files
%doc AUTHORS Changelog FAQ THANKS TODO *.md *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS Changelog FAQ THANKS TODO *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.99.6-alt1.dev.git20150201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.99.6-alt1.dev.git20150201.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.6-alt1.dev.git20150201
- Initial build for Sisyphus

