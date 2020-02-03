%define oname pycollada

Name: python3-module-%oname
Version: 0.4.1
Release: alt3

Summary: A python COLLADA library. Can be used to create, edit and load COLLADA documents
License: BSD
Group: Development/Python3
Url: https://github.com/pycollada/pycollada
BuildArch: noarch

# https://github.com/pycollada/pycollada.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3


%description
pycollada is a python module for creating, editing and loading COLLADA,
which is a COLLAborative Design Activity for establishing an interchange
file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a
python object. In addition, it supports creating a collada python object
from scratch, as well as in-place editing.

%package tests
Summary: Tests for pycollada
Group: Development/Python3
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
%python3_build_debug

%install
%python3_install

%files
%doc AUTHORS.md CHANGELOG.rst COPYING README.markdown 
%python3_sitelibdir/*
%exclude %python3_sitelibdir/collada/tests

%files tests
%python3_sitelibdir/collada/tests


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt3
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2.git20140411.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt2.git20140411.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.git20140411
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140411
- Version 0.4.1

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130302
- Version 0.4

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20111115
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110831.1
- Rebuild with Python-2.7

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110831
- Initial build for Sisyphus

