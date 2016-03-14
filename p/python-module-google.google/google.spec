%define oname google.google

%def_with python3

Name: python-module-%oname
Version: 1.05
Release: alt1.1
Summary: Python bindings to the Google search engine
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/google/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools dos2unix
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires google

%description
Python bindings to the Google search engine.

%package -n python3-module-%oname
Summary: Python bindings to the Google search engine
Group: Development/Python3
%py3_requires google

%description -n python3-module-%oname
Python bindings to the Google search engine.

%prep
%setup

dos2unix google.py

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/google.py %buildroot%_bindir/google.py3
install -d %buildroot%python3_sitelibdir/google
mv %buildroot%python3_sitelibdir/*.py \
	%buildroot%python3_sitelibdir/__pycache__ \
	%buildroot%python3_sitelibdir/google/
%endif

%python_install
install -d %buildroot%python_sitelibdir/google
mv %buildroot%python_sitelibdir/*.py* \
	%buildroot%python_sitelibdir/google/

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.05-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.05-alt1
- Initial build for Sisyphus

