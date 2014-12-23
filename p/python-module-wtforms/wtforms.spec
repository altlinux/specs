%define oname wtforms

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1.dev.git20141210
Summary: A flexible forms validation and rendering library for python web development
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/WTForms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wtforms/wtforms.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-ordereddict python-module-babel
BuildPreReq: python-module-sphinx-devel python-module-dateutil
BuildPreReq: python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-babel python3-module-dateutil
%endif

%description
WTForms is a flexible forms validation and rendering library for python
web development.

To get started using WTForms, we recommend reading the crash course on
the website: http://wtforms.simplecodes.com/.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
WTForms is a flexible forms validation and rendering library for python
web development.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
WTForms is a flexible forms validation and rendering library for python
web development.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: A flexible forms validation and rendering library for python web developmen
Group: Development/Python3

%description -n python3-module-%oname
WTForms is a flexible forms validation and rendering library for python
web development.

To get started using WTForms, we recommend reading the crash course on
the website: http://wtforms.simplecodes.com/.

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

%files
%doc *.txt *.rst *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.git20141210
- New snapshot

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.git20140718
- Initial build for Sisyphus

