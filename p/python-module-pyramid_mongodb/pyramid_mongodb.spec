%define oname pyramid_mongodb

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt2
Summary: Pyramid application template for a traversal-based URL mapping and MongoDB project
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_mongodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid pymongo

%description
pyramid_mongodb is a simple Paster template or scaffold for the Pyramid
Web Framework. It provides URL mapping via traversal and persistence via
MongoDB. It is based on the "starter" template included in Pyramid core,
and Mike Orr's "Akhet" template.

%package -n python3-module-%oname
Summary: Pyramid application template for a traversal-based URL mapping and MongoDB project
Group: Development/Python3
%py3_requires pyramid pymongo

%description -n python3-module-%oname
pyramid_mongodb is a simple Paster template or scaffold for the Pyramid
Web Framework. It provides URL mapping via traversal and persistence via
MongoDB. It is based on the "starter" template included in Pyramid core,
and Mike Orr's "Akhet" template.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc *.txt README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt README
%python3_sitelibdir/*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

