%define oname pydocstyle

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt2
Summary: Python docstring style checker
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pydocstyle

# https://github.com/PyCQA/pydocstyle.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-objects.inv python-module-sphinxcontrib-issuetracker
BuildRequires: python-module-html5lib python-module-mock python-module-pytest python-module-pathlib
BuildRequires: python2.7(backports.configparser)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-mock python3-module-pytest python3-module-pathlib
BuildRequires: python3(backports.configparser) python3(snowballstemmer)
%endif

%description
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python docstring style checker
Group: Development/Python3

%description -n python3-module-%oname
pydocstyle is a static analysis tool for checking
compliance with Python docstring conventions.

pydocstyle supports most of PEP 257 out of the box,
but it should not be considered a reference implementation.
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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
# those tests are known to fail
rm -f src/tests/test_integration.py
PYTHONPATH=%buildroot%python_sitelibdir py.test -vv
%if_with python3
pushd ../python3
# those tests are known to fail
rm -f src/tests/test_integration.py
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 -vv
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt2
- Upstream renamed package to pydocstyle from pep257.

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Updated to upstream version 2.1.1.

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.alpha.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.alpha.git20150226.1
- NMU: Use buildreq for BR.

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.alpha.git20150226
- Version 0.5.0-alpha
- Added docs

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

