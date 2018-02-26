# $Id: python-module-SAMPLE.spec 138 2004-03-26 23:17:36Z cray $
# vim: termencoding=koi8-r
# vim: encoding=utf-8
%define	version	2.06
%define release alt4

%setup_python_module xmms

Summary: XMMS control bindings for Python
Summary(ru_RU.UTF-8): Управление XMMS из Python
Name: %packagename
Version: %version
Release: %release.1
License: BSD
Group: Development/Python
Prefix: %_prefix
Url: http://people.via.ecp.fr/~flo/2002/PyXMMS
Packager: Fr. Br. George <george@altlinux.ru>
Source: %url/dist/py%modulename-%version.tar.bz2
Patch: pyxmms.setup.usr.patch

#BuildRequires: python-dev glib-devel libxmms-devel
BuildRequires: glib-devel libxmms-devel

%description
PyXMMS is a Python interface to XMMS, a free multimedia player for X-Window1.
PyXMMS consists of two components as of version 2.00:
  * a set of bindings for the xmms_remote* functions of the libxmms library,
    plus some higher-level functions 
  * a Pythonic interface to manage (including reading and writing) the main
    configuration file for XMMS.
In other words, PyXMMS can be used to control XMMS or manage its main
configuration file from a Python program. 

This module is built for python %__python_version

%description -l ru_RU.UTF-8
С помощью этого модуля можно управлять XMMS, музыкальным проигрывателем для X.
В модуль входит два набора функций:
  * Обёртки дл функций xmms_remote* из libxmms
  * Функции разбора файла настроек XMMS

Этот модуль собран для Python версии %__python_version

%prep
%setup -q -n py%modulename-%version
%patch

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record

%add_optflags -fno-strict-aliasing
%python_build_debug \
	install --optimize=2 \
		--root=`pwd`/buildroot \
		--record=INSTALLED_FILES
python build-documentation.py

%install

cp -pr buildroot %buildroot

unset RPM_PYTHON

%files -f INSTALLED_FILES
%doc doc/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.06-alt4.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.06-alt4
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.06-alt3
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.06-alt2.1
- Rebuilt with python-2.5.

* Thu Aug 10 2006 Fr. Br. George <george@altlinux.ru> 2.06-alt2
- Missing documentation added

* Mon Oct 10 2005 Fr. Br. George <george@altlinux.ru> 2.06-alt1
- Version upping

* Tue Apr 12 2005 Fr. Br. George <george@altlinux.ru> 2.04-alt3
- Version upping

* Sat Apr 09 2005 Fr. Br. George <george@altlinux.ru> 2.03-alt2
- Python 2.4 adaptation (actually rebuild only)

* Mon Aug 23 2004 Fr. Br. George <george@altlinux.ru> 2.03-alt1
- Initial ALT Linux build

