%define _unpackaged_files_terminate_build 1

# disable tests on 32bit architectures
%ifnarch %ix86 armh
%def_with check
%else
%def_without check
%endif

%def_without docs

%define descr \
HDF5 for Python (h5py) is a general-purpose Python interface to the \
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature \
scientific software library designed for the fast, flexible storage of \
enormous amounts of data. \
\
From a Python programmer's perspective, HDF5 provides a robust way to \
store data, organized by name in a tree-like fashion. You can create \
datasets (arrays on disk) hundreds of gigabytes in size, and perform \
random-access I/O on desired sections. Datasets are organized in a \
filesystem-like hierarchy using containers called "groups", and accessed \
using the tradional POSIX /path/to/resource syntax. \
\
H5py provides a simple, robust read/write interface to HDF5 data from \
Python. Existing Python and Numpy concepts are used for the interface; \
for example, datasets on disk are represented by a proxy class that \
supports slicing, and has dtype and shape attributes. HDF5 groups are \
presented using a dictionary metaphor, indexed by name.

Name:       h5py
Version:    3.2.1
Release:    alt3

Summary:    Python interface to the Hierarchical Data Format library, version 5
License:    MIT
Group:      Development/Python3
Url:        http://www.h5py.org/

#           https://github.com/h5py/h5py.git
Source:     %name-%version.tar

Patch1:     %name-alt-doc.patch
Patch2:     %name-alt-build.patch

BuildRequires: libhdf5-devel
BuildRequires: libsz2-devel
BuildRequires: libblosc2-devel

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-mpi4py-devel
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-module-sphinx-devel
%if_with check
BuildRequires: python3-module-numpy-testing
BuildRequires: python3(pytest_mpi)
%endif

%description
%descr

%package -n python3-module-%name
Summary: Python interface to the Hierarchical Data Format library, version 5
Group: Development/Python3
%add_python3_req_skip Tkinter

%description -n python3-module-%name
%descr

%if_with docs
%package -n python3-module-%name-doc
Summary: Documentation for Python interface to the HDF5
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%name-doc
%descr

This package contains development documentation for H5PY.

%package -n python3-module-%name-pickles
Summary: Pickles for Python interface to the HDF5
Group: Development/Python3

%description -n python3-module-%name-pickles
%descr

This package contains pickles for H5PY.
%endif

%package -n python3-module-%name-tests
Summary: Tests for Python interface to the HDF5
Group: Development/Python3
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-tests
%descr

This package contains tests for H5PY.

%prep
%setup
%patch1 -p1
%patch2 -p1

%if_with docs
sed -i 's|@PYVER@|%_python3_version|g' docs/Makefile
%endif

%build
%add_optflags -fno-strict-aliasing

%__python3 api_gen.py
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd docs
%make html
%make pickle
popd
%make -C docs_api html

install -d %buildroot%_docdir/%name
cp -fR docs/_build/html %buildroot%_docdir/%name/html
cp -fR docs_api/_build/html %buildroot%_docdir/%name/api
cp -fR lzf %buildroot%_docdir/%name/

# pickles
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%name/
%endif

install -d %buildroot%python3_sitelibdir/%name/examples
install -p -m644 examples/* %buildroot%python3_sitelibdir/%name/examples
touch %buildroot%python3_sitelibdir/%name/examples/__init__.py

%check
%__python3 setup.py test

%files -n python3-module-%name
%doc licenses *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/%name/examples
%if_with docs
%exclude %python3_sitelibdir/%name/pickle

%files -n python3-module-%name-doc
%_docdir/%name

%files -n python3-module-%name-pickles
%dir %python3_sitelibdir/%name
%python3_sitelibdir/%name/pickle
%endif

%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/%name/examples

%changelog
* Fri Feb 03 2023 Anton Vyatkin <toni@altlinux.org> 3.2.1-alt3
- Fixed BuildRequires.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt2
- Fixed BuildRequires.

* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1
- Updated to upstream version 3.2.1.

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt3
- fix build, fix tests packing

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.0-alt2
- Fixed build with numpy.

* Fri Feb 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.10.0-alt1
- Version updated to 2.10.0
- build for python2 disabled.

* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt4
- Enabled tests (disabled to ppc64le only)
- cleanup build requires.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt3
- Fixed build requires.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 2.9.0-alt2
- Added missing dep on `numpy.testing`.

* Wed Mar 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.1-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.1-alt1
- Updated to upstream version 2.7.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt2.git20150720.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt2.git20150720
- Version 2.5.0

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.a0.git20150227
- Version 2.5.0a0

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.b1.git20141107
- New snapshot

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.b1.git20141031
- Version 2.4.0b1
- Enabled testing

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.a0.git20140805
- New snapshot
- Added module for Python 3

* Fri Jul 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.a0.git20140625
- Version 2.4.0a0

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.a1.hg20120919
- Rebuilt with new libhdf5

* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.a1.hg20120919
- Version 2.2.0a1

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.beta.hg20120911
- New snapshot

* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.beta.hg20120219
- Rebuilt

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1.beta.hg20120219.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.beta.hg20120219
- Version 2.1.0-beta

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.hg20111016
- Version 2.0.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt1.svn20101222.1.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20101222.1
- Rebuilt with libhdf5-7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20101222
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20100926.2
- Rebuild with python-module-sphinx-devel

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20100926.1
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20100926
- Version 1.3.1

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20100417
- New snapshot

* Mon Mar 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20100319
- New snapshot
- Fixed build

* Thu Mar 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20100304
- Version 1.3.0
- Rebuilt with reformed NumPy
- Added:
  + documentation in PDF
  + tests and pickles packages

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Rebuilt with python 2.6

* Sat Sep 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

