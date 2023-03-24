%define oname Babel
# see babel/scripts/download_import_cldr.py
%define cldr_version 37
%define cldr_name cldr-%cldr_version

%def_with doc
%def_with check

Name: python3-module-babel
Version: 2.12.1
Release: alt1
Epoch: 1

Summary: a collection of tools for internationalizing Python applications
License: BSD
Group: Development/Python3

Url: http://babel.pocoo.org/

# Source-url: %__pypi_url %oname
Source: Babel-%version.tar.gz
Source1: Babel-failed_tests
# LC_ALL=ru_RU.UTF-8 python3 -m pytest tests |& sed -En '/^FAILED tests/s/.*::([^[ ]*).*/\1/p' | sort -u | tr '\n' ' ' > Babel-failed_tests

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3

# Automatically added by buildreq on Fri Mar 24 2023
# optimized out: libgpg-error python-sphinx-objects.inv python3 python3-base python3-dev python3-module-Pygments python3-module-cffi python3-module-charset-normalizer python3-module-pkg_resources python3-module-pytz python3-module-setuptools python3-module-sphinx sh4
BuildRequires: cldr-37-common python3-module-pyproject-installer python3-module-wheel python3-module-sphinx

%if_with check
BuildRequires: python3-module-pytest python3-module-freezegun python3-module-pytz
%endif

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

%prep
%setup -n %oname-%version

%if_with doc
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
python3 scripts/import_cldr.py /usr/share/unicode/%cldr_name/common
%pyproject_build

%install
%pyproject_install
%python3_prune

%if_with doc
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

%if_with check
%check
LC_ALL=ru_RU.UTF-8 python3 -m pytest tests -k "not `sed -E 's/ (.)/ and not \1/g' %SOURCE1`"
%endif

%files
%doc AUTHORS* CHANGES* README*
%if_with doc
%doc docs/_build/html
%endif
%_bindir/pybabel
%python3_sitelibdir/*

%changelog
* Fri Mar 24 2023 Fr. Br. George <george@altlinux.org> 1:2.12.1-alt1
- Autobuild version bump to 2.12.1
- Enable most of tests

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1:2.9.1-alt1
- new version 2.9.1 (with rpmrb script)

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1:2.9.0-alt1
- new version 2.9.0 (with rpmrb script)
- require CLDR = 37

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:2.8.0-alt1
- new version 2.8.0 (with rpmrb script)
- require CLDR = 36

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:2.6.0-alt2
- build python3 package separately

* Thu Oct 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1:2.6.0-alt1.1
- NMU: disable python2 check (due missed python-module-pytest-cov)

* Fri Feb 08 2019 Alexey Shabalin <shaba@altlinux.org> 1:2.6.0-alt1
- 2.6.0

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
