%define modulename python-memcached

%def_with python3

Name: python-module-memcached
Version: 1.53
Release: alt3.1

Summary: A Python module for memcached daemon
Group: Development/Python
License: GPL
Url: ftp://ftp.tummy.com/pub/python-memcached/

%setup_python_module %modulename

Source: %modulename-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2005
BuildRequires: python-devel python-modules-compiler python-modules-encodings

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides memcache

%description
%modulename is a Python module that interfaces to the memcached -
distributed memory object caching system.

%package -n python3-module-memcached
Summary: A Python module for memcached daemon
Group: Development/Python3
%py3_provides memcache

%description -n python3-module-memcached
%modulename is a Python module that interfaces to the memcached -
distributed memory object caching system.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%python_sitelibdir/*
%doc README* PKG-INFO ChangeLog *.html

%if_with python3
%files -n python3-module-memcached
%python3_sitelibdir/*
%doc README* PKG-INFO ChangeLog *.html
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.53-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.53-alt3
- Added provides: memcache

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.53-alt2
- Added module for Python 3

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.53-alt1
- Version 1.53

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.45-alt1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.45-alt1
- Version 1.45 (ALT #17271)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.tummy5.2
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt2.tummy5.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt2.tummy5
- Build as noarch.

* Mon Nov 14 2005 LAKostis <lakostis at altlinux.ru> 1.2-alt1.tummy5
- First build for Sisyphus.

