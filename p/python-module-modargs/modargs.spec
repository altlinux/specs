%define modulename modargs

%def_with python3

Name: python-module-%modulename
Version: 1.7
Release: alt2.1.1

Summary: Simple command line argument parsing library
License: Free
Group: Development/Python

Url: https://pypi.python.org/pypi/python-modargs

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
#BuildPreReq: python-tools-2to3
%endif

%setup_python_module %modulename
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

%description
modargs is a simple command line argument parsing library that infers
arguments from functions in a module.

%package -n python3-module-%modulename
Summary: Simple command line argument parsing library
Group: Development/Python3

%description -n python3-module-%modulename
modargs is a simple command line argument parsing library that infers
arguments from functions in a module.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7-alt2.1
- NMU: Use buildreq for BR.

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Version 1.7

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

