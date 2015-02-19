%define oname libsass

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.3
Release: alt1.git20150205
Summary: SASS for Python: A straightforward binding of libsass for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/libsass/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dahlia/libsass-python.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ libsass-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-werkzeug
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-werkzeug
%endif

%py_provides %oname
%py_requires six

%description
This package provides a simple Python extension module sass which is
binding Libsass (written in C/C++ by Hampton Catlin and Aaron Leung).
It's very straightforward and there isn't any headache related Python
distribution/deployment.

%package -n python3-module-%oname
Summary: SASS for Python: A straightforward binding of libsass for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
This package provides a simple Python extension module sass which is
binding Libsass (written in C/C++ by Hampton Catlin and Aaron Leung).
It's very straightforward and there isn't any headache related Python
distribution/deployment.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package provides a simple Python extension module sass which is
binding Libsass (written in C/C++ by Hampton Catlin and Aaron Leung).
It's very straightforward and there isn't any headache related Python
distribution/deployment.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package provides a simple Python extension module sass which is
binding Libsass (written in C/C++ by Hampton Catlin and Aaron Leung).
It's very straightforward and there isn't any headache related Python
distribution/deployment.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls *.py); do
	mv $i ${i}3
done
mv sassc sassc3
popd
%endif

%python_install

python setup.py build_ext -i
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*3
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.git20150205
- Initial build for Sisyphus

