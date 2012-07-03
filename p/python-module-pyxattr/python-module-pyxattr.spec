Name: python-module-pyxattr
Version: 0.5.0
Release: alt1.1.1.1

Summary: A python module for accessing filesystem Extended Attributes

License: LGPLv2.1
Group: Development/Python
Url: http://pyxattr.sourceforge.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Python Development Team <python@packages.altlinux.org>

%setup_python_module pyxattr

BuildPreReq: libattr-devel

%description
This is the pyxattr module, a Python extension module which gives access
to the extended attributes for filesystem objects available in some
operating systems.

%prep
%setup
%patch -p1

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*
%doc NEWS README

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.1
- Rebuilt for debuginfo

* Sun Jul 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt1
- 0.5.0
- spec fixes

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.2.1-alt1.1
- Rebuilt with python-2.5.

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
