%define oname atelier
Name: python-module-%oname
Version: 0.0.14
Release: alt1.git20150315.1
Summary: A collection of tools for software artists
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/atelier/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lsaffre/atelier.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-Fabric
BuildPreReq: python-module-babel python-module-unipath
BuildPreReq: python-module-dateutil
BuildPreReq: python-modules-logging
BuildPreReq: python-module-sphinx-devel

%py_provides %oname
%py_requires logging fabric babel unipath dateutil

%description
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

It contains

- some general Python utilities (:mod:`atelier.utils`)
- a library for generating reStructuredText from Python
  (:mod:`atelier.rstgen`)
- some Sphinx extensions (:mod:`atelier.sphinxconf`)
- a library of fabric commands (:mod:`atelier.fablib`)
- a minimalistic project management

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

This package contains tests for %oname.

%package sphinxconf
Summary: Sphinx extention for %oname
Group: Development/Python
Requires: %name = %EVR

%description sphinxconf
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

This package contains Sphinx extention for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test.*
%exclude %python_sitelibdir/*/sphinxconf

%files sphinxconf
%python_sitelibdir/*/sphinxconf

%files tests
%python_sitelibdir/*/test.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.14-alt1.git20150315.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.14-alt1.git20150315
- Initial build for Sisyphus

