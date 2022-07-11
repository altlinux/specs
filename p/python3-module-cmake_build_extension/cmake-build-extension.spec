Name: python3-module-cmake_build_extension
Version: 0.5.1
Release: alt1
Summary: Setuptools extension to build and package CMake projects
Url: https://pypi.org/project/cmake-build-extension
Group: Development/Python3
Source: cmake-build-extension-%version.tar.gz
License: MIT
BuildArch: noarch

# Automatically added by buildreq on Mon Jul 11 2022
# optimized out: git-core libgpg-error mercurial python3 python3-base python3-dev python3-module-packaging python3-module-pep517 python3-module-pkg_resources python3-module-pyparsing python3-module-setuptools python3-module-tomli sh4 xz
BuildRequires: python3-module-build python3-module-setuptools_scm python3-module-wheel pip

%description
This projects aims to simplify the integration of C++ projects based on
CMake with Python packaging tools. CMake provides out-of-the-box support
to either SWIG and pybind11, that are two among the most used projects
to create Python bindings from C++ source

%prep
%setup -n cmake-build-extension-%version

%build
python3 -m build -n -w

%install
pip install --no-deps --root %buildroot dist/cmake_build_extension-%version-py3-none-any.whl

%files
%python3_sitelibdir_noarch/*

%changelog
* Mon Jul 11 2022 Fr. Br. George <george@altlinux.org> 0.5.1-alt1
- Autobuild version bump to 0.5.1

* Mon Jul 11 2022 Fr. Br. George <george@altlinux.org> 0.5.0-alt1
- Initial build for ALT
