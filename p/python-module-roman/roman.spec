%define oname roman

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.1
Summary: Integer to Roman numerals converter
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/roman/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Integer to Roman numerals converter.

%package -n python3-module-%oname
Summary: Integer to Roman numerals converter
Group: Development/Python3

%description -n python3-module-%oname
Integer to Roman numerals converter.

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

%files
%doc CHANGES.txt PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

