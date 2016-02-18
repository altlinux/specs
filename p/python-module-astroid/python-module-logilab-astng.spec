#def_disable check
%def_with python3

%define oname astroid
Name: python-module-%oname
Version: 1.3.8
Release: alt1.1

Summary: Python Abstract Syntax Tree New Generation
License: LGPLv2.1+
Group: Development/Python

BuildArch: noarch

Url: http://www.logilab.org/project/logilab-astng
# hg clone https://bitbucket.org/logilab/astroid
Source: %name-%version.tar

Provides: python-module-logilab-astng = %version-%release
Obsoletes: python-module-logilab-astng <= 0.24.2

Requires: python-module-logilab-common >= 0.60.0

%setup_python_module %oname
%python_module_declare %python_sitelibdir/logilab

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-egenix-mx-base python-module-kerberos python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools python3-module-six xz
BuildRequires: python-module-logilab-common python-module-pytest python3-module-logilab-common python3-module-pytest rpm-build-python3 time

#BuildRequires: python-module-logilab-common
#BuildPreReq: python-module-setuptools-tests python-module-six

%{?!_without_check:%{?!_disable_check:BuildRequires: /usr/bin/pytest}}
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildRequires: python3-module-logilab-common /usr/bin/pytest3
#BuildPreReq: python3-module-six
#BuildPreReq: python-tools-2to3
%endif

%py_requires logilab.common six

%description
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentialy governed by
pylint's needs.
It extends class defined in the compiler.ast [1] module (python <= 2.4)
or in the builtin _ast module (python >= 2.5) with some additional
methods and attributes. Instance attributes are added by a builder
object, which can either generate extended ast (let's call them astng ;)
by visiting an existant ast tree or by inspecting living object. Methods
are added by monkey patching ast classes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentialy governed by
pylint's needs.
It extends class defined in the compiler.ast [1] module (python <= 2.4)
or in the builtin _ast module (python >= 2.5) with some additional
methods and attributes. Instance attributes are added by a builder
object, which can either generate extended ast (let's call them astng ;)
by visiting an existant ast tree or by inspecting living object. Methods
are added by monkey patching ast classes.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Abstract Syntax Tree New Generation
Group: Development/Python3
%py3_requires logilab.common six

Provides: python3-module-logilab-astng = %version-%release
Obsoletes: python3-module-logilab-astng <= 0.24.2

Requires: python3-module-logilab-common >= 0.60.0

%description -n python3-module-%oname
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentialy governed by
pylint's needs.
It extends class defined in the compiler.ast [1] module (python <= 2.4)
or in the builtin _ast module (python >= 2.5) with some additional
methods and attributes. Instance attributes are added by a builder
object, which can either generate extended ast (let's call them astng ;)
by visiting an existant ast tree or by inspecting living object. Methods
are added by monkey patching ast classes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentialy governed by
pylint's needs.
It extends class defined in the compiler.ast [1] module (python <= 2.4)
or in the builtin _ast module (python >= 2.5) with some additional
methods and attributes. Instance attributes are added by a builder
object, which can either generate extended ast (let's call them astng ;)
by visiting an existant ast tree or by inspecting living object. Methods
are added by monkey patching ast classes.

This package contains tests for %oname.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%check
#PYTHONPATH=%buildroot%python_sitelibdir pytest -vv

%if_with python3
PYTHONPATH=%buildroot%python3_sitelibdir pytest3 -vv
%endif

%files
%python_sitelibdir/astroid/
%exclude %python_sitelibdir/astroid/test*
%python_sitelibdir/*.egg-info
%doc ChangeLog README

%files tests
%python_sitelibdir/astroid/test*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/astroid/
%exclude %python3_sitelibdir/astroid/test*
%exclude %python3_sitelibdir/astroid/*/test*
%python3_sitelibdir/*.egg-info

%files -n python3-module-%oname-tests
%python3_sitelibdir/astroid/test*
%python3_sitelibdir/astroid/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.8-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.8-alt1
- Version 1.3.8

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2 (ALT #30535)

* Wed Mar 19 2014 Timur Aitov <timonbl4@altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.2-alt1.hg20130227
- Version 0.24.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.23.1-alt1.hg20120119.1
- Rebuild with Python-3.3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt1.hg20120119
- Version 0.23.1
- Added module for Python 3

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1
- Version 0.23.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.20.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.20.3-alt1
- 0.20.3

* Mon Sep 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.20.2-alt1
- 0.20.2

* Mon Sep 06 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.20.1-alt2
- run tests

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Fri Mar 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.3-alt1
- 0.19.3

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.2-alt1
- 0.19.2

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19.1-alt1.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Sun Mar 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.4-alt2
- use %%python_{build,install}

* Tue Dec 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.4-alt1
- 0.17.4

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.3-alt1
- 0.17.3
- spec cleanup
- probably fix automatic dependency search
- don't package tests

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.16.3-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 6 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.16.3-alt1
- Initial build for ALT Linux
