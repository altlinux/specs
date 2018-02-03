%define oname guessit

%def_with python3

Name: python-module-%oname
Version: 2.1.4
Release: alt1.1
Summary: GuessIt - a library for guessing information from video files
License: LGPLv3
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/guessit/

# https://github.com/wackou/guessit.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-babelfish python-module-stevedore
BuildRequires: python-module-requests python-module-dateutil
BuildRequires: python-module-yaml python-module-guess-language
BuildRequires: python-module-enzyme python-module-nose
BuildRequires: python-module-pbr python-module-pip pylint
BuildRequires: python-module-alabaster python-module-chardet python-module-html5lib python-module-ndg-httpsclient
BuildRequires: python-module-objects.inv python-module-unittest2
BuildRequires: python-module-pytest-runner python2.7(rebulk) python2.7(pytest_capturelog) python2.7(pytest_benchmark)
BuildRequires: python2.7(guessit)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-babelfish python3-module-stevedore
BuildRequires: python3-module-requests python3-module-dateutil
BuildRequires: python3-module-yaml python3-module-guess-language
BuildRequires: python3-module-enzyme python3-module-nose
BuildRequires: python3-module-pbr python3-module-pip pylint-py3
BuildRequires: python3-module-chardet python3-module-html5lib
BuildRequires: python3-module-unittest2 python3-module-urllib3
BuildRequires: python3-module-pytest-runner python3(rebulk) python3(pytest_capturelog) python3(pytest_benchmark)
%endif

%py_provides %oname
%py_requires babelfish stevedore requests dateutil yaml guess_language
%py_requires enzyme json logging

%description
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: GuessIt - a library for guessing information from video files
Group: Development/Python3
%py3_provides %oname
%py3_requires babelfish stevedore requests dateutil yaml guess_language
%py3_requires enzyme json logging

%description -n python3-module-%oname
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

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
%patch1 -p1

# remove mimetypes from test data, see https://github.com/guessit-io/guessit/pull/515
# TODO: consider removing following line on next release after 2.1.4
sed -i -e '/mimetype:/d' guessit/test/*.yml

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
rm -fR build conf.py
python setup.py test
%if_with python3
pushd ../python3
rm -fR build
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
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

