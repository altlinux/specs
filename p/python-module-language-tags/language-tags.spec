# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20141218.1.1.1.1
%define oname language-tags

%def_with python3

Name: python-module-%oname
Version: 0.2.0
#Release: alt1.git20141218.1.1
Summary: This project is a Python version of the language-tags Javascript project
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/language-tags/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/OnroerendErfgoed/language-tags.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-nose
#BuildPreReq: python-module-pytest-cov
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-nose
#BuildPreReq: python3-module-pytest-cov
%endif

%py_provides language_tags
%py_requires six

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-coverage python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest-cov python-module-setuptools python3-module-nose python3-module-pytest-cov python3-module-setuptools python3-module-six rpm-build-python3 time

# optimized out: -=FIXES: python2.7(sphinx_rtd_theme)
BuildRequires: python2.7(sphinx_rtd_theme)

%description
This Python API offers a way to validate and lookup languages tags.

It is based on BCP 47 (RFC 5646) and the latest IANA language subtag
registry.

%package -n python3-module-%oname
Summary: This project is a Python version of the language-tags Javascript project
Group: Development/Python3
%py3_provides language_tags
%py3_requires six

%description -n python3-module-%oname
This Python API offers a way to validate and lookup languages tags.

It is based on BCP 47 (RFC 5646) and the latest IANA language subtag
registry.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This Python API offers a way to validate and lookup languages tags.

It is based on BCP 47 (RFC 5646) and the latest IANA language subtag
registry.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This Python API offers a way to validate and lookup languages tags.

It is based on BCP 47 (RFC 5646) and the latest IANA language subtag
registry.

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20141218.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141218.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141218
- Initial build for Sisyphus

