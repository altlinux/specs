%def_with check

Name: python3-module-pyparsing
Version: 3.0.7
Release: alt1

Summary: Python parsing module

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyparsing

Source: pyparsing-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Feb 02 2022
# optimized out: alt-os-release libgpg-error mpdecimal python3 python3-base python3-dev python3-module-apipkg python3-module-attrs python3-module-distlib python3-module-filelock python3-module-iniconfig python3-module-markupsafe python3-module-packaging python3-module-pkg_resources python3-module-platformdirs python3-module-pluggy python3-module-py python3-module-pyparsing python3-module-pytest python3-module-six python3-module-system-seed-wheels python3-module-toml python3-module-virtualenv python3-modules-sqlite3 sh4 xz
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-coverage python3-module-jinja2 python3-module-railroad-diagrams python3-module-setuptools python3-module-tox
%endif

%description
The parsing module is an alternative approach to creating and executing
simple grammars, vs. the traditional lex/yacc approach, or the use of
regular expressions.  The parsing module provides a library of classes
that client code uses to construct the grammar directly in Python code.

%prep
%setup -n pyparsing-%version

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -v

%files
%doc CHANGES README.rst
%python3_sitelibdir/*

%changelog
* Wed Feb 02 2022 Fr. Br. George <george@altlinux.ru> 3.0.7-alt1
- Autobuild version bump to 3.0.7

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4.7-alt1
- new version 2.4.7 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt2
- build python3 package separately, cleanup spec

* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 2.4.2-alt1
- 2.2.0 -> 2.4.2.
- Enabled testing.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.

* Wed May 24 2017 Alexey Shabalin <shaba@altlinux.ru> 2.1.10-alt1
- 2.1.10
- build python and python3 packages from one spec

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Tue Feb 19 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.7-alt1
- Version 1.5.7
- Removed module for Python 3

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.6-alt2
- Added module for Python 3

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.6-alt1
- Version 1.5.6

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.5-alt1
- Version 1.5.5

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1
- Version 1.5.3

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Rebuilt with python 2.6

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version (1.5.1)
- cleanup spec

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.4.2-alt1.1
- Rebuilt with python-2.5.

* Sun Jun 11 2006 Ivan Fedorov <ns@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 1.1.2-alt5
- Conditional operators are excluded from spec

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 1.1.2-alt4.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 1.1.2-alt3.d
- Clause "noarch" inserted;

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 1.1.2-alt2.d
- Rebuild with new rpm/python macros;
- Build-requires on python-devel removed;

* Mon Mar 29 2004 Andrey Orlov <cray@altlinux.ru> 1.1.2-alt1.d
- Initial release
