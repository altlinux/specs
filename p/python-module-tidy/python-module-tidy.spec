%define version 0.2
%define release alt2
%define srcname uTidylib
%setup_python_module tidy

Summary: Wrapper for HTML Tidy at http://tidy.sourceforge.net
Name: %packagename
Version: %version
Release: %release.1
Source0: %srcname-%version.tar.bz2
License: MIT
Group: Development/Python
Prefix: %prefix
BuildArchitectures: noarch
URL: http://utidylib.sf.net
Packager: Python Development Team <python@packages.altlinux.org>

%py_requires ctypes

%description
A wrapper for the relocatable version of HTML Tidy (see
http://tidy.sourceforge.net for details).  This allows you to
tidy HTML files through a Pythonic interface.

%prep
%setup  -q -n %srcname-%version

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 0.2-alt1
- Initial build for ALT Linux.
