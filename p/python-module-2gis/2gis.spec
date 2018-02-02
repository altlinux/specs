%define oname 2gis

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20140722.1.1.1
Summary: 2gis library for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/2gis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/svartalf/python-2gis.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-requests python-module-six
#BuildPreReq: python-module-mock
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-requests python3-module-six
#BuildPreReq: python3-module-mock
%endif

%py_provides dgis
%py_requires requests six

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-traceback2 python-module-unittest2 python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-linecache2 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-traceback2 python3-module-unittest2 python3-module-urllib3
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-requests python-module-setuptools python3-module-html5lib python3-module-mock python3-module-requests python3-module-setuptools rpm-build-python3 time

%description
A Python library for accessing the 2gis API.

%package -n python3-module-%oname
Summary: 2gis library for Python
Group: Development/Python3
%py3_provides dgis
%py3_requires requests six

%description -n python3-module-%oname
A Python library for accessing the 2gis API.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A Python library for accessing the 2gis API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A Python library for accessing the 2gis API.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.git20140722.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20140722.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1.git20140722.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20140722
- Initial build for Sisyphus

