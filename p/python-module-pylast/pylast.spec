%define oname pylast

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20140825.1.1
Summary: A Python interface to Last.fm (and other API compatible social networks)
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pylast/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pylast/pylast.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
A Python interface to Last.fm and other api-compatible websites such as
Libre.fm.

%package -n python3-module-%oname
Summary: A Python interface to Last.fm (and other API compatible social networks)
Group: Development/Python3

%description -n python3-module-%oname
A Python interface to Last.fm and other api-compatible websites such as
Libre.fm.

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
%doc *.yaml *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.yaml *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20140825.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20140825.1
- NMU: Use buildreq for BR.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140825
- Initial build for Sisyphus

