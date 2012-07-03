Summary: An implementation the OpenBSD Blowfish password hashing algorithm
Version: 0.1
Release: alt4.1.1
%setup_python_module bcrypt
Name: python-module-bcrypt
Source0: http://www.mindrot.org/files/py-bcrypt/py-%modulename-%version.tar.gz
Source1: bfhash
Source2: bfhash.1
License: BSD
Group: Development/Python
URL: http://www.mindrot.org/projects/py-bcrypt/
Packager: Fr. Br. George <george@altlinux.ru>

%description
py-bcrypt is an implementation the OpenBSD Blowfish password hashing
algorithm, as described in "A Future-Adaptable Password Scheme" by Niels
Provos and David Mazieres: http://www.openbsd.org/papers/bcrypt-paper.ps

This system hashes passwords using a version of Bruce Schneier's
Blowfish block cipher with modifications designed to raise the cost of
off-line password cracking. The computation cost of the algorithm is
parametised, so it can be increased as computers get faster.

%prep
%setup -n py-%modulename-%version

%build
%python_build_debug

%install
%python_install
install -D -m755 %SOURCE1 %buildroot%_bindir/bfhash
install -D %SOURCE2  %buildroot%_man1dir/bfhash.1

%files
%doc ChangeLog  LICENSE  MANIFEST  PKG-INFO  README  TODO  test/*
%python_sitelibdir/%modulename
%_bindir/*
%_man1dir/*

%changelog
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

