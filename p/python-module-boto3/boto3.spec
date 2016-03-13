%define oname boto3

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt1.git20150807.1.1
Summary: The AWS SDK for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/boto3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boto/boto3.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-botocore python-module-bcdoc
#BuildPreReq: python-module-jmespath python-module-six
#BuildPreReq: python-module-nose python-module-mock
#BuildPreReq: python-module-futures
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
#BuildPreReq: python-module-guzzle_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-botocore python3-module-bcdoc
#BuildPreReq: python3-module-jmespath python3-module-six
#BuildPreReq: python3-module-nose python3-module-mock
%endif

%py_provides %oname
%py_requires concurrent.futures

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-dateutil python-module-docutils python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-jmespath python-module-markupsafe python-module-ntlm python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-dateutil python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-botocore python-module-futures python-module-guzzle_sphinx_theme python-module-html5lib python-module-nose python-module-objects.inv python-module-pbr python-module-setuptools-tests python-module-unittest2 python3-module-botocore python3-module-html5lib python3-module-nose python3-module-pbr python3-module-setuptools-tests python3-module-sphinx python3-module-unittest2 rpm-build-python3 time

%description
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

WARNING: Boto 3 is in developer preview and should not be used in
production yet! Please try it out and give feedback by opening issues or
pull requests on this repository. Thanks!

%package -n python3-module-%oname
Summary: The AWS SDK for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

WARNING: Boto 3 is in developer preview and should not be used in
production yet! Please try it out and give feedback by opening issues or
pull requests on this repository. Thanks!

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
export PYTHONPATH=$PWD
python setup.py test
#py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
#py.test-%_python3_version
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150807
- New snapshot

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150723
- Version 1.1.1

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150420
- Version 0.0.16

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1.git20150316
- Version 0.0.10

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20150219
- Version 0.0.9

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20150210
- Version 0.0.8

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141218
- Version 0.0.6

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141209
- Version 0.0.5

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141208
- Version 0.0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141126
- Version 0.0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141120
- Version 0.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141111
- Initial build for Sisyphus

