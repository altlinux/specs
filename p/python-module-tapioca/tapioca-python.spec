%define oname tapioca-python

Name: python-module-tapioca
Version: 0.14.1.0
Release: alt1.2.1.1

Summary: Python binding for Tapioca
License: GPLv2
Group: Development/Python
Url: http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca

# https://tapioca-voip.svn.sourceforge.net/svnroot/tapioca-voip/trunk
Source0: %oname-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu Jul 03 2008
BuildRequires: gcc-c++ python-module-pygtk-devel tapioca-glib-devel
BuildPreReq: libnumpy-devel gcc-fortran python-module-pygobject-devel
BuildPreReq: python-devel

%description
Python binding for Tapioca.

%prep
%setup

%build
export LIBS=-lpython%_python_version
%add_optflags -I%_includedir/numpy
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

#ifarch x86_64
#install -d %buildroot%python_sitelibdir
#mv %buildroot%python_sitelibdir_noarch/* \
#	%buildroot%python_sitelibdir/
#endif

%files
%doc AUTHORS ChangeLog NEWS README
%dir %python_sitelibdir/tapioca-0.14
%python_sitelibdir/tapioca-0.14/
%python_sitelibdir/pytapioca.pth

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14.1.0-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14.1.0-alt1.2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1.0-alt1.2
- Rebuilt for debuginfo

* Thu Feb 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1.0-alt1.1
- Version 0.14.1.0

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0.1-alt2
- Rebuilt with reformed NumPy
- Fixed for autoconf 2.6

* Fri Jan 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0.1-alt1
- Version 0.14.0.1

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt3
- Rebuilt with python 2.6

* Thu Jul 03 2008 Igor Zubkov <icesik@altlinux.org> 0.14.0-alt2
- rename

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 0.14.0-alt1
- build for Sisyphus

