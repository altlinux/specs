%define oname webapp2

%def_with python3

Name: python-module-%oname
Version: 2.5.2
Release: alt1.hg20140602
Summary: Taking Google App Engine's webapp to the next level!
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/webapp2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.google.com/p/webapp-improved/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-webob
BuildPreReq: python-module-jinja2 python-module-mako
BuildPreReq: python-module-simplejson python-module-babel
BuildPreReq: python-module-pytz
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-webob
BuildPreReq: python3-module-jinja2 python3-module-mako
BuildPreReq: python3-module-simplejson python3-module-babel
BuildPreReq: python-module-pytz
%endif

%py_provides %oname
#py_requires google.appengine
%py_requires webob jinja2 mako babel pytz

%description
webapp2 is a lightweight Python web framework compatible with Google App
Engine's webapp.

webapp2 is simple. it follows the simplicity of webapp, but improves it
in some ways: it adds better URI routing and exception handling, a full
featured response object and a more flexible dispatching mechanism.

webapp2 also offers the package webapp2_extras with several optional
utilities: sessions, localization, internationalization, domain and
subdomain routing, secure cookies and others.

webapp2 can also be used outside of Google App Engine, independently of
the App Engine SDK.

%if_with python3
%package -n python3-module-%oname
Summary: Taking Google App Engine's webapp to the next level!
Group: Development/Python3
%py3_provides %oname
#py3_requires google.appengine
%py3_requires webob jinja2 mako babel pytz

%description -n python3-module-%oname
webapp2 is a lightweight Python web framework compatible with Google App
Engine's webapp.

webapp2 is simple. it follows the simplicity of webapp, but improves it
in some ways: it adds better URI routing and exception handling, a full
featured response object and a more flexible dispatching mechanism.

webapp2 also offers the package webapp2_extras with several optional
utilities: sessions, localization, internationalization, domain and
subdomain routing, secure cookies and others.

webapp2 can also be used outside of Google App Engine, independently of
the App Engine SDK.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
webapp2 is a lightweight Python web framework compatible with Google App
Engine's webapp.

webapp2 is simple. it follows the simplicity of webapp, but improves it
in some ways: it adds better URI routing and exception handling, a full
featured response object and a more flexible dispatching mechanism.

webapp2 also offers the package webapp2_extras with several optional
utilities: sessions, localization, internationalization, domain and
subdomain routing, secure cookies and others.

webapp2 can also be used outside of Google App Engine, independently of
the App Engine SDK.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
webapp2 is a lightweight Python web framework compatible with Google App
Engine's webapp.

webapp2 is simple. it follows the simplicity of webapp, but improves it
in some ways: it adds better URI routing and exception handling, a full
featured response object and a more flexible dispatching mechanism.

webapp2 also offers the package webapp2_extras with several optional
utilities: sessions, localization, internationalization, domain and
subdomain routing, secure cookies and others.

webapp2 can also be used outside of Google App Engine, independently of
the App Engine SDK.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
#python run_tests.py
%if_with python3
pushd ../python3
python3 setup.py test -v
#python3 run_tests.py
popd
%endif

%files
%doc AUTHORS CHANGES README TODO example experimental
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README TODO example experimental
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.hg20140602
- Initial build for Sisyphus

