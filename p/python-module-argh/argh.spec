%define oname argh

%def_with python3

Name: python-module-%oname
Version: 0.26.1
Release: alt1.git20141030.2.1
Summary: An unobtrusive argparse wrapper with natural syntax
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/argh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/neithere/argh.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-coverage python-module-mock
#BuildPreReq: python-module-pytest-cov python-module-pytest-xdist
#BuildPreReq: python-module-tox python-module-argparse
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-coverage python3-module-mock
#BuildPreReq: python3-module-pytest-cov python3-module-pytest-xdist
#BuildPreReq: python3-module-tox python3-module-argparse
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-argcomplete python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-enum34 python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-rlcompleter2 python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-argcomplete python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-unittest2 python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest-cov python-module-pytest-xdist python-module-setuptools python-module-tox python3-module-html5lib python3-module-mock python3-module-pytest-cov python3-module-pytest-xdist python3-module-setuptools python3-module-tox rpm-build-python3 time

%description
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

http://argh.rtfd.org

%package -n python3-module-%oname
Summary: An unobtrusive argparse wrapper with natural syntax
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

http://argh.rtfd.org

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
./coverage.sh
%if_with python3
pushd ../python3
sed -i 's|py.test|py.test3|' coverage.sh \
	test/test_integration.py
./coverage.sh
popd
%endif

%files
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.26.1-alt1.git20141030.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.26.1-alt1.git20141030.2
- Fixed build spec with pytest3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.26.1-alt1.git20141030.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.26.1-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.26.1-alt1.git20141030
- Initial build for Sisyphus

