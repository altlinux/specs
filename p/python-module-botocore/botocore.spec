%define oname botocore

%def_with python3

Name: python-module-%oname
Version: 1.1.7
Release: alt1.git20150806.1.1
Summary: The low-level, core functionality of boto 3
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/botocore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boto/botocore.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-jmespath
#BuildPreReq: python-module-dateutil python-module-tox
#BuildPreReq: python-module-nose python-module-mock
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-guzzle_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-jmespath
#BuildPreReq: python3-module-dateutil python3-module-tox
#BuildPreReq: python3-module-nose python3-module-mock
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-dateutil python-module-guzzle_sphinx_theme python-module-html5lib python-module-jmespath python-module-nose python-module-objects.inv python-module-pbr python-module-setuptools-tests python-module-tox python-module-unittest2 python3-module-dateutil python3-module-html5lib python3-module-nose python3-module-pbr python3-module-setuptools-tests python3-module-tox python3-module-unittest2 rpm-build-python3 time

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for AWS-CLI.

WARNING
Botocore is currently under a developer preview, and its API is subject
to change prior to a GA (1.0) release. Until botocore reaches a 1.0
release, backwards compatibility is not guaranteed.

If you need a stable interface, please consider using boto.

%package -n python3-module-%oname
Summary: The low-level, core functionality of boto 3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for AWS-CLI.

WARNING
Botocore is currently under a developer preview, and its API is subject
to change prior to a GA (1.0) release. Until botocore reaches a 1.0
release, backwards compatibility is not guaranteed.

If you need a stable interface, please consider using boto.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for AWS-CLI.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for AWS-CLI.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.7-alt1.git20150806.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.7-alt1.git20150806.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.git20150806
- Version 1.1.7

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150723
- Version 1.1.3

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.0-alt1.git20150416
- Version 0.104.0

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95.0-alt1.git20150312
- Version 0.95.0

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.0-alt1.git20150223
- Version 0.93.0

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.0-alt1.git20150217
- Version 0.91.0

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.0-alt1.git20150212
- Version 0.88.0

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87.0-alt1.git20150210
- Version 0.87.0

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.85.0-alt1.git20150203
- Version 0.85.0

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.83.0-alt1.git20150119
- Version 0.83.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.82.0-alt1.git20150115
- Version 0.82.0

* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.80.0-alt1.git20141217
- Version 0.80.0

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.78.0-alt1.git20141208
- Version 0.78.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.76.0-alt1.git20141126
- New snapshot

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.76.0-alt1.git20141125
- Version 0.76.0

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75.0-alt1.git20141121
- Version 0.75.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.74.0-alt1.git20141120
- Version 0.74.0

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.73.0-alt1.git20141112
- Version 0.73.0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.71.0-alt1.git20141110
- Initial build for Sisyphus

