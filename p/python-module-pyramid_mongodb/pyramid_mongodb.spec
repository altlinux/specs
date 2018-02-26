%define oname pyramid_mongodb
Name: python-module-%oname
Version: 1.0
Release: alt1.1
Summary: Pyramid application template for a traversal-based URL mapping and MongoDB project
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_mongodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid pymongo

%description
pyramid_mongodb is a simple Paster template or scaffold for the Pyramid
Web Framework. It provides URL mapping via traversal and persistence via
MongoDB. It is based on the "starter" template included in Pyramid core,
and Mike Orr's "Akhet" template.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt README
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

