%define oname oslotest

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1.git20141105
Summary: OpenStack test framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslotest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack/oslotest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-pbr python-module-discover
BuildPreReq: python-module-fixtures python-module-subunit
BuildPreReq: python-module-six python-module-testrepository
BuildPreReq: python-module-testscenarios python-module-testtools
BuildPreReq: python-module-mock python-module-mox3
BuildPreReq: python-module-hacking python-module-coverage
BuildPreReq: python-module-mimeparse python-module-mccabe
BuildPreReq: python-module-flake8 pyflakes
BuildPreReq: python-module-sphinx-devel python-module-oslosphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pbr python3-module-discover
BuildPreReq: python3-module-fixtures python3-module-subunit
BuildPreReq: python3-module-six python3-module-testrepository
BuildPreReq: python3-module-testscenarios python3-module-testtools
BuildPreReq: python3-module-mock python3-module-mox3
BuildPreReq: python3-module-hacking python3-module-coverage
BuildPreReq: python3-module-mimeparse python3-module-mccabe
BuildPreReq: python3-module-flake8 python3-pyflakes
BuildPreReq: python3-module-sphinx python3-module-oslosphinx
%endif

%py_provides %oname

%description
OpenStack test framework and test fixtures.

%package -n python3-module-%oname
Summary: OpenStack test framework
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
OpenStack test framework and test fixtures.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
OpenStack test framework and test fixtures.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
OpenStack test framework and test fixtures.

This package contains documentation for %oname.

%prep
%setup

git init-db
git config user.email "real at altlinux.org"
git config user.name "REAL"
git add . -A
git commit -a -m "commit"
git tag %version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

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
	sed -i 's|python|python3|g' $i
	mv $i $i.py3
done
popd
mv %buildroot%python3_sitelibdir/%oname-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-py%_python3_version.egg-info
%endif

%python_install
mv %buildroot%python_sitelibdir/%oname-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-py%_python_version.egg-info

export PYTHONPATH=$PWD
pushd doc
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

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
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141105
- Initial build for Sisyphus

