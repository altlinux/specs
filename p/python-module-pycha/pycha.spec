%define oname pycha

%def_without python3

Name: python-module-%oname
Version: 0.7.0
Release: alt2.1
Summary: A library for making charts with Python
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pycha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pycairo
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pycairo
%endif

%py_provides %oname

%description
Pycha is a very simple Python package for drawing charts using the great
Cairo library. Its goals are:

* Lightweight
* Simple to use
* Nice looking with default values
* Customization

%if_with python3
%package -n python3-module-%oname
Summary: A library for making charts with Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pycha is a very simple Python package for drawing charts using the great
Cairo library. Its goals are:

* Lightweight
* Simple to use
* Nice looking with default values
* Customization
%endif

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

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.txt examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endiff
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.txt examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Fixed build

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

