%define oname geventhttpclient-facebook

%def_with python3

Name: python-module-%oname
Version: 0.4.4
Release: alt1.1
Summary: Port of the original facebook sdk to use geventhttpclient
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/geventhttpclient-facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

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
Port of the original facebook sdk to use geventhttpclient.

%package -n python3-module-%oname
Summary: Port of the original facebook sdk to use geventhttpclient
Group: Development/Python3

%description -n python3-module-%oname
Port of the original facebook sdk to use geventhttpclient.

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
%doc *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus

