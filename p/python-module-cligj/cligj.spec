%define _unpackaged_files_terminate_build 1
%define oname cligj

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: Click params for GeoJSON CLI
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cligj/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapbox/cligj.git
Source0: https://pypi.python.org/packages/fc/53/b89c392f33aa48b3063ad49e4dab70e424659d1fc4103b28b183f477f476/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-click-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-click-tests
%endif

%py_provides %oname
%py_requires click

%description
Common arguments and options for GeoJSON processing commands, using
Click.

%package -n python3-module-%oname
Summary: Click params for GeoJSON CLI
Group: Development/Python3
%py3_provides %oname
%py3_requires click

%description -n python3-module-%oname
Common arguments and options for GeoJSON processing commands, using
Click.

%prep
%setup -q -n %{oname}-%{version}

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
export LC_ALL=en_US.UTF-8
python setup.py test
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150528
- Version 0.2.0

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141227
- Initial build for Sisyphus

