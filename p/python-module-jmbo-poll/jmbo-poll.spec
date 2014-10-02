%define oname jmbo-poll

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20140408
Summary: Polling app for Jmbo
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-poll/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-poll.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Polling app for Jmbo.

%package -n python3-module-%oname
Summary: Polling app for Jmbo
Group: Development/Python3

%description -n python3-module-%oname
Polling app for Jmbo.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140408
- Initial build for Sisyphus

