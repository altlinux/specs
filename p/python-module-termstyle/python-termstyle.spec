%define oname termstyle

%def_with python3

Name: python-module-%oname
Version: 0.1.10
Release: alt1.1
Summary: Console colouring for python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-termstyle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
termstyle is a simple python library for adding coloured output to
terminal (console) programs. The definitions come from ECMA-048, the
"Control Functions for Coded Character Sets" standard.

%package -n python3-module-%oname
Summary: Console colouring for python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
termstyle is a simple python library for adding coloured output to
terminal (console) programs. The definitions come from ECMA-048, the
"Control Functions for Coded Character Sets" standard.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt1
- Initial build for Sisyphus

