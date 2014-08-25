%define oname	Rabbyt

%def_without python3

Name: python-module-Rabbyt
Version: 0.8.3
Release: alt1

Summary: Library for Python to game development

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Rabbyt/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://cheeseshop.python.org/packages/source/R/Rabbyt/%oname-%version.tar.bz2

# manually removed: pybliographic
# Automatically added by buildreq on Tue Dec 25 2007
BuildRequires: python-module-MySQLdb python-module-Pyrex python-module-setuptools
BuildPreReq: libGL-devel libGLU-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
BuildPreReq: python3-module-MySQLdb python3-module-Cython python3-module-setuptools
%endif

%description
Rabbyt is a sprite library for Python with game development in mind.
It has two goals:
1. Be fast, without sacrificing ease of use.
2. Be easy to use, without sacrificing speed.

%package -n python3-module-%oname
Summary: Library for Python to game development
Group: Development/Python3

%description -n python3-module-%oname
Rabbyt is a sprite library for Python with game development in mind.
It has two goals:
1. Be fast, without sacrificing ease of use.
2. Be easy to use, without sacrificing speed.

%prep
%setup -n %oname-%version

subst "s/'-O3',\?//" setup.py

%if_with python3
cp -fR . ../python3
rm -f ../python3/rabbyt/rabbyt.*.c
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc CHANGELOG README THANKS examples docs
%dir %python_sitelibdir/rabbyt
%python_sitelibdir/rabbyt/*.py*
%python_sitelibdir/rabbyt/*.so
%python_sitelibdir/Rabbyt-*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README THANKS examples docs
%dir %python3_sitelibdir/rabbyt
%python3_sitelibdir/rabbyt/*.py*
%python3_sitelibdir/rabbyt/*.so
%python3_sitelibdir/Rabbyt-*.egg-info
%endif

%changelog
* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1
- Version 0.8.3

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

