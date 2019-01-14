%define _unpackaged_files_terminate_build 1
%define oname pylint

%def_with check

Name: python3-module-%oname
Version: 2.2.2
Release: alt1

Summary: Python code static checker
License: GPLv2+
Group: Development/Python3
# https://github.com/PyCQA/pylint.git
Url: http://www.pylint.org/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-astroid
BuildRequires: python3-module-mccabe
BuildRequires: python3-module-isort
BuildRequires: python3-module-enchant
BuildRequires: python3-module-tox
BuildRequires: hunspell-en
%endif

BuildArch: noarch
Provides: pylint-py3 = %EVR
Obsoletes: pylint-py3 < %EVR
%py3_requires mccabe

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

%build
%python3_build

%install

%python3_install
# do not pack tests
rm -r %buildroot%python3_sitelibdir/pylint/test*

pushd %buildroot%_bindir
for i in $(ls); do
       mv $i $i.py3
done

%check
grep -qs '[[:space:]]*coverage[[:space:]]*$' tox.ini || exit 1
grep -qs ' {envsitepackagesdir}/coverage run ' tox.ini || exit 1
grep -qs 'https:' tox.ini || exit 1
grep -qsP 'python -c \x22import os' tox.ini || exit 1

sed -i -e '/[[:space:]]*coverage[[:space:]]*$/d' \
-e 's/ {envsitepackagesdir}\/coverage run / /' \
-e 's/https:.*/astroid/' \
-e '/python -c \x22import os/d' tox.ini

export PIP_NO_INDEX=YES
export PIP_NO_DEPS=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc ChangeLog README.rst doc/
%_bindir/pylint.py3
%_bindir/epylint.py3
%_bindir/pyreverse.py3
%_bindir/symilar.py3
%python3_sitelibdir/pylint/
%python3_sitelibdir/pylint-*.egg-info/

%changelog
* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 2.1.1 -> 2.2.2.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 1.9.1 -> 2.1.1.
- Move Python3 module to a separated src package.

* Fri May 25 2018 Stanislav Levin <slev@altlinux.org> 1.9.1-alt1
- 1.7.4 -> 1.9.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.4-alt2
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.4-alt2
- Updated runtime dependencies.

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.4-alt1
- Updated to upstream version 1.7.4.

* Mon Sep 25 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.1-alt1
- Rebuild with universal build tag (aka ubt macros)

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1
- Updated to upstream release 1.5.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1
- Version 1.4.4

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.1
- Added module for Python 3

* Wed Mar 19 2014 Timur Aitov <timonbl4@altlinux.org> 1.1.0-alt1
- 1.1.0

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
