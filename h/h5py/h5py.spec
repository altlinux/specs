%define hdf5dir %_libdir/hdf5-seq

%def_with python3

Name: h5py
Version: 2.7.1
Release: alt1
Summary: Python interface to the Hierarchical Data Format library, version 5
License: MIT
Group: Development/Python
Url: http://www.h5py.org/

# https://github.com/h5py/h5py.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: python-devel libnumpy-devel libhdf5-devel
BuildRequires: libsz2-devel python-module-Cython python-module-Pyrex
BuildRequires: python-module-sphinx-devel python-module-Pygments
BuildRequires: python-module-setuptools-tests python-module-six
BuildRequires: python-module-pkgconfig
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: python3-module-setuptools-tests
BuildRequires: python3-module-Cython python3-module-six
BuildRequires: python3-module-pkgconfig
%endif

%description
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.

%package -n python-module-%name
Summary: Python interface to the Hierarchical Data Format library, version 5
Group: Development/Python
%setup_python_module %name
%py_requires multiprocessing
%py_requires h5py.tests

%description -n python-module-%name
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.

%if_with python3
%package -n python3-module-%name
Summary: Python interface to the Hierarchical Data Format library, version 5
Group: Development/Python3
%py3_requires h5py.tests

%description -n python3-module-%name
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.
%endif

%package -n python-module-%name-doc
Summary: Documentation for Python interface to the HDF5
Group: Development/Documentation
BuildArch: noarch

%description -n python-module-%name-doc
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.

This package contains development documentation for H5PY.

%package -n python-module-%name-pickles
Summary: Pickles for Python interface to the HDF5
Group: Development/Python

%description -n python-module-%name-pickles
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.

This package contains pickles for H5PY.

%package -n python-module-%name-tests
Summary: Tests for Python interface to the HDF5
Group: Development/Python
Requires: python-module-%name = %version-%release

%description -n python-module-%name-tests
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.

This package contains tests for H5PY.

%if_with python3
%package -n python3-module-%name-tests
Summary: Tests for Python interface to the HDF5
Group: Development/Python3
Requires: python3-module-%name = %version-%release

%description -n python3-module-%name-tests
HDF5 for Python (h5py) is a general-purpose Python interface to the
Hierarchical Data Format library, version 5. HDF5 is a versatile, mature
scientific software library designed for the fast, flexible storage of
enormous amounts of data.

From a Python programmer's perspective, HDF5 provides a robust way to
store data, organized by name in a tree-like fashion. You can create
datasets (arrays on disk) hundreds of gigabytes in size, and perform
random-access I/O on desired sections. Datasets are organized in a
filesystem-like hierarchy using containers called "groups", and accessed
using the tradional POSIX /path/to/resource syntax.

H5py provides a simple, robust read/write interface to HDF5 data from
Python. Existing Python and Numpy concepts are used for the interface;
for example, datasets on disk are represented by a proxy class that
supports slicing, and has dtype and shape attributes. HDF5 groups are
presented using a dictionary metaphor, indexed by name.

This package contains tests for H5PY.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

sed -i 's|@PYVER@|%_python_version|g' docs/Makefile

%prepare_sphinx .
ln -s ../objects.inv docs/
ln -s ../objects.inv docs_api/

%build
%add_optflags -fno-strict-aliasing
python setup.py configure --hdf5=%hdf5dir
python api_gen.py
%python_build_debug

%if_with python3
pushd ../python3
python3 setup.py configure --hdf5=%hdf5dir
python3 api_gen.py
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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd
%make -C docs_api html

install -d %buildroot%python_sitelibdir/%name/examples
install -p -m644 examples/* %buildroot%python_sitelibdir/%name/examples
touch %buildroot%python_sitelibdir/%name/examples/__init__.py

install -d %buildroot%_docdir/%name
cp -fR docs/_build/html %buildroot%_docdir/%name/html
cp -fR docs_api/_build/html %buildroot%_docdir/%name/api
cp -fR lzf %buildroot%_docdir/%name/
#install -m644 docs/build/latex/*.pdf %buildroot%_docdir/%name/pdf

# pickles

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%name/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files -n python-module-%name
%doc licenses *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%name/pickle
%exclude %python_sitelibdir/%name/examples
%exclude %python_sitelibdir/*/tests

%files -n python-module-%name-doc
%_docdir/%name

%files -n python-module-%name-tests
%python_sitelibdir/*/tests
%python_sitelibdir/%name/examples

%files -n python-module-%name-pickles
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/pickle

%if_with python3
%files -n python3-module-%name
%doc licenses *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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

