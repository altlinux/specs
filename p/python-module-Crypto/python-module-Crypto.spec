# -*- coding: utf-8 -*-
%define modulever  2.5
%define version    2.5
%define release    alt1.1
%define sourcename pycrypto
%define oname Crypto

%def_with doc_package
%def_with python3

%setup_python_module %oname


Summary: Cryptography Toolkit for python
Summary(ru_RU.UTF-8): Криптографический инструментарий для python
Name: %packagename
Version: %version
Release: %release
# git://git.pycrypto.org:9419/crypto/pycrypto-2.x.git
Source: %sourcename-%modulever.tar.bz2
License: LGPL
Group: Development/Python
Prefix: %_prefix
Url: http://www.amk.ca/python/code/crypto.html
Packager: Python Development Team <python@packages.altlinux.org>

Provides: %{__python_module_prefix}-pycrypto
Obsoletes: %{__python_module_prefix}-pycrypto
BuildRequires: rpm-build-python > 0.12-alt3

%if_without doc_package
Provides: %{__python_module_prefix}-pycrypto-doc
Obsoletes: %{__python_module_prefix}-pycrypto-doc
%endif

BuildPreReq: python

%define moduledocdir %_docdir/%packagename-%version

# Automatically added by buildreq on Sun Jun 20 2004 (-bi)
BuildRequires: latex2html libgmp-devel python-doc-tools python-modules-compiler rpm-build-python

#BuildPreReq: texlive-latex-recommended
BuildPreReq: python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
This is a collection of both secure hash functions (such as MD5 and
SHA), and various encryption algorithms (AES, DES, IDEA, RSA, ElGamal,
etc.).  The package is structured to make adding new modules easy.

This module is built for python %_python_version

%description -l ru_RU.UTF-8
Это набор функций для вычисления безопасных хэшей (таких как MD5 и
SHA) и различных алгоритмов шифрования (AES, DES, IDEA, RSA, ElGamal и
т.д.). Устройство пакета подразумевает легкое добавление новых
модулей.

Модуль собран для python %_python_version

%if_with python3
%package -n python3-module-%oname
Summary: Cryptography Toolkit for python 3
Group: Development/Python3

%description -n python3-module-%oname
This is a collection of both secure hash functions (such as MD5 and
SHA), and various encryption algorithms (AES, DES, IDEA, RSA, ElGamal,
etc.).  The package is structured to make adding new modules easy.

This module is built for python %_python3_version

%package -n python3-module-%oname-test
Summary: Test for %name (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-test
Test for python3-module-%oname.
%endif

%if_with doc_package
%package doc
Buildarch: noarch
Summary: %modulename API documentation and example programs
Summary(ru_RU.UTF-8): Документация по API и примеры программ для %modulename
Group: Development/Python
Prefix: %_prefix
Requires: %packagename = %version
%description doc
%modulename is a collection of both secure hash functions (such as MD5
and SHA), and various encryption algorithms (AES, DES, IDEA, RSA,
ElGamal, etc.). Install python-%modulename-doc if you need module API
documentation and example programs

%description doc -l ru_RU.UTF-8
%modulename - это набор функций для вычисления безопасных хэшей (таких
как MD5 и SHA) и различных алгоритмов шифрования (AES, DES, IDEA, RSA,
ElGamal и т.д.). Установите python-%modulename-doc, если Вам требуется
документация по API и примеры программирования с использованием
данного модуля.


%endif

%package test

Summary: Test for %name
Group: Development/Python
Requires: %name = %version-%release

%description test
Test for %name.

%prep
%setup -n %sourcename-%modulever
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

export PYTHONPATH=$PWD/lib
pushd Doc
epydoc --config=epydoc-config
popd

%install
%python_build_install --optimize=2 \
		--record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_build_install --optimize=2
popd
%endif

# remove test framework from the [main] build
subst '/\/test/d' INSTALLED_FILES

mkdir -p %buildroot%moduledocdir/API
# install can't be [easily] used for a recursive installations :-(
cp -pr Doc/html/* %buildroot%moduledocdir/API
#cp -pr Demo %buildroot%moduledocdir/
install -p -m644 ACKS COPYRIGHT ChangeLog README TODO \
	%buildroot%moduledocdir/

%check
python setup.py test

%files -f INSTALLED_FILES
%exclude %python_sitelibdir/Crypto/SelfTest

%doc %dir %moduledocdir
%moduledocdir/ACKS
%moduledocdir/COPYRIGHT
%moduledocdir/ChangeLog
%moduledocdir/README
%moduledocdir/TODO

%if_with doc_package
%files doc
%endif

%doc %dir %moduledocdir
%moduledocdir/API
#moduledocdir/Demo

%files test
%python_sitelibdir/Crypto/SelfTest

%if_with python3
%files -n python3-module-%oname
%doc ACKS ChangeLog COPYRIGHT README TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/Crypto/SelfTest

%files -n python3-module-%oname-test
%python3_sitelibdir/Crypto/SelfTest
%endif

%changelog
* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Added module for Python 3

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt1
- Version 2.5

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt2.2
- Rebuild to remove libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt2
- Rebuilt for debuginfo

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Version 2.3

* Thu Jun 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0 (ALT #23581)
- Added doc and test packages

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.0-alt2.1.1
- Rebuilt with python-2.5.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.0-alt2.1
- Rebuilt with python-2.4.

* Tue Aug 31 2004 Alexey Morozov <morozov@altlinux.org> 2.0-alt2
- fixed provides/obsoletes

* Mon Aug 30 2004 Alexey Morozov <morozov@altlinux.org> 2.0-alt1
- package name changed from python-module-pycrypto to python-module-Crypto
- new version (2.0)
- separation of doc package is optional (by default docs go to the main package)

* Sun Jun 20 2004 Alexey Morozov <morozov@altlinux.org> 1.9a6-alt2
- Build w/ the new python modules scheme

* Sun Jan 11 2004 Alexey Morozov <morozov@altlinux.org> 1.9a6-alt1
- Initial build for ALT Linux
