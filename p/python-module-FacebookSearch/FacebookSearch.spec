%define oname FacebookSearch

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20131203.1
Summary: A Python library to easily iterate public information found by the Facebook Graph API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/FacebookSearch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ckoepp/FacebookSearch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This library is in a very early stage of development and due to this
there no documentation available (besides the source itself :p).

%package -n python3-module-%oname
Summary: A Python library to easily iterate public information found by the Facebook Graph API
Group: Development/Python3

%description -n python3-module-%oname
This library is in a very early stage of development and due to this
there no documentation available (besides the source itself :p).

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20131203.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20131203
- Initial build for Sisyphus

