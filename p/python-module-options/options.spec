%define oname options

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1
Summary: Simple, super-flexible options. Does magic upon request.
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/options
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-stuf python-module-six
BuildPreReq: python-module-nulltype python-module-tox
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-stuf python3-module-six
BuildPreReq: python3-module-nulltype python3-module-tox
%endif

%py_provides %oname
%py_requires stuf six nulltype

%description
options helps represent option and configuration data in a clean,
high-function way. Changes to options can "overlay" earlier or default
settings.

%if_with python3
%package -n python3-module-%oname
Summary: Simple, super-flexible options. Does magic upon request.
Group: Development/Python3
%py3_provides %oname
%py3_requires stuf six nulltype

%description -n python3-module-%oname
options helps represent option and configuration data in a clean,
high-function way. Changes to options can "overlay" earlier or default
settings.
%endif

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
export PYTHONPATH=$PWD
py.test --assert=plain -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version --assert=plain -vv
popd
%endif

%files
%doc *.rst README docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst README docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

