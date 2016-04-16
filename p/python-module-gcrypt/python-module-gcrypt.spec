Name: python-module-gcrypt
Version: 0.1.0
Release: alt2.qa3
%setup_python_module gcrypt

Summary: Python bindings for libgcrypt library
License: LGPLv2+
Group: Development/Python

Url: https://sourceforge.net/projects/libgcrypt-py/
# https://download.sourceforge.net/libgcrypt-py/libgcrypt-py-%version.tar.bz2
Source: libgcrypt-py-%version.tar

Provides: libgcrypt-py = %version-%release

BuildRequires: libgcrypt-devel

%description
libgcrypt-py is a Python wrapper around the libgcrypt library.

%prep
%setup -n libgcrypt-py-%version

%build
%python_build

%python_install
touch %buildroot%python_sitelibdir/_Gcrypt/__init__.py

%files
%python_sitelibdir/*

%changelog
* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.0-alt2.qa3
- NMU: cleaned up specfile, rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.0-alt2
- damn, i should be more careful with licensing

* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.0-alt1
- first build
