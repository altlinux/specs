%define oname rtree
%define sover 3

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.8.2
Release: alt1.git20150107
Summary: R-Tree spatial index for Python GIS
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Rtree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Toblerity/rtree.git
Source: %name-%version.tar

#BuildPreReq: spatialindex-devel
BuildPreReq: spatialindex
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%ifarch x86_64
Requires: libspatialindex_c.so.%sover()(64bit)
%else
Requires: libspatialindex_c.so.%sover
%endif

%description
Rtree is a ctypes Python wrapper of libspatialindex that provides a
number of advanced spatial indexing features for the spatially curious
Python user. These features include:

* Nearest neighbor search
* Intersection search
* Multi-dimensional indexes
* Clustered indexes (store Python pickles directly with index entries)
* Bulk loading
* Deletion
* Disk serialization
* Custom storage implementation (to implement spatial indexing in ZODB,
  for example)

%package -n python3-module-%oname
Summary: R-Tree spatial index for Python GIS
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Rtree is a ctypes Python wrapper of libspatialindex that provides a
number of advanced spatial indexing features for the spatially curious
Python user. These features include:

* Nearest neighbor search
* Intersection search
* Multi-dimensional indexes
* Clustered indexes (store Python pickles directly with index entries)
* Bulk loading
* Deletion
* Disk serialization
* Custom storage implementation (to implement spatial indexing in ZODB,
  for example)

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Rtree is a ctypes Python wrapper of libspatialindex that provides a
number of advanced spatial indexing features for the spatially curious
Python user.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Rtree is a ctypes Python wrapper of libspatialindex that provides a
number of advanced spatial indexing features for the spatially curious
Python user.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/ 

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20150107
- Initial build for Sisyphus

