%define oname finance

%def_with python3

Name: python-module-%oname
Version: 0.2502
Release: alt1.1

Summary: finance - Financial Risk Calculations
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/finance

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
finance - Financial Risk Calculations. Optimized for ease of use through
class construction and operator overload.

The purpose of this project is to deliver ease of use python code for
financial risk calculations. This code is not unconsious reproduction of
textbook material.

It's about developing abstract data types as objects to ease financial
calculations and code development.

At this point the code is by no means optimized for speed.

Financial and mathematical concepts are developed on the PythonHacks
homepage.

%if_with python3
%package -n python3-module-%oname
Summary: finance - Financial Risk Calculations
Group: Development/Python3

%description -n python3-module-%oname
finance - Financial Risk Calculations. Optimized for ease of use through
class construction and operator overload.

The purpose of this project is to deliver ease of use python code for
financial risk calculations. This code is not unconsious reproduction of
textbook material.

It's about developing abstract data types as objects to ease financial
calculations and code development.

At this point the code is by no means optimized for speed.

Financial and mathematical concepts are developed on the PythonHacks
homepage.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.html *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.html *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2502-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2502-alt1
- Version 0.2502

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2501-alt1
- Initial build for Sisyphus

