%define oname inflection

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20140903
Summary: A port of Ruby on Rails inflector to Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/inflection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jpvanhal/inflection.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Inflection is a string transformation library. It singularizes and
pluralizes English words, and transforms strings from CamelCase to
underscored string. Inflection is a port of Ruby on Rails' inflector to
Python.

%package -n python3-module-%oname
Summary: A port of Ruby on Rails inflector to Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Inflection is a string transformation library. It singularizes and
pluralizes English words, and transforms strings from CamelCase to
underscored string. Inflection is a port of Ruby on Rails' inflector to
Python.

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
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140903
- Initial build for Sisyphus

