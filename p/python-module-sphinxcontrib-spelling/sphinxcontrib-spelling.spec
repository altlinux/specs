%define oname sphinxcontrib-spelling

Name: python-module-%oname
Version: 2.1.1
Release: alt1

Summary: Sphinx "spelling" extension
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-spelling

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-enchant
BuildPreReq: python-module-setuptools python-module-pbr
BuildPreReq: python-module-sphinx-devel

Requires: python-module-sphinxcontrib = %EVR

%description
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains documentation for %oname.

%package -n python-module-sphinxcontrib
Summary: Core package of sphinxcontrib
Group: Development/Python

%description -n python-module-sphinxcontrib
Core package of sphinxcontrib.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%install
%python_install

touch %buildroot%python_sitelibdir/sphinxcontrib/__init__.py

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS ChangeLog README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.py*
%dir %python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/*/tests

%files docs
%doc docs/build/html/*

%files -n python-module-sphinxcontrib
%python_sitelibdir/*/__init__.py*

%changelog
* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

