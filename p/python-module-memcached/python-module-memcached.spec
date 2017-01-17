%define _unpackaged_files_terminate_build 1
%define modulename python-memcached

%def_with python3

Name: python-module-memcached
Version: 1.58
Release: alt1

Summary: A Python module for memcached daemon
Group: Development/Python
License: GPL
Url: https://github.com/linsomniac/python-memcached

%setup_python_module %modulename

Source0: https://pypi.python.org/packages/f7/62/14b2448cfb04427366f24104c9da97cf8ea380d7258a3233f066a951a8d8/python-memcached-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2005
BuildRequires: python-devel python-modules-compiler python-modules-encodings

BuildRequires: python-module-setuptools
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-six
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
%setup -q -n python-memcached-%{version}

%if_with python3
cp -fR . ../python3
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
%doc ChangeLog PKG-INFO test-requirements.txt README.md
%python_sitelibdir/*
%doc README* PKG-INFO ChangeLog

%if_with python3
%files -n python3-module-memcached
%doc ChangeLog PKG-INFO test-requirements.txt README.md
%python3_sitelibdir/*
%doc README* PKG-INFO ChangeLog
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated PyPI update

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.57-alt1
- 1.57

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

