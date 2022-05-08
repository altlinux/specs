%define mname svg
%define oname %mname.charts

%def_without doc
%def_without check

Name: python3-module-%oname
Version: 6.1
Release: alt3

Summary: Python SVG Charting Library

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/svg.charts/

# Source-url: https://pypi.io/packages/source/s/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

%if_with doc
BuildRequires: rpm-macros-sphinx3 python3-module-sphinx python3-module-rst.linker
BuildRequires: python3-module-jaraco.packaging
%endif

%if_with check
BuildRequires: python3-module-jaraco.itertools 
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-cssutils python3-module-dateutil
BuildRequires: python3-module-lxml python3-module-six
BuildRequires: python3-module-pytest-runner python3-module-setuptools_scm
BuildRequires: python3-module-pytest python3-module-tempora

%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires cssutils dateutil lxml six

%description
svg.charts is a pure-python library for generating charts and graphs in
SVG, originally based on the SVG::Graph Ruby package by Sean E. Russel.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%if_with doc
%package -n python3-module-%oname-doc
Summary: Doc files of %oname
Group: Development/Python3

%description -n python3-module-%oname-doc
Doc files of %oname.
%endif

%prep
%setup

%if_with doc
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build

%install
%python3_install

# fix install hack
[ "%_libexecdir" = %_libdir ] || mv %buildroot%_libexecdir %buildroot%_libdir

install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%if_with doc
export PYTHONPATH=$PWD
pushd docs
sphinx-build-3 -b pickle -d _build/doctrees . _build/pickle
sphinx-build-3 -b html -d _build/doctrees . _build/html
popd
%endif

%check
rm -f conf.py
python3 setup.py test

%files
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*

%if_with doc
%files -n python3-module-%oname-doc
%doc docs/_build/html
%endif

%changelog
* Sun May 08 2022 Grigory Ustinov <grenka@altlinux.org> 6.1-alt3
- Build without docs.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 6.1-alt2
- Rename package, spec cleanup.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt1
- new version 6.1 (with rpmrb script)
- python3 only

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- new version (6.0) with rpmgs script
- separate doc packing
- disable check section (wait for jaraco.*)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt2.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 3.0-alt2
- Fixed build by removing mercurial version check.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

