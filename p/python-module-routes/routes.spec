%define oname routes
Name: python-module-%oname
Version: 1.12.3
Release: alt1.hg20100605.1
Summary: Routing Recognition and Generation Tools
License: BSD
Group: Development/Python
Url: http://routes.groovie.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://bitbucket.org/bbangert/routes/
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx python-module-Pygments

%description
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate URLs.
Routes makes it easy to create pretty and concise URLs that are RESTful
with little effort.

Routes allows conditional matching based on domain, cookies, HTTP
method, or a custom function. Sub-domain support is built in. Routes
comes with an extensive unit test suite.

%package doc
Summary: Documentation for Routing Recognition and Generation Tools
Group: Development/Documentation
BuildArch: noarch

%description doc
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate URLs.
Routes makes it easy to create pretty and concise URLs that are RESTful
with little effort.

This package contains documentation for Routes.

%prep
%setup

%build
%python_build

pushd docs
%make_build html
popd

%install
%python_install

install -d %buildroot%_docdir/%name
cp -fR docs/_build/html/* %buildroot%_docdir/%name/

%files
%doc CHANGELOG LICENSE README TODO
%python_sitelibdir/*

%files doc
%_docdir/%name

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12.3-alt1.hg20100605.1
- Rebuild with Python-2.7

* Wed Jul 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.3-alt1.hg20100605
- Version 1.12.3

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20090928.1
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20090928
- Initial build for Sisyphus

