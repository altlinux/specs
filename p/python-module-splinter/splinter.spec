%define oname splinter

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20141109.1
Summary: splinter - python test framework for web applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/splinter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/cobrateam/splinter.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-selenium python-module-zope.testbrowser
#BuildPreReq: python-module-lxml python-module-cssselect
#BuildPreReq: python-module-django python-module-flask
#BuildPreReq: python-module-coverage python-module-argparse
#BuildPreReq: python-module-mechanize
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-selenium python3-module-zope.testbrowser
#BuildPreReq: python3-module-lxml python3-module-cssselect
#BuildPreReq: python3-module-django python3-module-flask
#BuildPreReq: python3-module-coverage python3-module-argparse
#BuildPreReq: python3-module-mechanize
%endif

%py_provides %oname
%py_requires zope.testbrowser mechanize

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-BeautifulSoup4 python-module-PyStemmer python-module-Pygments python-module-WSGIProxy2 python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-itsdangerous python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-mechanize python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-restkit python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-waitress python-module-webob python-module-webtest python-module-werkzeug python-module-yaml python-module-zope python-module-zope.cachedescriptors python-module-zope.event python-module-zope.exceptions python-module-zope.interface python-module-zope.schema python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-cssselect python3-module-genshi python3-module-html5lib python3-module-jinja2 python3-module-paste python3-module-psycopg2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-waitress python3-module-webtest python3-module-wsgiproxy python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-coverage python-module-django python-module-docutils python-module-flask python-module-objects.inv python-module-selenium python-module-setuptools-tests python-module-zope.testbrowser python3-module-coverage python3-module-django python3-module-flask python3-module-setuptools-tests python3-module-zope.testbrowser rpm-build-python3 time

%description
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

%package -n python3-module-%oname
Summary: splinter - python test framework for web applications
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.testbrowser mechanize

%description -n python3-module-%oname
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

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
%doc AUTHORS *.rst samples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst samples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20141109.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141109
- Initial build for Sisyphus

