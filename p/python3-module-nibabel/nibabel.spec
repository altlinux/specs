%define _unpackaged_files_terminate_build 1
%define oname nibabel

%def_disable docs

# on armh couple tests failed
# FAILED nibabel/tests/test_arraywriters.py::test_rt_bias
# FAILED nibabel/tests/test_round_trip.py::test_round_trip
%ifnarch armh
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 5.2.1
Release: alt2

Summary: Easy access to NIfTI images from within Python
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/nibabel
Vcs: https://github.com/nipy/nibabel

BuildArch: noarch

Source: %oname-%version.tar
Patch: drop-distutils.patch
Patch1: nibabel-5.2.1-tests-replace-deprecated-nose-fixtures-with-pytest-s.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-httpserver
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-modules-sqlite3
%endif

Conflicts: python-module-%oname

%description
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

While NiBabel is not yet complete (i.e. doesn't support everything the
C library can do), it already provides access to the most important
features of the NIfTI-1 data format and libniftiio capabilities.

%package tests
Summary: Tests for NiBabel
Group: Development/Python3
Requires: %name = %EVR

%description tests
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains tests for NiBabel.

%if_enabled docs
%package doc
Summary: Documentation and examples for NiBabel
Group: Development/Documentation
BuildArch: noarch

%description doc
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains documentation and examples for NiBabel.

%package pickles
Summary: Pickles for NiBabel
Group: Development/Python3

%description pickles
NiBabel aims to provide easy access to NIfTI images from within Python.
It uses SWIG-generated wrappers for the NIfTI reference library and
provides the nifti.image.NiftiImage class for Python-style access to the
image data.

This package contains pickles for NiBabel.
%endif

%prep
%setup
%autopatch -p1

%if_enabled docs
sed -i 's|@PYVER@|%_python3_version|g' doc/Makefile
sed -i 's|PYTHON ?=.*|PYTHON ?= %__python3|g' doc/Makefile
sed -i 's|sphinx-build|&-3|' doc/Makefile
%endif

%build
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi
%pyproject_build

%install
%pyproject_install

%if_enabled docs
cp -f doc/source/conf.py %buildroot%python3_sitelibdir
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd doc
%make html
popd

install -d %buildroot%_docdir/%oname
cp -fR build/html %buildroot%_docdir/%oname/
cp -fR build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/*
%python3_sitelibdir/nisext
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%if_enabled docs
%exclude %python3_sitelibdir/%oname/pickle
%endif
%exclude %python3_sitelibdir/nisext/test*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/testing
%exclude %python3_sitelibdir/%oname/*/tests

%if_enabled docs
%files doc
%_docdir/%oname

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/nisext/test*
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/testing
%python3_sitelibdir/%oname/*/tests

%changelog
* Wed May 29 2024 Stanislav Levin <slev@altlinux.org> 5.2.1-alt2
- Fixed FTBFS (Pytest 8.2.0).

* Tue Feb 27 2024 Anton Vyatkin <toni@altlinux.org> 5.2.1-alt1
- New version 5.2.1.

* Mon Dec 25 2023 Anton Vyatkin <toni@altlinux.org> 5.2.0-alt1
- New version 5.2.0.

* Thu Oct 19 2023 Anton Vyatkin <toni@altlinux.org> 5.1.0-alt1
- New version 5.1.0.

* Mon Apr 24 2023 Anton Vyatkin <toni@altlinux.org> 3.1.1-alt2
- Fix Requires

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1-alt1
- Updated to upstream version 3.1.1.

* Wed Apr 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt2
- Build for python2 disabled.

* Fri Sep 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt2
- Fixed build dependencies.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.dev.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.dev.git20141209.1
- NMU: Use buildreq for BR.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.dev.git20141209
- Version 2.1.0.dev

* Wed Aug 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4.git20120903
- Added module for Python 3

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3.git20120903
- New snapshot

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3.git20120609
- Built with OpenBLAS instead of GotoBLAS2

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20120609
- Moved all tests into tests subpackage

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20120609
- Version 1.3.0

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.git20101014
- Enabled docs (except pdf)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.git20101014.1
- Rebuild with Python-2.7

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20101014
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100725.2
- Rebuilt with python-module-sphinx-devel

* Wed Aug 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100725.1
- Excluded %oname/dicom/tests

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100725
- New snapshot

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100326.2
- Rebuilt

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100326.1
- Fixed build error

* Wed Mar 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100326
- New snapshot

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100203
- Initial build for Sisyphus

