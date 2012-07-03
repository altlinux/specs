# test new macroses
%define python_build %__python setup.py build
%define python_install %__python setup.py install --root %buildroot

%define oname minihallib
Name: python-module-%oname
Version: 0.1.10
Release: alt3.1

Summary: Library to handle HAL devices and events

Group: Development/Python
License: GPLv2+ or AFL
Url: http://pypi.python.org/pypi/minihallib

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/m/%oname/%oname-%version.tar.bz2
BuildArch: noarch

%setup_python_module %oname

# python-module-MySQLdb python-module-Pyrex python-module-Rabbyt python-module-lxml 
# Automatically added by buildreq on Tue Jan 08 2008
BuildRequires:  python-module-ruledispatch python-module-setuptools

%description
Python threaded library to handle HAL devices and their events.

%prep
%setup -q -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-%version-py%__python_version.egg-info/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.10-alt3.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt3
- Rebuilt with python 2.6

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 0.1.10-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.1.10-alt2
- Build as noarch.
- Use __python_version macro while packaging.

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- new version 0.1.10 (with rpmrb script)

* Sat Oct 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.8-alt1
- initial build for ALT Linux Sisyphus
