%define oname	Rabbyt

Name: python-module-Rabbyt
Version: 0.7.5
Release: alt4.1.1

Summary: Library for Python to game development

License: MIT
Group: Development/Python
Url: http://matthewmarshall.org/projects/rabbyt/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://cheeseshop.python.org/packages/source/R/Rabbyt/%oname-%version.tar.bz2

# manually removed: pybliographic
# Automatically added by buildreq on Tue Dec 25 2007
BuildRequires: python-module-MySQLdb python-module-Pyrex python-module-setuptools
BuildPreReq: libGL-devel libGLU-devel

%description
Rabbyt is a sprite library for Python with game development in mind.
It has two goals:
1. Be fast, without sacrificing ease of use.
2. Be easy to use, without sacrificing speed.

%prep
%setup -n %oname-%version

subst "s/'-O3',\?//" setup.py

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_build_install --optimize=2

%files
%doc CHANGELOG README THANKS examples
%dir %python_sitelibdir/rabbyt
%python_sitelibdir/rabbyt/*.py*
%python_sitelibdir/rabbyt/*.so
%python_sitelibdir/Rabbyt-*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt4.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt4.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt4
- BuildRequires: replaced libmesa-devel by libGL-devel
- Rebuilt for debuginfo

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt3
- Fixed build

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt2
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.7.5-alt1.1
- Rebuilt with python-2.5.

* Tue Dec 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- initial build for ALT Linux Sisyphus (thanks to PLD)

