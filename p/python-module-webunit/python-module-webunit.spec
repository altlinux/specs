Name: python-module-webunit
Version: 1.3.10
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Unit test your websites with code that acts like a web browser
License: BSD
Group: Development/Python

Url: http://pypi.python.org/pypi/webunit
Source: http://pypi.python.org/packages/source/w/webunit/webunit-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 11 2010
BuildRequires: python-devel

%description
Webunit is a framework for unit testing websites:

 * Browser-like page fetching including fetching the images and stylesheets needed for a page and following redirects
 * Cookies stored and trackable (all automatically handled)
 * HTTP, HTTPS, GET, POST, basic auth all handled, control over expected status codes, ...
 * DOM parsing of pages to retrieve and analyse structure, including simple form re-posting
 * Two-line page-fetch followed by form-submit possible, with error checking
 * Ability to register error page content across multiple tests
 * Uses python's standard unittest module as the underlying framework
 * May also be used to regression-test sites, or ensure their ongoing operation once in production

%prep
%setup -n webunit-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/webunit*
%exclude %python_sitelibdir/demo

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.10-alt1.1
- Rebuild with Python-2.7

* Mon Oct 11 2010 Victor Forsiuk <force@altlinux.org> 1.3.10-alt1
- 1.3.10

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 1.3.9-alt1
- Initial build.
