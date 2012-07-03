Name: python-module-gcrypt
Version: 0.1.0
Release: alt2.1.1
%setup_python_module gcrypt

Summary: Python bindings for D-BUS library
License: %lgpl2plus
Group: Development/Python

Url: http://sourceforge.net/projects/libgcrypt-py/files/libgcrypt-py/
Source: http://downloads.sourceforge.net/project/libgcrypt-py/libgcrypt-py/libgcrypt-py%%20%version/libgcrypt-py-%version.tar.bz2

Provides: libgcrypt-py = %version-%release

BuildRequires: libgcrypt-devel

BuildPreReq: rpm-build-licenses

%description
libgcrypt python bindings for use with python programs.

%prep
%setup -q -n libgcrypt-py-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot
touch %buildroot/%python_sitelibdir/_Gcrypt/__init__.py

%files
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.0-alt2
- damn, i should be more careful with licensing

* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.0-alt1
- first build 
