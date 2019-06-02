%define _unpackaged_files_terminate_build 1
%define oname rtree
%define sover 4

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.8.3
Release: alt2

Summary: R-Tree spatial index for Python GIS

License: LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Rtree/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Toblerity/rtree.git
# Source-url: https://pypi.io/packages/source/r/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires: spatialindex-devel
%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-sphinx-devel
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: rpm-macros-sphinx3 python3-module-sphinx
BuildRequires: python-tools-2to3
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

%if_with python3
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
%endif

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
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/ 

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%make -C docs pickle SPHINXBUILD=sphinx-build-3
%make -C docs html SPHINXBUILD=sphinx-build-3

%if_with python2
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
export LC_ALL=en_US.UTF-8
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt2
- build python3 module only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1.1
- rebuild with spatialindex

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt2.git20150107
- Fixed build

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20150107
- Initial build for Sisyphus

