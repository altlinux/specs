%define oname pyramid-openid
Name: python-module-%oname
Version: 0.3.4
Release: alt1.1
Summary: A view for pyramid that functions as an OpenID consumer
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid-openid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid

%description
pyramid_openid provides a view for the Pyramid framework that acts as an
OpenID consumer.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

