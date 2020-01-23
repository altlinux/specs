%define oname atelier

Name: python3-module-%oname
Version: 1.1.9
Release: alt1

Summary: A collection of tools for software artists
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/atelier/
BuildArch: noarch

# https://github.com/lsaffre/atelier.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-unipath
BuildRequires: python3-module-future python3-module-dateutil

%py3_provides %oname
Conflicts: python-module-%oname


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
Group: Development/Python3
Requires: %name = %EVR

%description tests
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

This package contains tests for %oname.

%package sphinxconf
Summary: Sphinx extention for %oname
Group: Development/Python3
Requires: %name = %EVR

%description sphinxconf
`atelier` is a collection of tools for managing and
maintaining multiple Python software projects.

This package contains Sphinx extention for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
pushd docs
sphinx-build-3 -b pickle -d _build/doctrees . _build/pickle
sphinx-build-3 -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/sphinxconf

%files sphinxconf
%python3_sitelibdir/*/sphinxconf

%files tests
%python3_sitelibdir/*/test.*

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.9-alt1
- Version updated to 1.1.9
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.14-alt1.git20150315.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.14-alt1.git20150315
- Initial build for Sisyphus

