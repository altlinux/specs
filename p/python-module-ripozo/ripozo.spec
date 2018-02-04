%define oname ripozo

%def_with python3

Name: python-module-%oname
Version: 0.1.27
Release: alt1.dev0.git20150423.1.1.1
Summary: An tool for easily making RESTful interfaces
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/ripozo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vertical-knowledge/ripozo.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-jinja2
#BuildPreReq: python-module-tox python-module-mock
#BuildPreReq: python-module-ripozo-tests python-module-coverage
#BuildPreReq: python-module-virtualenv
#BuildPreReq: python-modules-json python-modules-logging
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-jinja2
#BuildPreReq: python3-module-tox python3-module-mock
#BuildPreReq: python3-module-ripozo-tests python3-module-coverage
#BuildPreReq: python3-module-virtualenv
%endif

%py_provides %oname
%py_requires six jinja2 json logging

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pytest python-module-pytz python-module-ripozo python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-ripozo python3-module-setuptools python3-module-six python3-module-unittest2
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-ripozo-tests python-module-setuptools python-module-tox python-module-virtualenv python3-module-coverage python3-module-html5lib python3-module-jinja2-tests python3-module-mock python3-module-ripozo-tests python3-module-setuptools python3-module-tox python3-module-virtualenv rpm-build-python3 time

%description
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

%if_with python3
%package -n python3-module-%oname
Summary: An tool for easily making RESTful interfaces
Group: Development/Python3
%py3_provides %oname
%py3_requires six jinja2 json logging

%description -n python3-module-%oname
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

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

export PYTHONPATH=%buildroot%python_sitelibdir
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.27-alt1.dev0.git20150423.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.27-alt1.dev0.git20150423.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.27-alt1.dev0.git20150423.1
- NMU: Use buildreq for BR.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.27-alt1.dev0.git20150423
- Version 0.1.27.dev0

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20-alt1.dev0.git20150324
- Initial build for Sisyphus

