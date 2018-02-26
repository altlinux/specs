%define module	Cellulose

Name: python-module-Cellulose
Version: 0.2
Release: alt2.1

Summary: Python/Cellulose package

License: BSD
Url: http://cheeseshop.python.org/pypi/Cellulose/
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://cheeseshop.python.org/packages/source/C/Cellulose/%module-%version.tar.bz2
BuildArch: noarch

# manually removed: pybliographic
# Automatically added by buildreq on Tue Dec 25 2007
BuildRequires: python-module-MySQLdb python-module-Pyrex python-module-Rabbyt python-module-setuptools

%description
Stateful, object-oriented, pseudo-functional programming in python.

%prep
%setup -q -n %module-%version

%build
%__python setup.py build

%install
install -d %buildroot%python_sitelibdir
cp -af cellulose %buildroot%python_sitelibdir

%files
%doc AUTHORS CHANGELOG LICENSE README TODO
%doc docs
%python_sitelibdir/cellulose/


%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt1.1
- Rebuilt with python-2.5.

* Tue Dec 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus (thanks to PLD)

