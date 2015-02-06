%define mname tw2
%define oname %mname.forms

%def_with python3

Name: python-module-%oname
Version: 2.2.2.1
Release: alt1.git20140727
Summary: The basic form widgets for ToscaWidgets 2, a web widget toolkit
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.forms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.forms.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-jinja2 python-module-tw2.core-tests
BuildPreReq: python-module-six python-module-sieve
BuildPreReq: python-module-webob python-module-webtest
BuildPreReq: python-module-FormEncode
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-jinja2 python3-module-tw2.core-tests
BuildPreReq: python3-module-six python3-module-sieve
BuildPreReq: python3-module-webob python3-module-webtest
%endif

%py_provides %oname
%py_requires %mname genshi mako jinja2 tw2.core six webob

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.forms package contains the basic html form widgets.

%package -n python3-module-%oname
Summary: The basic form widgets for ToscaWidgets 2, a web widget toolkit
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname genshi mako jinja2 tw2.core six webob

%description -n python3-module-%oname
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.forms package contains the basic html form widgets.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/forms
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*
%python3_sitelibdir/%mname/forms
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.1-alt1.git20140727
- Initial build for Sisyphus

