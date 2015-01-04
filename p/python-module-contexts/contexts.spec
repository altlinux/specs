%define oname contexts

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.10.1
Release: alt1.git20141112
Summary: Descriptive testing for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Contexts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benjamin-hodgson/Contexts.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-colorama
%endif
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-colorama
%endif

%py_provides %oname
%py_requires colorama

%description
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

%package -n python3-module-%oname
Summary: Descriptive testing for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires colorama

%description -n python3-module-%oname
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%if_with python2
%python_install
%endif

%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.md RELEASING
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md RELEASING
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20141112
- Initial build for Sisyphus

