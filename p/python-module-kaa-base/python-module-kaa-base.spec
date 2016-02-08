%define oname kaa-base

%def_with python3

Name: python-module-%oname
Version: 0.99.2
Release: alt2.git20130522

Summary: Base module for all Kaa modules

License: LGPL
Group: Development/Python
Url: http://freevo.org/kaa

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

Source: %name-%version.tar

# Automatically added by buildreq on Sat May 26 2007
BuildRequires: glib2-devel python-devel python-module-PyXML python-modules-compiler

BuildPreReq: python-modules-sqlite3
BuildPreReq: python-module-dbus python-module-avahi
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

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

%package -n python3-module-%oname
Summary: Base module for all Kaa modules
Group: Development/Python3
%add_python3_req_skip avahi

%description -n python3-module-%oname
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
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir

install -d %buildroot%python_sitelibdir/%oname

%files
%python_sitelibdir/kaa/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/kaa/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 0.99.2-alt2.git20130522
- Disabled Doc, Pickle and Sphinx

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.2-alt1.git20130522
- Version 0.99.2
- Added module for Python 3

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

