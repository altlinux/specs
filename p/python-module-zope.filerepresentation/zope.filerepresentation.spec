%define oname zope.filerepresentation
Name: python-module-%oname
Version: 3.6.1
Release: alt1
Summary: File-system Representation Interfaces
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.filerepresentation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface

%description
File-system representation interfaces.

The interfaces defined here are used for file-system and
file-system-like representations of objects, such as file-system
synchronization, FTP, PUT, and WebDAV.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

