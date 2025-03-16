%define _unpackaged_files_terminate_build 1

%define pypi_name hiq

Name: python3-module-%pypi_name
Version: 1.1.8
Release: alt1

Summary: HiQ - Observability And Optimization In Modern AI Era
License: UPL
Group: Development/Python3
URL: https://github.com/oracle/hiq

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%filter_from_requires /python3(oci)/d
%filter_from_requires /python3(py_zipkin)/d
%filter_from_requires /python3(py_zipkin.zipkin)/d

BuildArch: noarch

Source: %pypi_name-%version.tar

Patch: %name-%version-%release.patch

%description
HiQ is a declarative, non-intrusive, dynamic and transparent tracking
system for both monolithic application and distributed system. It brings
the runtime information tracking and optimization to a new level without
compromising with speed and system performance, or hiding any tracking
overhead information. HiQ applies for both I/O bound and CPU bound
applications. In addition to latency tracking, HiQ provides memory, disk
I/O and Network I/O tracking out of the box. The output can be saved in
form of normal line by line log file, or HiQ tree, or span graph.

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
cd hiq
%python3_build

%install
cd hiq
%python3_install

%files
%doc CONTRIBUTING.md LICENSE.txt README.md SECURITY.md
%python3_sitelibdir/%pypi_name/
%dir %python3_sitelibdir/%{pypi_name}_*-info/
%python3_sitelibdir/%{pypi_name}_*-info/*

%changelog
* Sun Mar 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.8-alt1
- Initial build for Sisyphus
