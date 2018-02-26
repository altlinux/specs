Name: python-module-libacl
Version: 0.5.0
Release: alt3.1.1

Summary: POSIX.1e ACLs for python
License: LGPLv2.1+
Group: Development/Python

URL: http://pylibacl.sourceforge.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Python Development Team <python@packages.altlinux.org>

BuildPreReq: libacl-devel python-module-setuptools

%description
python-libacl is a C extension module for Python which implements
POSIX ACLs manipulation. It is a wrapper on top of the systems's
acl C library - see acl(5).

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*
%doc IMPLEMENTATION NEWS PLATFORMS PORTING README

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt3
- Rebuilt for debuginfo

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt2
- fix buildreqs

* Sun Jul 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt1
- 0.5.0
- spec fixes

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.1
- Rebuilt with python 2.6

* Sat Apr 05 2008 Mikhail Pokidko <pma@altlinux.org> 0.2.1-alt1
- Initial ALT build

