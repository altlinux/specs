%define oname pycollada
Name: python-module-%oname
Version: 0.3
Release: alt1.git20111115
Summary: A python COLLADA library. Can be used to create, edit and load COLLADA documents
License: BSD
Group: Development/Python
Url: https://github.com/pycollada/pycollada
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pycollada/pycollada.git
Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
pycollada is a python module for creating, editing and loading COLLADA,
which is a COLLAborative Design Activity for establishing an interchange
file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a
python object. In addition, it supports creating a collada python object
from scratch, as well as in-place editing.

%package tests
Summary: Tests for pycollada
Group: Development/Python
Requires: %name = %version-%release

%description tests
pycollada is a python module for creating, editing and loading COLLADA,
which is a COLLAborative Design Activity for establishing an interchange
file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a
python object. In addition, it supports creating a collada python object
from scratch, as well as in-place editing.

This package contains tests for pycollada

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc AUTHORS CHANGELOG.md COPYING README.markdown 
%python_sitelibdir/*
%exclude %python_sitelibdir/collada/tests

%files tests
%python_sitelibdir/collada/tests

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20111115
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110831.1
- Rebuild with Python-2.7

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110831
- Initial build for Sisyphus

