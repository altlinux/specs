%define oname billiard

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt1

Summary: billiard is a fork of the Python 2.7 multiprocessing package
License: GPL
Group: Development/Python
Requires: python
Url: https://github.com/celery/billiard/

# Source-git: https://github.com/celery/billiard.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools gcc-c++ python-module-sphinx
BuildRequires: python2.7(case)
BuildRequires: python2.7(unittest2) python2.7(mock) python2.7(pytest) python2.7(psutil)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(case)
BuildRequires: python3(unittest2) python3(mock) python3(pytest) python3(psutil)
%endif

%add_findreq_skiplist %python_sitelibdir/%oname/popen_spawn_win32.py
%add_findreq_skiplist %python3_sitelibdir/%oname/popen_spawn_win32.py

%description
billiard is a fork of the Python 2.7 multiprocessing package.
The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package. This standalone variant is intended
to be compatible with Python 2.4 and 2.5, and will draw it's
fixes/improvements from python-trunk.

%if_with python3
%package -n python3-module-%oname
Summary: billiard is a fork of the Python 2.7 multiprocessing package
Group: Development/Python3

%description -n python3-module-%oname
billiard is a fork of the Python 2.7 multiprocessing package.
The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package. This standalone variant is intended
to be compatible with Python 2.4 and 2.5, and will draw it's
fixes/improvements from python-trunk.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

python setup.py build_sphinx --builder="html" --source-dir=Doc

%install
%if_with python3
pushd ../python3
%python3_install
popd

%if "%_libexecdir" != "%_libdir"
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif
%endif

%python_install

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc build/sphinx/html LICENSE.txt CHANGES.txt README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt CHANGES.txt README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jun 04 2019 Vitaly Lipatov <lav@altlinux.ru> 3.6.0-alt1
- new version (3.6.0) with rpmgs script

* Fri Mar 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0.3-alt2
- Updated build dependencies.

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0.3-alt1
- Updated to upstream version 3.5.0.3.
- Enabled tests.
- Merged in python3 build from python3-module-billiard.

* Wed May 31 2017 Lenar Shakirov <snejok@altlinux.ru> 3.3.0.23-alt1
- Version 3.3.0.23

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.20-alt1
- Version 3.3.0.20

* Sat Oct 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.18-alt1
- Version 3.3.0.18 (ALT #30404)

* Thu Apr 11 2013 Dmitry Derjavin <dd@altlinux.org> 2.7.3.26-alt2
- test_multiprocessing.py removed because of the wrong python2.7(test)
  dependency.

* Thu Apr 11 2013 Dmitry Derjavin <dd@altlinux.org> 2.7.3.26-alt1
- Initial ALTLinux build.


