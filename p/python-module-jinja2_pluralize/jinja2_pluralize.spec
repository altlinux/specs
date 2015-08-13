%define oname jinja2_pluralize

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20140709
Summary: Jinja2 pluralize filters
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jinja2_pluralize
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/audreyr/jinja2_pluralize.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jinja2 python-module-inflect
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jinja2 python3-module-inflect
%endif

%py_provides %oname
%py_requires jinja2 inflect

%description
Jinja2 pluralize filters.

%if_with python3
%package -n python3-module-%oname
Summary: Jinja2 pluralize filters
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2 inflect

%description -n python3-module-%oname
Jinja2 pluralize filters.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Jinja2 pluralize filters.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Jinja2 pluralize filters.

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

%make docs
%make -C docs pickle
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140709
- Initial build for Sisyphus

