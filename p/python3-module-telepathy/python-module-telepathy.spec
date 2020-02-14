%define oname telepathy

Name: python3-module-%oname
Version: 0.15.19
Release: alt4

Summary: Python bindings for telepathy library
License: LGPL 2.1 or later
Group: Development/Python3
URL: http://telepathy.freedesktop.org/
BuildArch: noarch

Source0: http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%version.tar.gz
#Upstream git commit 0c4e6e9f41b24bbb7ea33653b8a81ff79c0ea032
Patch: python-telepathy-0.15.19-autotools.patch
Patch1: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 xsltproc

Requires: python3-module-dbus >= 0.80


%description
Telepathy python bindings for use with python programs.

%prep
%setup -n telepathy-python-%version
%patch -p1
%patch1 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
#define __libtoolize true
#autoreconf
%configure \
	am_cv_python_pythondir=%python3_sitelibdir \
	am_cv_python_pyexecdir=%python3_sitelibdir

%install
%makeinstall_std

%files
%doc AUTHORS README examples
%python3_sitelibdir/*


%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.15.19-alt4
- Porting on Python3.

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.15.19-alt3
- bugfix (closes: #27962); added patch from fedora.

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.19-alt2
- Fixed build with make 3.82

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.19-alt1.1
- Rebuild with Python-2.7

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.19-alt1
- Version 0.15.19 (ALT #22793)

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.18-alt1
- Version 0.15.18

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.17-alt1
- Version 0.15.17

* Thu Mar 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.16-alt1
- Version 0.15.16

* Thu Jan 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.15-alt1
- Version 0.15.15 (ALT #22793)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.12-alt2
- Rebuilt with python 2.6

* Fri Nov 20 2009 Aleksey Lim <alsroot@altlinux.org> 0.15.12-alt1
- Update version to 0.15.12

* Mon Jul 06 2009 Aleksey Lim <alsroot@altlinux.org> 0.15.7-alt1
- Update version to 0.15.7

* Sun Jan 18 2009 Aleksey Lim <alsroot@altlinux.org> 0.15.6-alt2
- add URL tag

* Sun Jan 18 2009 Aleksey Lim <alsroot@altlinux.org> 0.15.6-alt1
- New upstream release

* Tue Nov 11 2008 Aleksey Lim <alsroot@altlinux.org> 0.15.3-alt1
- New upstream release

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.14.0-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 0.14.0-alt2
- fix build on x86_64

* Sun Oct 14 2007 Igor Zubkov <icesik@altlinux.org> 0.14.0-alt1
- build for Sisyphus

