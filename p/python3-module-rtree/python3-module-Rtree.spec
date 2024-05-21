%define _unpackaged_files_terminate_build 1
%define pypi_name Rtree
%define mod_name rtree

%def_with check

Name: python3-module-%mod_name
Version: 1.2.0
Release: alt1

Summary: R-Tree spatial index for Python GIS
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Rtree/
Vcs: https://github.com/Toblerity/rtree

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# PyPI well known name
Provides: python3-module-%pypi_name = %EVR
Requires: spatialindex
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: spatialindex
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

%prep
%setup
%autopatch -p1

# remove setup.py to make the package noarch
rm setup.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGES.rst CREDITS.txt LICENSE.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue May 21 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.
- Built from upstream VCS.

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

