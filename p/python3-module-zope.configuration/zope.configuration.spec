%define oname zope.configuration

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt1

Summary: Zope Configuration Markup Language (ZCML)
License: ZPL-2.1
Group: Development/Python3

Url: https://pypi.org/project/zope.configuration
Vcs: https://github.com/zopefoundation/zope.configuration.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-zope.i18nmessageid
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-manuel-tests
BuildRequires: python3-module-manuel
%endif

%py3_requires zope.i18nmessageid
%py3_requires zope.interface zope.schema

%description
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

%package tests
Summary: Tests for Zope Configuration Markup Language (ZCML)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing
%add_python3_req_skip bad_to_the_bone

%description tests
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

This package contains tests for Zope Configuration Markup Language
(ZCML).

%package pickles
Summary: Pickles for Zope Configuration Markup Language (ZCML)
Group: Development/Python

%description pickles
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

This package contains pickles for Zope Configuration Markup Language
(ZCML).

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv3 docs/

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

export PYTHONPATH=$PWD/src
sed -i "s|SPHINXBUILD   = sphinx-build|SPHINXBUILD   = py3_sphinx-build|" docs/Makefile
%make -C docs pickle
%make -C docs html
install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst docs/_build/html
%python3_sitelibdir/zope/configuration/
%python3_sitelibdir/%oname-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/*/tests

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/*/pickle

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Mon May 22 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt3
- Fixed BuildRequires.
- Build with check again.

* Fri Jan 29 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt2
- Bootstrap for python3.9.

* Tue Nov 17 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt1
- 4.3.1 -> 4.4.0

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt2
- NMU: Remove python2 module build
- Rearrange unittests execution

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.3.1-alt1
- Version updated to 4.3.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150225.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150225.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150225.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150225.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150225
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.8.0-alt2.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt5.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt5
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt4
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt3
- Enabled tests

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Set archdep for package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

