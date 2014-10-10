%define oname bottle

%def_with python3

Name: python-module-%oname
Version: 0.13
Release: alt1.dev.git20141002
Summary: Fast and simple WSGI-framework for small web-applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bottle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/defnull/bottle.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

%package -n python3-module-%oname
Summary: Fast and simple WSGI-framework for small web-applications
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Bottle is a fast and simple micro-framework for small web applications.
It offers request dispatching (Routes) with url parameter support,
templates, a built-in HTTP Server and adapters for many third party
WSGI/HTTP-server and template engines - all in a single file and with no
dependencies other than the Python Standard Library.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make docs
sphinx-build -b pickle -d build/docs/doctrees docs build/docs/pickle

install -d %buildroot%python_sitelibdir/%oname
cp -fR build/docs/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc build/docs/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.dev.git20141002
- Initial build for Sisyphus

