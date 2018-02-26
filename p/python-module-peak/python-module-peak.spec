%define modulename peak
%define svnrev 2590

Name: python-module-%modulename
Version: 0.5
Release: alt2.alpha4.svn.%svnrev.1.1

Summary: the "Python Enterprise Application Kit"
License: PSF or ZPL
Group: Development/Python

Url: http://peak.telecommunity.com
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

Source: %name-%version.tar

# Automatically added by buildreq on Tue Mar 31 2009
BuildRequires: python-module-setuptools

%setup_python_module %modulename

%description
PEAK is the "Python Enterprise Application Kit". If you develop
"enterprise" applications with Python, or indeed almost any sort of
application with Python, PEAK may help you do it faster, easier, on a
larger scale, and with fewer defects than ever before. The key is
component-based development, on a reliable infrastructure.

PEAK tools can be used with other "Python Enterprise" frameworks such as
Zope, Twisted, and the Python DBAPI to construct web-based, GUI, or
command-line applications, interacting with any kind of storage, or with
no storage at all.  Whatever the application type, PEAK can help you put
it together.

%prep
%setup

%build
%python_build
   
%install
%python_install

%files
%_bindir/*
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt2.alpha4.svn.2590.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt2.alpha4.svn.2590.1
- Rebuild with Python-2.7

* Tue Jul 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.alpha4.svn.2590
- Rebuild with python 2.6

* Tue Mar 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5-alt1.alpha4.svn.2590
- Initial build for Sisyphus

