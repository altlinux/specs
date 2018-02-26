%def_disable check

Name: pylint
Version: 0.21.3
Release: alt1.1

Summary: Python code static checker
License: GPLv2+
Group: Development/Python

BuildArch: noarch

Url: http://www.logilab.org/project/name/pylint
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Andrey Rahmatullin <wrar@altlinux.org>

%add_findreq_skiplist %python_sitelibdir/%name/gui.py

%setup_python_module %name
#%%py_requires logilab.astng
Requires: python-module-logilab-common >= 0.50.1 python-module-logilab-astng >= 0.20.1

%{?!_without_check:%{?!_disable_check:BuildRequires: /usr/bin/pytest %py_dependencies logilab.astng unittest2 }}

%description
Pylint is a Python source code analyzer which looks for programming
errors, helps enforcing a coding standard and sniffs for some code
smells (as defined in Martin Fowler's Refactoring book)

Pylint can be seen as another PyChecker since nearly all tests you
can do with PyChecker can also be done with Pylint. However, Pylint
offers some more features, like checking length of lines of code,
checking if variable names are well-formed according to your coding
standard, or checking if declared interfaces are truly implemented,
and much more.

Additionally, it is possible to write plugins to add your own checks.

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install
rm -rf %buildroot%python_sitelibdir/%name/test

%check
PYTHONPATH=$(pwd)/build/lib/ pytest -t test

%files
%_bindir/*
%python_sitelibdir/%name
%python_sitelibdir/*.egg-info
%doc ChangeLog README doc/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.21.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.21.3-alt1
- 0.21.3
- run tests

* Mon Jun 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.21.0-alt1
- 0.21.0
- disable findreq for gui.py

* Fri Mar 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.1-alt1.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.18.1-alt1
- 0.18.1

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Mar 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.16.0-alt2
- use %%python_{build,install}

* Fri Jan 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Wed Oct 15 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.15.1-alt1
- 0.15.1
- spec cleanup
- don't package tests

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.12.2-alt3.1
- Rebuilt with python-2.5.

* Sat Dec 9 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.12.2-alt3
- Fixed requires/provides calculation

* Fri Dec 8 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.12.2-alt2
- Fixed dependencies

* Wed Dec 6 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.12.2-alt1
- Initial build for ALT Linux
