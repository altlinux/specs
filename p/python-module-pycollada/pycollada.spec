%define oname pycollada

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt2.git20140411.1
Summary: A python COLLADA library. Can be used to create, edit and load COLLADA documents
License: BSD
Group: Development/Python
Url: https://github.com/pycollada/pycollada
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pycollada/pycollada.git
Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
pycollada is a python module for creating, editing and loading COLLADA,
which is a COLLAborative Design Activity for establishing an interchange
file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a
python object. In addition, it supports creating a collada python object
from scratch, as well as in-place editing.

%package -n python3-module-%oname
Summary: A python COLLADA library. Can be used to create, edit and load COLLADA documents
Group: Development/Python3

%description -n python3-module-%oname
pycollada is a python module for creating, editing and loading COLLADA,
which is a COLLAborative Design Activity for establishing an interchange
file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a
python object. In addition, it supports creating a collada python object
from scratch, as well as in-place editing.

%package -n python3-module-%oname-tests
Summary: Tests for pycollada
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pycollada is a python module for creating, editing and loading COLLADA,
which is a COLLAborative Design Activity for establishing an interchange
file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a
python object. In addition, it supports creating a collada python object
from scratch, as well as in-place editing.

This package contains tests for pycollada

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS.md CHANGELOG.rst COPYING README.markdown 
%python_sitelibdir/*
%exclude %python_sitelibdir/collada/tests

%files tests
%python_sitelibdir/collada/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS.md CHANGELOG.rst COPYING README.markdown 
%python3_sitelibdir/*
%exclude %python3_sitelibdir/collada/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/collada/tests
%endif

%changelog
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

