%define mname yieldfrom
%define oname %mname.requests

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20141019.1
Summary: asyncio port of Requests: "Python HTTP for Humans"
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.requests/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rdbhost/yieldfromRequests.git
Source: %name-%version.tar

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest-cov python-module-wheel
BuildPreReq: python-module-asyncio python-module-chardet
BuildPreReq: python-module-yieldfrom.urllib3
BuildPreReq: python-module-yieldfrom.http.client
%endif
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python3-module-sphinx kr-sphinx-themes
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cov python3-module-wheel
BuildPreReq: python3-module-asyncio python3-module-chardet
BuildPreReq: python3-module-yieldfrom.urllib3
BuildPreReq: python3-module-yieldfrom.http.client
%endif

%py_provides %oname requests
%py_requires %mname asyncio chardet
%py_requires yieldfrom.http.client yieldfrom.urllib3
Conflicts: python-module-requests

%description
Requests is an Apache2 Licensed HTTP library, written in Python, for
human beings.

yieldfrom.Requests is the same library, ported to run under Python's
asyncio.

%package -n python3-module-%oname
Summary: asyncio port of Requests: "Python HTTP for Humans"
Group: Development/Python3
%py3_provides %oname requests
%py3_requires %mname asyncio chardet
%py3_requires yieldfrom.http.client yieldfrom.urllib3
Conflicts: python3-module-requests

%description -n python3-module-%oname
Requests is an Apache2 Licensed HTTP library, written in Python, for
human beings.

yieldfrom.Requests is the same library, ported to run under Python's
asyncio.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Requests is an Apache2 Licensed HTTP library, written in Python, for
human beings.

yieldfrom.Requests is the same library, ported to run under Python's
asyncio.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Requests is an Apache2 Licensed HTTP library, written in Python, for
human beings.

yieldfrom.Requests is the same library, ported to run under Python's
asyncio.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx %mname
ln -s ../objects.inv %mname/docs/
cp -fR %_datadir/kr-sphinx-themes yieldfrom/docs/_themes
ln -s ../LICENSE %mname/

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
aFile=$(ls %buildroot%python_sitelibdir_noarch/*.pth)
echo %mname >$aFile
%endif

%if_with python3
pushd ../python3
%python3_install
aFile=$(ls %buildroot%python3_sitelibdir_noarch/*.pth)
echo %mname >$aFile
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD
%make -C %mname/docs pickle
%make -C %mname/docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR %mname/docs/_build/pickle \
	%buildroot%python_sitelibdir/%oname/

%check
%if_with python2
python setup.py test
py.test test_requests.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version test_requests.py
popd
%endif

%if_with python2
%files
%doc NOTICE *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc %mname/docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc NOTICE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt1.git20141019.1
- NMU just rebuild.

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141019
- Initial build for Sisyphus

