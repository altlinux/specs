%define oname guessit

%def_with python3

Name: python-module-%oname
Version: 0.10.4
Release: alt1.dev0.git20150427.1
Summary: GuessIt - a library for guessing information from video files
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/guessit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wackou/guessit.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-babelfish python-module-stevedore
#BuildPreReq: python-module-requests python-module-dateutil
#BuildPreReq: python-module-yaml python-module-guess-language
#BuildPreReq: python-module-enzyme python-module-nose
#BuildPreReq: python-module-mock python-module-argparse
#BuildPreReq: python-module-pbr python-module-pip pylint
#BuildPreReq: python-module-sphinx-devel python-module-Pygments
#BuildPreReq: python-modules-json python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-babelfish python3-module-stevedore
#BuildPreReq: python3-module-requests python3-module-dateutil
#BuildPreReq: python3-module-yaml python3-module-guess-language
#BuildPreReq: python3-module-enzyme python3-module-nose
#BuildPreReq: python3-module-mock python3-module-argparse
#BuildPreReq: python3-module-pbr python3-module-pip pylint-py3
#BuildPreReq: python3-module-Pygments
%endif

%py_provides %oname
%py_requires babelfish stevedore requests dateutil yaml guess_language
%py_requires enzyme json logging

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-docutils python-module-egenix-mx-base python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-kerberos python-module-logilab-common python-module-markupsafe python-module-ntlm python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-logilab-common python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx
BuildRequires: pylint pylint-py3 python-module-alabaster python-module-babelfish python-module-chardet python-module-dateutil python-module-guess-language python-module-html5lib python-module-ndg-httpsclient python-module-nose python-module-objects.inv python-module-pbr python-module-pip python-module-setuptools-tests python-module-stevedore python-module-unittest2 python-module-yaml python3-module-babelfish python3-module-chardet python3-module-dateutil python3-module-guess-language python3-module-html5lib python3-module-nose python3-module-pbr python3-module-setuptools-tests python3-module-stevedore python3-module-unittest2 python3-module-urllib3 python3-module-yaml rpm-build-python3 time

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.4-alt1.dev0.git20150427.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.4-alt1.dev0.git20150427
- Version 0.10.4.dev0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.dev0.git20141110
- Version 0.9.5.dev0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.dev0.git20141009
- Initial build for Sisyphus

