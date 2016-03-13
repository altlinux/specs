%define oname binstr

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20110927.1.1
Summary: Utility functions for strings of binary digits
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/binstr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/DavidMcEwan/binstr.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-modules-unittest rpm-build-python3

%description
A collection of utility functions for creating and operating on strings
of binary digits. It is compatible with Python versions >2.6 including
3.x.

It is useful to use these functions to make small bugs in your code
easier to find since all inputs are checked thoroughly for errors using
assertions.

%package -n python3-module-%oname
Summary: Utility functions for strings of binary digits
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A collection of utility functions for creating and operating on strings
of binary digits. It is compatible with Python versions >2.6 including
3.x.

It is useful to use these functions to make small bugs in your code
easier to find since all inputs are checked thoroughly for errors using
assertions.

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
python binstr_test.py -v
%if_with python3
pushd ../python3
python3 binstr_test.py -v
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20110927.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20110927.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20110927
- Initial build for Sisyphus

