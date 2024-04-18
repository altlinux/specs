%define  modulename mapbox-earcut

Name:    python3-module-%modulename
Version: 1.0.1
Release: alt1

Summary: Python bindings to the mapbox earcut C++ library
License: ISC AND BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/skogler/mapbox_earcut_python

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pybind11
BuildRequires: gcc-c++
#BuildRequires: cmake

# Source-url: https://github.com/skogler/mapbox_earcut_python/releases/download/v%version/mapbox_earcut-%version.tar.gz
Source:  %modulename-%version.tar

%description
%summary.

%prep
%setup -n %modulename-%version

%build
# https://github.com/mapbox/earcut.hpp/issues/97
# https://github.com/mapbox/earcut.hpp/issues/103
%add_optflags -ffp-contract=off

%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/mapbox_earcut.cpython-3*.so
%python3_sitelibdir/mapbox_earcut-%version.dist-info
%doc LICENSE.md README.md

%changelog
* Thu Apr 18 2024 Anton Midyukov <antohami@altlinux.org> 1.0.1-alt1
- Initial build
