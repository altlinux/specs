%define oname clize

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 4.0.3
Release: alt1

Summary: Command-line argument parsing for Python, without the effort

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/clize/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/epsy/clize.git
# Source-url: https://pypi.io/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sigtools python-module-six
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sigtools >= 2.0
BuildRequires: python3-module-attrs >= 17.4.0
BuildRequires: python3-module-six
BuildRequires: python3-module-od
BuildRequires: python3(dateutil)
BuildRequires: python3(unittest2) python3(repeated_test) python3(pygments)
%endif

%py_provides %oname
%py_requires sigtools six

BuildRequires(pre): rpm-macros-sphinx
%if_with python2
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python-module-sigtools
%endif
BuildRequires: time

%description
Clize procedurally turns your functions into convenient command-line
interfaces.

%package -n python3-module-%oname
Summary: Command-line argument parsing for Python, without the effort
Group: Development/Python3
%py3_provides %oname
%py3_requires sigtools six

%description -n python3-module-%oname
Clize procedurally turns your functions into convenient command-line
interfaces.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Clize procedurally turns your functions into convenient command-line
interfaces.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Clize procedurally turns your functions into convenient command-line
interfaces.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%if_with python2
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

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
%endif

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/clize/tests/
popd
%endif

%if_with python2
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)
- build python3 module only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.a2.git20150111.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.a2.git20150111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt1.a2.git20150111.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.a2.git20150111
- Initial build for Sisyphus

