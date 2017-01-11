%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname selenium

%def_with python3

Name: python-module-%oname
Version: 3.0.2
#Release: alt1.1
Summary: Python bindings for Selenium
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/selenium/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/0c/42/20c235e604bf736bc970c1275a78c4ea28c6453a0934002f95df9c49dad0/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
Python language bindings for Selenium WebDriver.

The selenium package is used automate web browser interaction from
Python.

%package -n python3-module-%oname
Summary: Python bindings for Selenium
Group: Development/Python3

%description -n python3-module-%oname
Python language bindings for Selenium WebDriver.

The selenium package is used automate web browser interaction from
Python.

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

find %buildroot -type f -name '*.so' -exec rm -f '{}' +

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.47.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.47.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.47.0-alt1
- Version 2.47.0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.44.0-alt1
- Version 2.44.0

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.43.0-alt1
- Initial build for Sisyphus

