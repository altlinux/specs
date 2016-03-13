%define oname datastreams

%def_with python3

Name: python-module-%oname
Version: 0.2.6
Release: alt1.git20150113.1.1
Summary: A module for managing data in streams
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/datastreams/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/csu/datastreams.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pymongo python-modules-wsgiref
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pymongo
%endif

%py_provides %oname
%py_requires pymongo wsgiref

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
A module for managing data in streams.

%package -n python3-module-%oname
Summary: A module for managing data in streams
Group: Development/Python3
%py3_provides %oname
%py3_requires pymongo wsgiref

%description -n python3-module-%oname
A module for managing data in streams.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.6-alt1.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1.git20150113.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20150113
- Initial build for Sisyphus

