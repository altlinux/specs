%define _name python-gudev

Name: python-module-gudev
Version: 147.2
Release: alt1.1

Summary: Python (PyGObject) bindings to the GUDev library
Group: Development/Python
License: LGPLv3+
Url: http://github.com/nzjrs/python-gudev

# http://github.com/nzjrs/python-gudev/tarball/%version/nzjrs-python-gudev-%version-0-ga9f8dd2.tar.gz
Source: %_name-%version.tar.bz2

BuildRequires: python-devel libgudev-devel python-module-pygobject-devel

%description
python-gudev is a Python (PyGObject) binding to the GUDev UDEV library.

%prep
%setup -q -n %_name-%version

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%python_sitelibdir/*
%_datadir/*
%doc README NEWS

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 147.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 02 2010 Yuri N. Sedunov <aris@altlinux.org> 147.2-alt1
- first build for Sisyphus

