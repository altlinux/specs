%define version 0.6.12a
%define release alt1
%setup_python_module basicproperty

Name: %packagename
Version: %version
Release: %release.1

Summary: Core data-types and property classes
License: BSD-style, see license.txt for details
Group: Development/Python

URL: http://basicproperty.sourceforge.net/
Packager: Sergey Alembekov <rt@altlinux.ru>

Source0: %modulename-%version.tar

BuildPreReq: %py_dependencies setuptools

%description
Core data-types and property classes

BasicProperty and BasicTypes provide the core datatypes for
both wxoo and the PyTable RDBMS Wrapper project.


%prep
%setup -n %modulename-%version

%build
rm -Rf basicproperty/propertyaccel.so
%python_build

%install
rm -Rf basicproperty/nevoo
%python_install

%files
%python_sitelibdir/basictypes/
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.12a-alt1.1
- Rebuild with Python-2.7

* Mon Mar 29 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6.12a-alt1
- 0.6.12a

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.9a-alt1.1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-basicproperty
  * postclean-05-filetriggers for spec file

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.9a-alt1.1.1
- Rebuilt with python 2.6

* Tue Feb 24 2009 Sergey Alembekov <rt@altlinux.ru> 0.6.9a-alt1.1
- fix x86_64 build

* Wed Oct 22 2008 Sergey Alembekov <rt@altlinux.ru> 0.6.9a-alt1
- Initial build for ALTLinux

