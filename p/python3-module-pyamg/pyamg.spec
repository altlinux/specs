%define oname pyamg

%def_without docs

Name: python3-module-%oname
Version: 4.0.0
Release: alt1

Summary: PyAMG: Algebraic Multigrid Solvers in Python
License: BSD
Group: Development/Python3
Url: http://code.google.com/p/pyamg/

Source: %name-%version.tar
Patch0: remove-test-failing-on-i586.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libnumpy-py3-devel
BuildRequires: python3-module-scipy python3-module-pybind11 python3-module-m2r
BuildRequires: python3-module-nose python3-module-numpy-testing
%if_with docs
BuildRequires: python3-module-sphinx
%endif


%description
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

%if_with docs
%package docs
Summary: Documentation for PyAMG
Group: Development/Documentation
BuildArch: noarch

%description docs
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains documentation for PyAMG.
%endif

%package tests
Summary: Tests for PyAMG
Group: Development/Python3
Requires: %name = %EVR

%description tests
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains tests for PyAMG.

%prep
%setup
%ifarch i586
%patch -p2
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=$PWD

pushd Docs/
make man
popd
%endif

%check
%__python3 setup.py build_ext -i

%files
%doc *.txt *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests

%if_with docs
%files docs
%doc Docs/build/man
%endif

%files tests
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%exclude %python3_sitelibdir/%oname/*/example*


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.0-alt1
- Version updated to 4.0.0
- porting on python3

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2
- Fixed build

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2
- Avoid requirement on pythonX.Y(example)

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Feb 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt2
- Moved examples into tests subpackage

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1
- Initial build for Sisyphus

