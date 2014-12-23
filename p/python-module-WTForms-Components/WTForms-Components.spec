%define oname WTForms-Components

%def_with python3

Name: python-module-%oname
Version: 0.9.7
Release: alt1.git20141222
Summary: Additional fields, validators and widgets for WTForms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/WTForms-Components/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/wtforms-components.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wtforms python-module-SQLAlchemy
BuildPreReq: python-module-SQLAlchemy-Utils python-module-six
BuildPreReq: python-module-validators python-module-intervals
BuildPreReq: python-module-phonenumbers python-module-colour
BuildPreReq: python-module-Pygments python-module-jinja2
BuildPreReq: python-module-docutils python-module-ipaddr
BuildPreReq: python-module-flexmock python-module-psycopg2
BuildPreReq: python-module-WTForms-Test python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wtforms python3-module-SQLAlchemy
BuildPreReq: python3-module-SQLAlchemy-Utils python3-module-six
BuildPreReq: python3-module-validators python3-module-intervals
BuildPreReq: python3-module-phonenumbers python3-module-colour
BuildPreReq: python3-module-Pygments python3-module-jinja2
BuildPreReq: python3-module-docutils python3-module-ipaddr
BuildPreReq: python3-module-flexmock python3-module-psycopg2
BuildPreReq: python3-module-WTForms-Test python3-modules-sqlite3
%endif

%py_provides wtforms_components
%py_requires validators phonenumbers colour

%description
Additional fields, validators and widgets for WTForms.

%package -n python3-module-%oname
Summary: Additional fields, validators and widgets for WTForms
Group: Development/Python3
%py3_provides wtforms_components
%py3_requires validators phonenumbers colour

%description -n python3-module-%oname
Additional fields, validators and widgets for WTForms.

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

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20141222
- Initial build for Sisyphus

