%define oname aiowsgi

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.dev0.git20140814
Summary: Minimalist wsgi server using asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aiowsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gawel/aiowsgi.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-waitress python-module-webob
BuildPreReq: python-module-nose python-module-webtest
BuildPreReq: python-module-coverage python-module-coveralls
BuildPreReq: python-module-mock python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-waitress python3-module-webob
BuildPreReq: python3-module-nose python3-module-webtest
BuildPreReq: python3-module-coverage python3-module-coveralls
BuildPreReq: python3-module-mock python3-module-asyncio
%endif

%py_provides %oname
%py_requires waitress webob trollius

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
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.dev0.git20140814
- Initial build for Sisyphus

