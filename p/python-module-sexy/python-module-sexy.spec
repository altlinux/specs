Name: python-module-sexy
Version: 0.1.9
Release: alt1.1.1

Summary: Python language bindings for libsexy

Group: Development/Python
License: LGPL
Url: http://www.chipx86.com/w/index.php/Libsexy

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module sexy

Source: http://releases.chipx86.com/libsexy/sexy-python/sexy-python-%version.tar

# Automatically added by buildreq on Sun Jul 25 2010
BuildRequires: gcc-c++ glibc-devel libsexy-devel python-module-pygtk-devel

%description
Pysexy are the python language bindings for libsexy.

%prep
%setup -n sexy-python-%version

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README NEWS
%python_sitelibdir/*
%_datadir/pygtk/2.0/defs/sexy.defs

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.9-alt1.1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.1
- Rebuilt for debuginfo

* Sun Jul 25 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.9-alt1
- cleanup spec, fix build, build from git

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt0.1.1.1
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.1.9-alt0.1.1
- Rebuilt with python-2.5.

* Wed Jun 13 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.9-alt0.1
- initial build for ALT Linux Sisyphus
