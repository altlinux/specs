%define _unpackaged_files_terminate_build 1

%define oname guessit

Name: python3-module-%oname
Version: 3.3.1
Release: alt2

Summary: GuessIt - a library for guessing information from video files

License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/guessit/

# https://github.com/wackou/guessit.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-babelfish python3-module-stevedore
BuildRequires: python3-module-requests python3-module-dateutil
BuildRequires: python3-module-yaml python3-module-guess-language
BuildRequires: python3-module-enzyme python3-module-nose
BuildRequires: pylint-py3
BuildRequires: python3-module-chardet
BuildRequires: python3-module-unittest2 python3-module-urllib3
BuildRequires: python3-module-pytest-runner python3(rebulk) python3(pytest_benchmark)

%py3_provides %oname
%py3_requires babelfish stevedore requests dateutil yaml guess_language
%py3_requires enzyme json logging

%description
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

This package contains documentation for %oname.

%prep
%setup

# remove mimetypes from test data, see https://github.com/guessit-io/guessit/pull/515
# TODO: consider removing following line on next release after 2.1.4
sed -i -e '/mimetype:/d' guessit/test/*.yml

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
export LC_ALL=en_US.UTF-8

%python3_install

%check
export LC_ALL=en_US.UTF-8
rm -fR build
python3 setup.py test

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt2
- drop unused BR

* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.
- Build without docs (upstream removed them).

* Tue Oct 20 2020 Stanislav Levin <slev@altlinux.org> 3.1.1-alt2
- Dropped buildtime dependency on pytest_capturelog.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- New version 3.1.0.
- Build without python2.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.4-alt1
- Updated to upstream version 2.1.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.4-alt1.dev0.git20150427.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.4-alt1.dev0.git20150427.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.4-alt1.dev0.git20150427
- Version 0.10.4.dev0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.dev0.git20141110
- Version 0.9.5.dev0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.dev0.git20141009
- Initial build for Sisyphus

