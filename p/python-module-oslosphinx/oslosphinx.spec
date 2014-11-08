%define oname oslosphinx

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.2.0
Release: alt1.git20141011
Summary: OpenStack Sphinx Extensions and Theme
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/oslosphinx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/openstack/oslosphinx.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: git
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pbr python-module-sphinx-devel
#BuildPreReq: python-module-hacking
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pbr python3-module-sphinx
#BuildPreReq: python3-module-hacking
%endif

%py_provides %oname

%description
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package -n python3-module-%oname
Summary: OpenStack Sphinx Extensions and Theme
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Theme and extension support for Sphinx documentation from the OpenStack
project.

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
%python_install
mv %buildroot%python_sitelibdir/%oname-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/%oname-py%_python_version.egg-info

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/%oname-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/%oname-py%_python3_version.egg-info
%endif

pushd doc
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20141011
- Initial build for Sisyphus

