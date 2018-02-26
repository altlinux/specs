%define oname kaa-base
Name: python-module-%oname
Version: 0.4.0
Release: alt3.1.1

Summary: Base module for all Kaa modules

License: LGPL
Group: Development/Python
Url: http://freevo.org/kaa

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

BuildPreReq: rpm-build-compat >= 1.2

Source: http://prdownloads.sf.net/freevo/%oname-%version.tar.bz2

# Automatically added by buildreq on Sat May 26 2007
BuildRequires: glib2-devel python-devel python-module-PyXML python-modules-compiler

%description
This module contains some basic code needed in all kaa modules. This
is a requirement for all the other modules in the repository.

The module also contains a main loop (notifier). Some kaa modules like
kaa-Display require the main loop to be running, for other modules
like kaa-Thumb it's optional and some like kaa-Metadata don't need the
main loop at all. The documentation of the module should explain if
and why the main loop is needed. If you already have a main loop
running, please read SourceDoc/MainLoop how to merge the main loop you
use with the kaa main loop.

%prep
%setup -n %oname-%version

%build
%python_build_debug

%install
%python_install

%files
%doc AUTHORS NEWS README TODO
%python_sitelibdir/kaa/

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Rebuilt for debuginfo

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Rebuilt with python 2.6

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version 0.4.0 (with rpmrb script)
- cleanup spec

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt0.1
- initial build for ALT Linux Sisyphus

