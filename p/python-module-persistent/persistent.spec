%define oname persistent

%def_with python3

Name: python-module-%oname
Version: 4.2.4.2
Release: alt1.1

%setup_python_module %oname

Summary: Translucent persistent objects
License: ZPL 2.1
Group: Development/Python

Url: http://www.zope.org/Products/ZODB

# https://github.com/zopefoundation/persistent.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-repoze.sphinx.autointerface
BuildRequires: python-dev python-module-coverage python-module-nose python-module-setuptools python-module-zope
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-coverage python3-module-nose python3-module-setuptools python3-module-zope
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
%endif

%py_provides persistent.TimeStamp

%description
This package contains a generic persistence implementation for Python.
It forms the core protocol for making objects interact "transparently"
with a database such as the ZODB.

%package docs
Summary: Documentation for translucent persistent objects
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%package tests
Summary: Tests for translucent persistent objects
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains a generic tests persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%if_with python3
%package -n python3-module-%oname
Summary: Sample python3 module specfile
Group: Development/Python
%py3_provides persistent.TimeStamp

%description -n python3-module-%oname
This specfile is provided as sample specfile for python3 module
packages. It contains most of usual tags and constructions used in such
specfiles.

%package -n python3-module-%oname-tests
Summary: Sample python3 module tests specfile
Group: Development/Python
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This specfile is provided as sample specfile for python3 module tests
packages. It contains most of usual tags and constructions used in such
specfiles.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
install -p -m644 persistent/_compat.h \
	%buildroot%_includedir/python%_python3_version%_python3_abiflags/
popd
%endif

%python_install
install -p -m644 persistent/_compat.h \
	%buildroot%_includedir/python%_python_version/

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=%python_sitelibdir:%python_sitelibdir_noarch
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27-pure-cffi -v

%if_with python3
pushd ../python3
export PYTHONPATH=%python3_sitelibdir:%python3_sitelibdir_noarch
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py35 -v
popd
%endif

%files
%doc *.txt
%_includedir/python%_python_version
%python_sitelibdir/%oname/
%exclude %python_sitelibdir/%oname/test*
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%oname/test*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_includedir/python%_python3_version%_python3_abiflags
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/test*
%python3_sitelibdir/*.egg-info

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.4.2-alt1
- Updated to upstream version 4.2.4.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt2.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Really version 4.1.1

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1.1
- Fixed build

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.6-alt1
- Initial build for ALT Linux Sisyphus
