%define _unpackaged_files_terminate_build 1

%define pypi_name itree

Name: python3-module-%pypi_name
Version: 0.0.21
Release: alt1

Summary: An Interval Tree Library
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/juncongmoo/itree

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(zlib)

%description
In computer science, an interval tree is a tree data structure to hold
intervals. Every node in itree has a start and an end value.

%prep
%setup -n %pypi_name-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.md
%python3_sitelibdir/_%{pypi_name}*
%python3_sitelibdir/%pypi_name/
%exclude %python3_sitelibdir/tests
%dir %python3_sitelibdir/py_%{pypi_name}*info/
%python3_sitelibdir/py_%{pypi_name}*info/*

%changelog
* Sun Mar 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.21-alt1
- Initial build for Sisyphus
