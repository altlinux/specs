%define oname babel

%def_with python3
%def_with doc
#def_disable check

Name:    python-module-%oname
Version: 2.4.0
Release: alt1.1
Epoch:   1

Summary: a collection of tools for internationalizing Python applications
License: BSD
Group: Development/Python

Url: http://babel.pocoo.org/

# https://github.com/mitsuhiko/babel.git
Source: %name-%version.tar
Source1: CLDR.tar

BuildArch: noarch
BuildPreReq: python-module-setuptools python-module-sphinx-devel
BuildPreReq: python-module-pytest-cov
%{?!_without_check:%{?!_disable_check:BuildRequires: %py_dependencies setuptools.command.test pytz}}

%setup_python_module babel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytz
%if_with bootstrap
%else
BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: python3-module-pytest-cov
%endif
%endif
%py_requires pytz

%description
Babel is an integrated collection of utilities that assist in
internationalizing and localizing Python applications, with an emphasis
on web-based applications.
The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:
  * tools to build and work with gettext message catalogs, and
  * a Python interface to the CLDR (Common Locale Data Repository),
    providing access to various locale display names, localized number
    and date formatting, etc.

%if_with python3
%package -n python3-module-%oname
Summary: a collection of tools for internationalizing Python 3 applications
Group: Development/Python3
%py3_requires pytz

%description -n python3-module-%oname
Babel is an integrated collection of utilities that assist in
internationalizing and localizing Python applications, with an emphasis
on web-based applications.
The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:
  * tools to build and work with gettext message catalogs, and
  * a Python interface to the CLDR (Common Locale Data Repository),
    providing access to various locale display names, localized number
    and date formatting, etc.
%endif

%prep
%setup -a1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_with doc
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
python scripts/import_cldr.py CLDR/common
%python_build
%if_with python3
pushd ../python3
python scripts/import_cldr.py CLDR/common
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/pybabel %buildroot%_bindir/pybabel3
%endif

%python_install

%if_with doc
%make -C docs html
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%_bindir/pybabel
%python_sitelibdir/*
%doc AUTHORS CHANGES README.rst
%if_with doc
%doc docs/_build/html
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README.rst
%if_with doc
%doc docs/_build/html
%endif
%_bindir/pybabel3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:2.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.4.0-alt1
- Updated to upstream version 2.4.0

* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 1:2.3.4-alt1.1
- BOOTSTRAP:
  + avoid even more extra BRs when requested to
  + make doc knob more effective (and rename from docs)

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.4-alt1
- 2.3.4

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.1.1-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 06 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.1.1-alt1
- Return to stable release 2.1.1
- Set Epoch to 1

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 3.0-alt4.dev.git20150928
- New version
- Fix project homepage

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt3.dev.git20150805
- Enabled tests and docs

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2.dev.git20150805
- Added missing files

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev.git20150805
- Version 3.0-dev

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev.git20140407
- Version 2.0-dev

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20121012
- Version 1.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Thu Feb 21 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt1.1
- Rebuild with Python-2.7

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.9.5-alt1
- 0.9.5
- build from SVN
- run tests
- add pytz to Requires according to the upstream recommendation

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.1
- Rebuilt with python 2.6

* Sun Oct 18 2009 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt1
- initial build
