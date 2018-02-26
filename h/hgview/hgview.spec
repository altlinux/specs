Name: hgview
Version: 1.2.1
Release: alt1.1

Summary: Qt4 based Mercurial log navigator
License: GPLv2+
Group: Development/Tools

BuildArch: noarch

Url: http://www.logilab.org/project/hgview
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

%setup_python_module hgviewlib
%py_requires mx.DateTime
Requires: python-module-qscintilla2-qt4

BuildPreReq: mercurial mercurial-hgext asciidoc xmlto python-module-PyQt4

%description
hgview is a simple tool aiming at visually navigate in a Mercurial repository
history.
It is written in Python/Qt4 with quick and efficient key-based navigation in
mind, trying to be fast enough to be usable for big repositories.

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/hgext/
%python_sitelibdir/hgviewlib/
%python_sitelibdir/*.egg-info
%_man1dir/*
%doc ChangeLog README

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1
- Rebuild with Python-2.7

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.2.0-alt1
- initial build
