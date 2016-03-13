%define oname coards

%def_with python3

Name: python-module-%oname
Version: 1.0.5
Release: alt1.1
Summary: A parser for COADS-compliant dates
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/coards/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A COADS compliant time parser.

This module is intended to help parse time values represented using the
COARDS convention.

%package -n python3-module-%oname
Summary: A parser for COADS-compliant dates
Group: Development/Python3

%description -n python3-module-%oname
A COADS compliant time parser.

This module is intended to help parse time values represented using the
COARDS convention.

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

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus

