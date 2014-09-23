%define oname facepy

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20140824
Summary: Facepy makes it really easy to interact with Facebook's Graph API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/facepy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jgorset/facepy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Facepy makes it really easy to interact with Facebook's Graph API.

%package -n python3-module-%oname
Summary: Facepy makes it really easy to interact with Facebook's Graph API
Group: Development/Python3

%description -n python3-module-%oname
Facepy makes it really easy to interact with Facebook's Graph API.

%prep
%setup

sed -i 's|@VERSION@|%version|g' docs/source/conf.py

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
%make -C docs html

%files
%doc AUTHORS *.rst docs/build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst docs/build/html
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20140824
- Initial build for Sisyphus

