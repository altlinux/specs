Name: hgview
Version: 1.9.0
Release: alt1

Summary: Qt4 based Mercurial log navigator
License: GPLv2+
Group: Development/Tools

BuildArch: noarch

Url: http://www.logilab.org/project/hgview
# hg clone http://hg.logilab.org/review/hgview
Source0: https://pypi.python.org/packages/dd/42/a70bcd09b92c99bc38546b847d9517fd0adede2d0146099b6740f1cb2499/%{name}-%{version}.tar.gz

%setup_python_module hgviewlib
%py_requires mx.DateTime
Requires: python-module-qscintilla2-qt4

BuildPreReq: mercurial mercurial-hgext asciidoc xmlto python-module-PyQt4

%description
hgview is a simple tool aiming at visually navigate in a Mercurial
repository history.
It is written in Python/Qt4 with quick and efficient key-based
navigation in mind, trying to be fast enough to be usable for big
repositories.

%prep
%setup -q 

%build
%python_build


%install
%python_install
mv %buildroot/usr/man %buildroot/usr/share
rm -rf %buildroot/usr/share/doc/%name

%files
%_bindir/*
%python_sitelibdir/hgext/
%python_sitelibdir/hgviewlib/
%python_sitelibdir/*.egg-info
%_man1dir/*
%doc ChangeLog README

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1
- automated PyPI update

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1
- Version 1.8.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1
- Rebuild with Python-2.7

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.2.0-alt1
- initial build
