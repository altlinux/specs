%define oname aiowsgi

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.dev0.git20140814.1.1.1
Summary: Minimalist wsgi server using asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aiowsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gawel/aiowsgi.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-waitress python-module-webob
#BuildPreReq: python-module-nose python-module-webtest
#BuildPreReq: python-module-coverage python-module-coveralls
#BuildPreReq: python-module-mock python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-waitress python3-module-webob
#BuildPreReq: python3-module-nose python3-module-webtest
#BuildPreReq: python3-module-coverage python3-module-coveralls
#BuildPreReq: python3-module-mock python3-module-asyncio
%endif

%py_provides %oname
%py_requires waitress webob trollius

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-BeautifulSoup4 python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-enum34 python-module-futures python-module-genshi python-module-html5lib python-module-lxml python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-setuptools python-module-six python-module-waitress python-module-webob python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-BeautifulSoup4 python3-module-asyncio python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-html5lib python3-module-lxml python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-sh python3-module-six python3-module-waitress python3-module-webob python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 xz
BuildRequires: python-module-nose python-module-pbr python-module-setuptools python-module-trollius python-module-unittest2 python-module-webtest python-module-z4r-coveralls python3-module-nose python3-module-pbr python3-module-setuptools python3-module-unittest2 python3-module-webtest python3-module-z4r-coveralls rpm-build-python3 time

%description
Minimalist wsgi server using asyncio.

%package -n python3-module-%oname
Summary: Minimalist wsgi server using asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires waitress webob asyncio

%description -n python3-module-%oname
Minimalist wsgi server using asyncio.

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
export PYTHONPATH=$PWD
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
nosetests3 -v
popd
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1.dev0.git20140814.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.dev0.git20140814.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.dev0.git20140814.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.dev0.git20140814
- Initial build for Sisyphus

