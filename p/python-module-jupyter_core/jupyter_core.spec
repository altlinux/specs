%define _unpackaged_files_terminate_build 1
%define oname jupyter_core

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.2.1
Release: alt1
Summary: Jupyter core package
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jupyter_core
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/bc/d0/8f57f733913fbd4ce1a01991b008bace8dcf05158080821c6de76b4c5d01/%{oname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-zope rpm-build-python3 time python3-module-pytest

#BuildRequires: python-module-objects.inv

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-traitlets python-module-mock ipython
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-traitlets python3-module-mock ipython3
#BuildRequires: python3 python3-module-zope
%endif

%py_provides %oname
#%py_requires traitlets

%description
Jupyter core package. A base package on which Jupyter projects rely.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jupyter core package. A base package on which Jupyter projects rely.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Jupyter core package
Group: Development/Python3
%py3_provides %oname
#%py3_requires traitlets

%description -n python3-module-%oname
Jupyter core package. A base package on which Jupyter projects rely.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jupyter core package. A base package on which Jupyter projects rely.

This package contains tests for %oname.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md docs/_build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/_build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt2.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 4.0.4-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus

