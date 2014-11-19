%define oname jmbo-contact

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20141107
Summary: Jmbo contact form app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-contact/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-contact.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Jmbo contact form app.

%package -n python3-module-%oname
Summary: Jmbo contact form app
Group: Development/Python3

%description -n python3-module-%oname
Jmbo contact form app.

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
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141107
- Version 0.1.2

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20120801
- Initial build for Sisyphus

