%define oname evelink

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1.p2.git20141130.1
Summary: Python Bindings for the EVE Online API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/EVELink/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eve-val/evelink.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-requests
#BuildPreReq: python-module-argparse python-module-coverage
#BuildPreReq: python-module-coveralls python-module-mock
#BuildPreReq: python-module-nose python-module-unittest2
#BuildPreReq: python-modules-wsgiref python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-requests
#BuildPreReq: python3-module-argparse python3-module-coverage
#BuildPreReq: python3-module-coveralls python3-module-mock
#BuildPreReq: python3-module-nose python3-module-unittest2
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-funcsigs python-module-linecache2 python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytest python-module-requests python-module-setuptools python-module-six python-module-traceback2 python-module-unittest2 python-module-urllib3 python-module-yaml python-modules python-modules-bsddb python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-requests python3-module-setuptools python3-module-sh python3-module-six python3-module-unittest2 python3-module-urllib3 python3-module-yaml xz
BuildRequires: python-module-mock python-module-nose python-module-setuptools-tests python-module-z4r-coveralls python-modules-sqlite3 python-modules-wsgiref python3-module-html5lib python3-module-mock python3-module-nose python3-module-setuptools-tests python3-module-z4r-coveralls python3-modules-sqlite3 rpm-build-python3 time

%description
EVELink provides a means to access the EVE XML API from Python.

%package -n python3-module-%oname
Summary: Python Bindings for the EVE Online API
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
EVELink provides a means to access the EVE XML API from Python.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
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

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.p2.git20141130.1
- NMU: Use buildreq for BR.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.p2.git20141130
- Initial build for Sisyphus

