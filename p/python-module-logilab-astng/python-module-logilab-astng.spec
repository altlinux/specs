%def_disable check
%def_with python3

%define oname logilab-astng
Name: python-module-%oname
Version: 0.23.1
Release: alt1.hg20120119

Summary: Python Abstract Syntax Tree New Generation
License: LGPLv2.1+
Group: Development/Python

BuildArch: noarch

Url: http://www.logilab.org/project/logilab-astng
# hg clone http://hg.logilab.org/logilab/astng
Source: %name-%version.tar

%setup_python_module %oname
%python_module_declare %python_sitelibdir/logilab

%{?!_without_check:%{?!_disable_check:BuildRequires: /usr/bin/pytest}}
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute /usr/bin/pytest3
%endif

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

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Abstract Syntax Tree New Generation
Group: Development/Python3

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
rm -rf %buildroot%python_sitelibdir/logilab/astng/test
rm -rf %buildroot%python_sitelibdir/logilab/__init__.py*

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/logilab/astng/test
rm -rf %buildroot%python3_sitelibdir/logilab/__init__.py*
popd
%endif

%check
touch build/lib/logilab/__init__.py
ln -sf %python_sitelibdir/logilab/common build/lib/logilab/common
PYTHONPATH=$(pwd)/build/lib/ pytest -t test
rm -f build/lib/logilab/{common,__init__.py}

%if_with python3
pushd ../python3
touch build/lib/logilab/__init__.py
ln -sf %python3_sitelibdir/logilab/common build/lib/logilab/common
PYTHONPATH=$(pwd)/build/lib/ pytest3 -t test
rm -f build/lib/logilab/{common,__init__.py}
popd
%endif

%files
%python_sitelibdir/logilab/
%python_sitelibdir/*.egg-info
%doc ChangeLog README

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/logilab/
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
