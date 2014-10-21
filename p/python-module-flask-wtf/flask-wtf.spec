%define oname flask-wtf

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.10.2
Release: alt1.git20141005
Summary: Simple integration of Flask and WTForms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-WTF/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lepture/flask-wtf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-flask
BuildPreReq: python-module-werkzeug python-module-wtforms
BuildPreReq: python-module-flask-babel python-module-speaklater
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-flask
BuildPreReq: python3-module-werkzeug python3-module-wtforms
BuildPreReq: python3-module-flask-babel python3-module-speaklater
%endif

%py_provides flask_wtf

%description
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

%package -n python3-module-%oname
Summary: Simple integration of Flask and WTForms
Group: Development/Python3
%py3_provides flask_wtf

%description -n python3-module-%oname
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

This package comtains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

This package comtains documentation for %oname.

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

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20141005
- Initial build for Sisyphus

