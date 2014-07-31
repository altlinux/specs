%define oname pyramid-openid

%def_with python3

Name: python-module-%oname
Version: 0.3.4
Release: alt2
Summary: A view for pyramid that functions as an OpenID consumer
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid-openid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires pyramid

%description
pyramid_openid provides a view for the Pyramid framework that acts as an
OpenID consumer.

%package -n python3-module-%oname
Summary: A view for pyramid that functions as an OpenID consumer
Group: Development/Python3
%py3_requires pyramid

%description -n python3-module-%oname
pyramid_openid provides a view for the Pyramid framework that acts as an
OpenID consumer.

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

