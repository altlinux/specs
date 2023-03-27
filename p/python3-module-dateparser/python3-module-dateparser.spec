%define pypi_name dateparser
#regex!=2019.02.19,!=2021.8.27,<2022.3.15
%def_disable check

Name: python3-module-%pypi_name
Version: 1.1.8
Release: alt1.1

Summary: Python parser for human readable dates 
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/dateparser

Vcs: https://github.com/scrapinghub/dateparser.git
Source: https://github.com/scrapinghub/dateparser/archive/v%version/%pypi_name-%version.tar.gz
BuildArch: noarch

#grep calendars setup.py 
#'calendars': ['convertdate', 'umalqurra', 'jdatetime', 'ruamel.yaml'],

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel  python3-module-setuptools
BuildRequires: python3-module-nose python3-module-mock
BuildRequires: python3-module-parameterized
BuildRequires: python3-module-dateutil python3-module-tzlocal
BuildRequires: python3-module-pytz python3-module-regex
BuildRequires: python3-module-sphinx-devel python3-module-sphinx_rtd_theme
%{?_enable_check:BuildRequires: python3-module-tox
BuildRequires: python3-module-flake8 python3-module-pytest
BuildRequires: python3-module-pytest-cov python3-module-parameterized
BuildRequires: python3-module-orderedset python3-module-convertdate
BuildRequires: python3-module-ruamel-yaml python3-module-umalqurra
BuildRequires: python3-module-hijri-converter python3-module-langdetect
BuildRequires: python3-module-fasttext}

%description
Date parsing library designed to parse dates from HTML pages.

%package pickles
Summary: Pickles for %pypi_name
Group: Development/Python3

%description pickles
Date parsing library designed to parse dates from HTML pages.

This package contains pickles for %pypi_name.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Date parsing library designed to parse dates from HTML pages.

This package contains documentation for %pypi_name.

%prep
%setup -n %pypi_name-%version

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%pyproject_build

%install
%pyproject_install
export PYTHONPATH=$PWD
%make -C docs pickle html SPHINXBUILD=sphinx-build-3

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%pypi_name/

%check
%tox_check

%files
%_bindir/%pypi_name-download
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%doc *.rst

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Mon Mar 27 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1.1
- fixed BR

* Thu Mar 23 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Sat Jan 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Thu Dec 29 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Tue Nov 22 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Thu Oct 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

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

