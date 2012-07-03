%define version 2.1.4
%define release alt1
%setup_python_module textile

Summary: This is Textile. A Humane Web Text Generator
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename-%version.tar.gz
License: Freely Distributable
Group: Development/Python
BuildArch: noarch
URL: http://loopcore.com/python-textile/
Packager: Python Development Team <python at packages.altlinux.org>

%description
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc PKG-INFO test

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.4-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Version 2.1.4

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.10-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.0.10-alt1.1
- Rebuilt with python-2.5.

* Thu Apr 28 2005 Ivan Fedorov <ns@altlinux.ru> 2.0.10-alt1
- Initial build for ALT Linux
