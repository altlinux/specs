%def_with python3

Summary: An implementation the OpenBSD Blowfish password hashing algorithm
Version: 3.1.3
Release: alt2.1
%setup_python_module bcrypt
Name: python-module-bcrypt
Source0: %version.tar.gz
Source1: bfhash
Source2: bfhash.1
License: BSD
Group: Development/Python
Url: http://code.google.com/p/py-bcrypt/

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
BuildPreReq: python-module-six python-module-cffi
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six python3-module-cffi
%endif

%description
py-bcrypt is an implementation the OpenBSD Blowfish password hashing
algorithm, as described in "A Future-Adaptable Password Scheme" by Niels
Provos and David Mazieres: http://www.openbsd.org/papers/bcrypt-paper.ps

This system hashes passwords using a version of Bruce Schneier's
Blowfish block cipher with modifications designed to raise the cost of
off-line password cracking. The computation cost of the algorithm is
parametised, so it can be increased as computers get faster.

%if_with python3
%package -n python3-module-bcrypt
Summary: An implementation the OpenBSD Blowfish password hashing algorithm
Group: Development/Python3

%description -n python3-module-bcrypt
py-bcrypt is an implementation the OpenBSD Blowfish password hashing
algorithm, as described in "A Future-Adaptable Password Scheme" by Niels
Provos and David Mazieres: http://www.openbsd.org/papers/bcrypt-paper.ps

This system hashes passwords using a version of Bruce Schneier's
Blowfish block cipher with modifications designed to raise the cost of
off-line password cracking. The computation cost of the algorithm is
parametised, so it can be increased as computers get faster.
%endif

%prep
%setup -n %modulename-%version

%build
%python_build_debug

%if_with python3
%python3_build_debug
%endif

%install
%python_install
install -D -m755 %SOURCE1 %buildroot%_bindir/bfhash
install -D %SOURCE2  %buildroot%_man1dir/bfhash.1

%if_with python3
%python3_install
install -D -m755 %SOURCE1 %buildroot%_bindir/bfhash.py3
sed -i 's|python|python3|' %buildroot%_bindir/bfhash.py3
%endif

%files
%doc *.rst
%python_sitelibdir/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%_man1dir/*

%if_with python3
%files -n python3-module-bcrypt
%doc *.rst
%python3_sitelibdir/*
%_bindir/*.py3
%exclude %_man1dir/bfhash*
%_man1dir/*
%endif

%check
PYTHONPATH=%buildroot%python_sitelibdir py.test
%if_with python3
PYTHONPATH=%buildroot%python3_sitelibdir py.test3
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.3-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.3-alt2
- Fixed build.

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 3.1.3-alt1
- Autobuild version bump to 3.1.3

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 3.1.1-alt1
- Autobuild version bump to 3.1.1

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 3.1.0-alt1
- Autobuild version bump to 3.1.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Dec 07 2015 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Autobuild version bump to 2.0.0
- Update bfhash(1)
- Provide check section

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1
- Added module for Python 3

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Autobuild version bump to 0.4

* Fri Jun 14 2013 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Autobuild version bump to 0.3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt4.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt4.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Rebuilt with python 2.6

* Sat Jul 11 2009 Fr. Br. George <george@altlinux.ru> 0.1-alt2
- BFHash utility added

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt1.1
- Rebuilt with python-2.5.

* Tue Sep 18 2007 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build for ALT

