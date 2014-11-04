%define mname tzf
%define oname %mname.pyramid_yml

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20141011
Summary: Loads a yml defined configuration
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tzf.pyramid_yml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/fizyk/pyramid_yml.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid python-module-pymlconf
BuildPreReq: python-module-coverage python-module-pytest-cov
BuildPreReq: python-module-pytest_pyramid
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-pymlconf
BuildPreReq: python3-module-coverage python3-module-pytest-cov
BuildPreReq: python3-module-pytest_pyramid
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
tzf.pyramid_yml is a convenience package, that allows for a yml
settings, that can be kept in a structured, clear way, and also
extensible depending on an 'environment'.

%package -n python3-module-%oname
Summary: Loads a yml defined configuration
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR

%description -n python3-module-%oname
tzf.pyramid_yml is a convenience package, that allows for a yml
settings, that can be kept in a structured, clear way, and also
extensible depending on an 'environment'.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
tzf.pyramid_yml is a convenience package, that allows for a yml
settings, that can be kept in a structured, clear way, and also
extensible depending on an 'environment'.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
tzf.pyramid_yml is a convenience package, that allows for a yml
settings, that can be kept in a structured, clear way, and also
extensible depending on an 'environment'.

This package contains documentation for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 tzf/__init__.py %buildroot%python_sitelibdir/tzf/
%if_with python3
pushd ../python3
install -p -m644 tzf/__init__.py %buildroot%python3_sitelibdir/tzf/
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20141011
- Initial build for Sisyphus

