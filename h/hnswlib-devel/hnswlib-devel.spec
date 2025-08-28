%define        _unpackaged_files_terminate_build 1
%define        nomen hnswlib
%def_enable    check

Name:          %nomen-devel
Version:       0.8.0
Release:       alt1.1
Summary:       Header-only C++/python library for fast approximate nearest neighbors
License:       Apache-2.0
Group:         Sciences/Mathematics
Url:           https://github.com/nmslib/hnswlib
Vcs:           https://github.com/nmslib/hnswlib.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-pyproject
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pybind11)
BuildRequires: python3(numpy)
%if_enabled check
BuildRequires: python3(tox)
BuildRequires: python3(hypothesis)
%endif

Requires:      rpm-macros-cmake
Requires:      cmake
Requires:      gcc-c++
Requires:      libgomp-devel

%add_optflags -Wno-error=return-type

%description
Header-only C++ HNSW implementation with python bindings, insertions and
updates.

%package       -n python3-module-%nomen
Summary:       HNSW implementation library for Python3
Group:         Development/Python3

%description   -n python3-module-%nomen
HNSW implementation library for Python3

Header-only C++ HNSW implementation with python bindings, insertions and
updates.


%prep
%setup

%build
%cmake
%cmake_build
%pyproject_build

%install
%cmakeinstall_std
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README*
%_includedir/%{nomen}*
%_cmakedir/%nomen

%files         -n python3-module-%nomen
%python3_sitelibdir/%{nomen}*.so
%python3_sitelibdir/%{nomen}*/METADATA


%changelog
* Thu Aug 28 2025 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1.1
- ! fixed build for python3 returning req.package numpy

* Fri May 16 2025 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- initial build for Sisyphus
