%define version 0.10.0
%define release alt1.2
%setup_python_module Nevow

Name: %packagename
Version:%version
Release: %release.1
BuildArch: noarch

Summary: Web Application Construction Kit
License: MIT
Group: Development/Python
Packager: Alexey Shabalin <shaba@altlinux.ru>
Url: http://divmod.org/trac/wiki/Divmod%{modulename}

Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/%modulename-%version.tar.gz
Patch1: Nevow-0.10.0-fix-twisted.plugins.patch

BuildPreReq: rpm-build-python
BuildRequires: python-module-Cython python-module-twisted python-module-twisted-core-gui python-module-twisted-core-test
BuildRequires: python-devel python-module-setuptools
BuildPreReq: python-module-zope.interface

Requires: python-module-twisted-web python-module-twisted-core-gui

%description

Divmod Nevow is a web application construction kit written in Python. It is
designed to allow the programmer to express as much of the view logic as
desired in Python, and includes a pure Python XML expression syntax named stan
to facilitate this. However it also provides rich support for designer-edited
templates, using a very small XML attribute language to provide bi-directional
template manipulation capability.

Nevow also includes Divmod Athena, a "two way web" or "`COMET`_"
implementation, providing a two-way bridge between Python code on the server
and JavaScript code on the client.  Modular portions of a page, known as
"athena fragments" in the server python and "athena widgets" in the client
javascript, can be individually developed and placed on any Nevow-rendered page
with a small template renderer.  Athena abstracts the intricacies of HTTP
communication, session security, and browser-specific bugs behind a simple
remote-method-call interface, where individual widgets or fragments can call
remote methods on their client or server peer with one method: "callRemote".

%prep
%setup -q -n %modulename-%version
%patch1 -p1

%build
%python_build

%install
%python_install
install -D -p -m 0644 doc/man/nevow-xmlgettext.1 %buildroot%_man1dir/nevow-xmlgettext.1

%files
%_bindir/*
%python_sitelibdir/Nevow-*.egg-info
%python_sitelibdir/nevow/
%python_sitelibdir/formless/
%python_sitelibdir/twisted/plugins/*.py*
%doc README LICENSE doc
%_man1dir/*
%exclude %_prefix/doc

#%%exclude %_bindir/*

%changelog
* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.0-alt1.2.1
- Rebuild with Python-2.7

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1.2
- added python-module-twisted-core-test to buildrqs

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.1
- Added requirements on python-module-twisted-web and
  python-module-twisted-core-gui (ALT #23198)

* Tue Mar 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.33-alt3.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Alexey Shabalin <shaba@altlinux.ru> 0.9.33-alt3
- apply patch by repocop fix for pkg-contains-cvs-or-svn-control-dir

* Mon Nov 09 2009 Alexey Shabalin <shaba@altlinux.ru> 0.9.33-alt2
- update buildreq

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.9.33-alt1
- 0.9.33
- build as noarch

* Mon Nov 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.9.31-alt1
- first build for Sisyphus
- thx to aris@ for spec 


