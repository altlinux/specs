%define _unpackaged_files_terminate_build 1
%define oname jupyter_core

%def_with python3
%def_enable check

Name: python-module-%oname
Version: 4.4.0
Release: alt2
Summary: Jupyter core package
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/jupyter_core

Source: %oname-%version.tar
Source2: %oname-%version-alt-tests.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
BuildRequires: python-module-zope python-module-pytest python2.7(traitlets.config) python2.7(mock)
BuildRequires: python2.7(sphinxcontrib_github_alt)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-zope python3-module-pytest python3(traitlets.config) python3(mock)
BuildRequires: python3(sphinxcontrib_github_alt)
%endif

%py_provides %oname

Conflicts: python-module-jupyter <= 1.0.0-alt1
Obsoletes: python-module-jupyter <= 1.0.0-alt1

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
# disable tests messing with env since package is not properly installed to system
patch -p2 < %SOURCE2
LC_ALL=en_US.UTF-8 PYTHONPATH=%buildroot%python_sitelibdir py.test -vv
%if_with python3
pushd ../python3
rm -fR build
# disable tests messing with env since package is not properly installed to system
patch -p2 < %SOURCE2
LC_ALL=en_US.UTF-8 PYTHONPATH=%buildroot%python_sitelibdir py.test3 -vv
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
* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt2
- Updated build dependencies.

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream version 4.4.0.
- Enabled tests.

* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt2
- added conflict on python-module-jupyter

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

