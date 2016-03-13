%define oname babel

%def_with python3
%def_with docs
#def_disable check

Name:    python-module-%oname
Version: 2.1.1
Release: alt1.1.1
Epoch:   1

Summary: a collection of tools for internationalizing Python applications
License: BSD
Group: Development/Python

Url: http://babel.pocoo.org/

# https://github.com/mitsuhiko/babel.git
Source: %name-%version.tar
Source1: CLDR.tar
Patch1:	fix-import_cldr.patch

BuildArch: noarch
#BuildPreReq: python-module-setuptools-tests python-module-sphinx-devel
#BuildPreReq: python-module-pytest-cov
%{?!_without_check:%{?!_disable_check:BuildRequires: %py_dependencies setuptools.command.test pytz}}

%setup_python_module babel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-coverage python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest-cov python-module-setuptools-tests python3-module-pytest-cov python3-module-pytz python3-module-setuptools-tests rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pytest-cov
#BuildPreReq: python3-module-pytz python-tools-2to3
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
%patch1 -p1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
python scripts/import_cldr.py CLDR/common
%python_build
%if_with python3
pushd ../python3
python scripts/import_cldr.py CLDR/common
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build build_ext
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

%if_with docs
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
%python_sitelibdir/babel/
%python_sitelibdir/*.egg-info
%doc AUTHORS CHANGES README
%if_with docs
%doc docs/_build/html
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README
%if_with docs
%doc docs/_build/html
%endif
%_bindir/pybabel3
%python3_sitelibdir/babel/
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
