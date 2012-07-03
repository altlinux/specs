%define oname pyramid-flatpages
Name: python-module-%oname
Version: 0.0.1.mdfix
Release: alt1.1
Summary: Manage your site's pages using configurable data sources for storage
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid-flatpages/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid repoze.tm2 weberror markdown

%description
Manage your site's pages using configurable data sources for storage.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.md
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1.mdfix-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1.mdfix-alt1
- Initial build for Sisyphus

