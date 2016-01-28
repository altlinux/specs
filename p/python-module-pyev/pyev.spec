%define oname pyev

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt1.1
Summary: Python libev interface
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pyev/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-module-setuptools libev-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-ctypes python-modules-email python3 python3-base
BuildRequires: libev-devel python-devel python3-devel rpm-build-python3

%description
Python libev interface.

%package -n python3-module-%oname
Summary: Python libev interface
Group: Development/Python3

%description -n python3-module-%oname
Python libev interface.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python libev interface.

This package contains documentation for %oname.

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

%files docs
%doc doc/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

