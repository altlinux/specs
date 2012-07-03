Name: python-module-pysvn
Version: 1.5.2
Release: alt3.2
Summary: Subversion support for python
License: Apache License
Group: Development/Python
Url: http://pysvn.tigris.org/
Packager: Gennady Kovalev <gik@altlinux.ru>
Source0: pysvn-%version.tar
Patch0: pysvn-%version-alt-allinone.patch
Patch1: pysvn-alt-no-rpath.patch
# Automatically added by buildreq on Tue Jan 01 2008
BuildRequires: gcc-c++ libcom_err-devel libexpat-devel libkrb5-devel libsubversion-devel python-devel python-modules-compiler python-modules-xml subversion

%description
The pysvn project's goal is to enable Tools to be written in Python that use Subversion.


%prep
%setup -n pysvn-%version
%patch0 -p1
%patch1 -p2


%build
cd Source
python setup.py configure --enable-debug --verbose
%make


%install
mkdir -p %buildroot%python_sitelibdir 
cp -r Source/pysvn %buildroot%python_sitelibdir


%files
%dir %python_sitelibdir/pysvn
%python_sitelibdir/pysvn/*


%changelog
* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3.2
- Removed RPATH

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt3.1
- Rebuild with Python-2.7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt3
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.5.2-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 02 2008 Gennady Kovalev <gik@altlinux.ru> 1.5.2-alt1
- Initial build

