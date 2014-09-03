%define tarname tagsplugin
Name: python-module-trac-tagsplugin
%define r_minor r14146
Version: 0.8
Release: alt1.%r_minor

Summary: Tagging System for Trac

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/TagsPlugin

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
The TagsPlugin implements both a generic tagging engine, and frontends for the
Wiki and ticket systems. An extra text entry box is added to the Wiki edit page
for tagging Wiki pages, and ticket fields (you can configure which ones)
are treated as tags for the ticket system

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

chmod -R a+r %buildroot%python_sitelibdir/tractags

%files
%doc changelog
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.r14146
- Version 0.8

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.r7906.1
- Rebuild with Python-2.7

* Fri Apr 30 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6-alt1.r7906
- Build for ALT

