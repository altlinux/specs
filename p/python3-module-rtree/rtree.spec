%define _unpackaged_files_terminate_build 1
%define oname rtree
%define srcname Rtree

# check failed on i586
%ifarch %ix86
%def_disable check
%endif

Name: python3-module-%oname
Version: 0.9.4
Release: alt1

Summary: R-Tree spatial index for Python GIS

License: LGPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/Rtree/

# https://github.com/Toblerity/rtree.git
# Source-url: https://files.pythonhosted.org/packages/source/R/%srcname/%srcname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: spatialindex-devel
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy

Requires: spatialindex

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

# Delete junk from tarball.
rm -rf Rtree.egg-info
find . -name '*.pyc' -delete
rm setup.cfg
rm -rf docs/build

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build

%install
%python3_install

%make -C docs html SPHINXBUILD=sphinx-build-3

%check
export LC_ALL=en_US.UTF-8

PYTHONPATH="%buildroot%python3_sitelibdir" \
    py.test3 -ra tests
PYTHONPATH="%buildroot%python3_sitelibdir" \
    py.test3 -ra --doctest-modules rtree

%files
%doc *.txt *.md
%python3_sitelibdir/*

%files docs
%doc docs/build/html/*

%changelog
* Tue Jul 27 2021 Anton Midyukov <antohami@altlinux.org> 0.9.4-alt1
- new version (0.9.4) with rpmgs script
- enable check
- BuildArch: noarch

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

