%define oname zope.configuration
%def_without check

Name: python-module-%oname
Version: 4.3.1
Release: alt1

Summary: Zope Configuration Markup Language (ZCML)
License: ZPL
Group: Development/Python

Url: http://pypi.python.org/pypi/zope.configuration/
# https://github.com/zopefoundation/zope.configuration.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx

BuildRequires: python-module-setuptools
BuildRequires: python-module-alabaster
BuildRequires: python-module-coverage
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-nosexcover
BuildRequires: python-module-objects.inv
BuildRequires: python-module-repoze.sphinx.autointerface
BuildRequires: python-module-zope.i18nmessageid
BuildRequires: python-module-zope.schema
BuildRequires: time

BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-nosexcover
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-zope.i18nmessageid
BuildPreReq: python3-module-zope.schema

%if_with check
BuildRequires: python-module-manuel-tests
BuildRequires: python-module-manuel

BuildPreReq: python3-module-manuel-tests
BuildPreReq: python3-module-manuel
%endif

Requires: python-module-zope.i18nmessageid
%py_requires zope.interface zope.schema


%description
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

%package -n python3-module-%oname
Summary: Zope Configuration Markup Language (ZCML) (Python 3)
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires zope.interface zope.schema

%description -n python3-module-%oname
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Configuration Markup Language (ZCML) (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing
%add_python3_req_skip bad_to_the_bone

%description -n python3-module-%oname-tests
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

%package tests
Summary: Tests for Zope Configuration Markup Language (ZCML)
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing
%add_python_req_skip bad_to_the_bone

%description tests
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

This package contains tests for Zope Configuration Markup Language
(ZCML).

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%if_with check
%check
export PYTHONPATH=$PWD/src
python setup.py test -v
nosetests -vv --with-xunit --with-xcoverage

pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test -v
nosetests3 -vv --with-xunit --with-xcoverage
popd
%endif

%files
%doc *.txt *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/*/tests

%files -n python3-module-%oname
%doc *.txt *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests


%changelog
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

