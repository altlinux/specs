%define oname eggtestinfo

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt2.1.1

Summary: Add test information to .egg-info
License: ZPL
Group: Development/Python

Url: https://pypi.python.org/pypi/eggtestinfo

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
This package is a setuptools plugin: it adds a file to the generated
.egg-info directory, capturing the information used by the setup.py test
command when running tests.

%package -n python3-module-%oname
Summary: Add test information to .egg-info
Group: Development/Python3

%description -n python3-module-%oname
This package is a setuptools plugin: it adds a file to the generated
.egg-info directory, capturing the information used by the setup.py test
command when running tests.

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt2.1
- NMU: Use buildreq for BR.

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added module for Python 3

* Sat Apr 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

