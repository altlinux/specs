%define tarname tocmacro
Name: python-module-trac-tocmacro
%define r_minor r13602
Version: 11.0.0.4
Release: alt1.%r_minor

Summary: The TocMacro generates a table of contents for the current page or a set of pages

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/TocMacro

# http://trac-hacks.org/svn/tocmacro/0.11/
Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
The TocMacro generates a table of contents for the current page or a set of pages

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

chmod -R a+r %buildroot%python_sitelibdir/tractoc

%files
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.0.0.4-alt1.r13602
- Version 11.0.0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 11.0.0.3-alt1.r7916.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 11.0.0.3-alt1.r7916
- Build for ALT
