%define oname phonenumbers

%def_with python3

Name: python-module-%oname
Version: 7.0.1
Release: alt1.git20141126.1
Summary: Python port of Google's libphonenumber
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/phonenumbers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/daviddrysdale/python-phonenumbers.git
# branch: dev
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Python version of Google's common library for parsing, formatting,
storing and validating international phone numbers.

%package -n python3-module-%oname
Summary: Python port of Google's libphonenumber
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python version of Google's common library for parsing, formatting,
storing and validating international phone numbers.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md python/HISTORY
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md python/HISTORY
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.0.1-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.1-alt1.git20141126
- Version 7.0.1

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.0-alt1.git20141102
- Version 7.0.0

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1.git20141026
- Initial build for Sisyphus

