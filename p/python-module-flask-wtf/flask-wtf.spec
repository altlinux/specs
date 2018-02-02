%define oname flask-wtf

%def_with python3

Name: python-module-%oname
Version: 0.14.2
Release: alt1.1
Summary: Simple integration of Flask and WTForms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-WTF/

# https://github.com/lepture/flask-wtf.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
Patch2: %oname-%version-upstream-sphinx.patch

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-flask
BuildRequires: python-module-werkzeug python-module-wtforms
BuildRequires: python-module-flask-babel python-module-speaklater
BuildRequires: python-module-sphinx-devel
BuildRequires: flask-sphinx-themes
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-flask
BuildRequires: python3-module-werkzeug python3-module-wtforms
BuildRequires: python3-module-flask-babel python3-module-speaklater
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
%patch1 -p1
%patch2 -p1

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

PYTHONPATH=$(pwd) %make -C docs pickle
PYTHONPATH=$(pwd) %make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test ||:
%if_with python3
pushd ../python3
py.test3 ||:
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.14.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.2-alt1
- Updated to upstream version 0.14.2.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20141005
- Initial build for Sisyphus

