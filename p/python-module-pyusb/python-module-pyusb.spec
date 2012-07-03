Name: python-module-pyusb
Version: 0.4.2
Release: alt1.1.1.1

Summary: Python module which provides easy USB access

Group: Development/Python
License: GPL
Url: http://pyusb.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module pyusb

Source: http://prdownloads.sf.net/pyusb/pyusb-%version.tar.gz

# Automatically added by buildreq on Wed Jun 17 2009
BuildRequires: libusb-compat-devel python-devel

%description
PyUSB is a Python module which provides easy USB access. For uncountable
reasons, PyUSB has been frozen for a while, but the project is coming
back soon. Meanwhile, you can access the current project page here.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.1
- Rebuilt with python 2.6

* Wed Jun 17 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
