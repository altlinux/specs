%define oname fuse
%define version 0.2.1
#define cvsdate 20091102
%define release alt2
%setup_python_module %oname

Summary: This is a Python interface to FUSE
Name: python-module-%oname
Version: %version
Release: %release.1
Url: http://sourceforge.net/projects/fuse/
Source0: python-%modulename.tar.bz2
License: LGPL
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>

BuildPreReq: libfuse-devel

%description
This is a Python interface to FUSE.

FUSE (Filesystem in USErspace) is a simple interface for userspace
programs to export a virtual filesystem to the linux kernel.  FUSE
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

%prep
%setup

%build
%python_build_debug

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc AUTHORS COPYING FAQ README.* example Changelog

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Rebuilt for debuginfo

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Version 0.2.1

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.cvs20091102
- Version 0.2 (ALT #22414)

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt0.cvs20060425.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt0.cvs20060425.1
- Rebuilt with python-2.5.

* Wed Apr 26 2006 Ivan Fedorov <ns@altlinux.ru> 0.1-alt0.cvs20060425
- Initial build for ALT Linux.
