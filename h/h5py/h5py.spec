%define hdf5dir %_libdir/hdf5-seq
Name: h5py
Version: 2.1.0
Release: alt2.beta.hg20120219
Summary: Python interface to the Hierarchical Data Format library, version 5
License: MIT
Group: Development/Python
Url: http://code.google.com/p/h5py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.google.com/p/h5py/
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel libnumpy-devel libhdf5-devel strace
BuildPreReq: libsz2-devel python-module-Cython python-module-Pyrex
BuildPreReq: python-module-sphinx-devel python-module-Pygments
#BuildPreReq: texlive-latex-recommended

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

%prep
%setup

sed -i 's|@PYVER@|%_python_version|g' docs/Makefile

%prepare_sphinx docs

%build
#python setup.py cython
#python setup.py configure --hdf5=%hdf5dir --api=18
pushd %name
python api_gen.py
popd
%add_optflags -fno-strict-aliasing
%python_build_debug --hdf5=%hdf5dir --api=18

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd

install -d %buildroot%python_sitelibdir/%name/examples
install -p -m644 examples/* %buildroot%python_sitelibdir/%name/examples
touch %buildroot%python_sitelibdir/%name/examples/__init__.py

install -d %buildroot%_docdir/%name
cp -fR docs/build/html lzf %buildroot%_docdir/%name/
#install -m644 docs/build/latex/*.pdf %buildroot%_docdir/%name/pdf

# pickles

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%name/

%files -n python-module-%name
%doc licenses *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%name/pickle
%exclude %python_sitelibdir/%name/examples
%exclude %python_sitelibdir/*/lowtest
%exclude %python_sitelibdir/*/*/tests

%files -n python-module-%name-doc
%_docdir/%name

%files -n python-module-%name-tests
%python_sitelibdir/*/lowtest
%python_sitelibdir/*/*/tests

%files -n python-module-%name-pickles
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/pickle

%changelog
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

