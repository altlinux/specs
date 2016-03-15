%define oname oauth2

%def_with python3

Name: python-module-%oname
Version: 1.5.211
Release: alt1.1
Summary: Library for OAuth version 1.0a (forked from python-oauth)

Group: Development/Python
License: MIT
Url: https://github.com/simplegeo/python-oauth2
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
python-oauth2 implements OAuth, which is an open protocol to allow API
authentication in a simple and standard method from desktop and web 
applications. This was forked from python-oauth.

%package -n python3-module-%oname
Summary: Library for OAuth version 1.0a (forked from python-oauth)
Group: Development/Python3

%description -n python3-module-%oname
python-oauth2 implements OAuth, which is an open protocol to allow API
authentication in a simple and standard method from desktop and web 
applications. This was forked from python-oauth.

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
rm -rf %buildroot/%python_sitelibdir/tests

%if_with python3
pushd ../python3
%python3_install
popd
rm -rf %buildroot/%python3_sitelibdir/tests
%endif

%files
%doc LICENSE.txt README.md example/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt README.md example/
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.211-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.211-alt1
- Version 1.5.211
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.170-alt2
- Rebuild with Python-2.7

* Mon Jun 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.170-alt1
- 1.5.170

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.165-alt1
- Initial
