%define modname dateparser
#module 'logging' has no attribute 'config'
%def_disable check

Name: python3-module-%modname
Version: 1.1.1
Release: alt1

Summary: Python parser for human readable dates 
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/dateparser

Vcs: https://github.com/scrapinghub/dateparser.git
Source: https://github.com/scrapinghub/dateparser/archive/v%version/%modname-%version.tar.gz
BuildArch: noarch

#grep calendars setup.py 
#'calendars': ['convertdate', 'umalqurra', 'jdatetime', 'ruamel.yaml'],

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-mock
BuildRequires: python3-module-parameterized python3-module-wheel
BuildRequires: python3-module-dateutil python3-module-tzlocal python3-module-regex
BuildRequires: python3-module-sphinx-devel python3-module-sphinx_rtd_theme
%{?_enable_check:BuildRequires: python3-module-flake8 python3-module-pytest
BuildRequires: python3-module-pytest-cov python3-module-parameterized
BuildRequires: python3-module-orderedset python3-module-convertdate
BuildRequires: python3-module-ruamel-yaml python3-module-umalqurra
BuildRequires: python3-module-hijri-converter python3-module-langdetect
BuildRequires: python3-module-fasttext}

%description
Date parsing library designed to parse dates from HTML pages.

%package pickles
Summary: Pickles for %modname
Group: Development/Python3

%description pickles
Date parsing library designed to parse dates from HTML pages.

This package contains pickles for %modname.

%package docs
Summary: Documentation for %modname
Group: Development/Documentation
BuildArch: noarch

%description docs
Date parsing library designed to parse dates from HTML pages.

This package contains documentation for %modname.

%prep
%setup -n %modname-%version

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle html SPHINXBUILD=sphinx-build-3

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%modname/

%check
%__python3 setup.py test

%files
%_bindir/%modname-download
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%doc *.rst

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Thu Mar 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Nov 05 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Sep 26 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt2
- fixed BRs

* Sat Jun 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt1
- 0.7.6 (python3 only)

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4
- enabled %%check

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2
- made python2 build optional

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.git20141125.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141125
- Initial build for Sisyphus

