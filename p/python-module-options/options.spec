%define oname options

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1.1.1
Summary: Simple, super-flexible options. Does magic upon request.
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/options
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-stuf python-module-six
#BuildPreReq: python-module-nulltype python-module-tox
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-stuf python3-module-six
#BuildPreReq: python3-module-nulltype python3-module-tox
%endif

%py_provides %oname
%py_requires stuf six nulltype

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-parse python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-parse python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nulltype python-module-objects.inv python-module-stuf python-module-tox python3-module-nulltype python3-module-six python3-module-stuf python3-module-tox rpm-build-python3 time python3-module-pytest

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

