%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname argparse_tools

%def_with python3

Name: python-module-%oname
Version: 1.0.6
Release: alt1
Summary: Share a standardized set of argparse arguments within your codebase
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/argparse_tools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/adgaudio/argparse_tools.git
Source0: https://pypi.python.org/packages/2a/e3/71c4febc0bcf2d37ead2da1fe584ebf0d9f33c889f3d8d8f06d8de16bb05/%{oname}-%{version}.zip
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-test
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-test
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-setuptools
BuildRequires: python-module-nose python-module-pytest python3-module-nose python3-module-pytest rpm-build-python3 time

%description
This package wraps argparse to facilitate sharing a standardized set of
arguments across various scripts and applications that may use argparse.

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
This package wraps argparse to facilitate sharing a standardized set of
arguments across various scripts and applications that may use argparse.

This package contains examples for %oname.

%package -n python3-module-%oname
Summary: Share a standardized set of argparse arguments within your codebase
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package wraps argparse to facilitate sharing a standardized set of
arguments across various scripts and applications that may use argparse.

%package -n python3-module-%oname-examples
Summary: Examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
This package wraps argparse to facilitate sharing a standardized set of
arguments across various scripts and applications that may use argparse.

This package contains examples for %oname.

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

%check
nosetests
#if_with python3
%if 0
pushd ../python3
nosetests3
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.dev0.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.dev0.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.dev0.git20150126
- Initial build for Sisyphus

