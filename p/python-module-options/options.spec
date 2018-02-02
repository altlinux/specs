%define oname options

%def_with python3

Name: python-module-%oname
Version: 1.4.8
Release: alt1.1
Summary: Simple, super-flexible options. Does magic upon request.
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/options

Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-chainmap python-module-combomethod
BuildRequires: python-module-stuf
BuildRequires: python-module-nulltype python-module-tox
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-chainmap python3-module-combomethod
BuildRequires: python3-module-stuf python3-module-six python3-module-pytest
BuildRequires: python3-module-nulltype python3-module-tox
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
%patch1 -p1

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
py.test3 --assert=plain -vv
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.8-alt1
- Updated to upstream version 1.4.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

