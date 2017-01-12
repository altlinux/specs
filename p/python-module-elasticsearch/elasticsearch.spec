%define _unpackaged_files_terminate_build 1
%define oname elasticsearch

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.1.0
Release: alt1
Summary: Python client for Elasticsearch
License: ASL
Group: Development/Python
Url: https://github.com/elastic/elasticsearch-py

# https://github.com/elasticsearch/elasticsearch-py.git
Source0: https://pypi.python.org/packages/2a/0a/fca7faa8155a1b6fcd3ce86a351640a2593b1ac8ee461f908a190b06e284/%{oname}-%{version}.tar.gz
Patch0: %name-2.3.0-alt1.patch

BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-urllib3 python-module-requests
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-mock python-module-pyaml
#BuildPreReq: python-module-nosexcover python-module-pylibmc
#BuildPreReq: python-modules-logging python-modules-json
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-urllib3 python3-module-requests
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-mock
#BuildPreReq: python3-module-nosexcover
%endif

%py_provides %oname
%py_requires json

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ndg-httpsclient python3-module-nose python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nosexcover python-module-objects.inv python-module-pbr python-module-pylibmc python-module-pytest python-module-requests python-module-unittest2 python-module-yaml python3-module-chardet python3-module-coverage python3-module-html5lib python3-module-nosexcover python3-module-pbr python3-module-pytest python3-module-unittest2 python3-module-urllib3 rpm-build-python3 time python-module-sphinx_rtd_theme

%description
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python client for Elasticsearch
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test.*

%files tests
%python_sitelibdir/*/*/test.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1
- automated PyPI update

* Mon May  9 2016 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.dev.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.dev.git20150226.1
- NMU: Use buildreq for BR.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.dev.git20150226
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.dev.git20150211
- Version 1.5.0-dev

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20141231
- Version 1.3.0

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.git20141022
- Tuned requirements

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141022
- Initial build for Sisyphus

