%define        _unpackaged_files_terminate_build 1
%define        oname amgcl

Name:          %oname-devel
Version:       1.4.4
Release:       alt1
Summary:       C++ library for solving large sparse linear systems with algebraic multigrid method
License:       MIT
Group:         Sciences/Mathematics
Url:           https://amgcl.readthedocs.io
Vcs:           https://github.com/ddemidov/amgcl.git

Source:        %name-%version.tar
BuildArch:     noarch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
AMGCL is a header-only C++ library for solving large sparse linear systems with
algebraic multigrid (AMG) method. AMG is one of the most effective iterative
methods for solution of equation systems arising, for example, from discretizing
PDEs on unstructured grids. The method can be used as a black-box solver for
various computational problems, since it does not require any information about
the underlying geometry. AMG is often used not as a standalone solver but as a
preconditioner within an iterative solver (e.g. Conjugate Gradients, BiCGStab,
or GMRES).

AMGCL builds the AMG hierarchy on a CPU and then transfers it to one of the
provided backends. This allows for transparent acceleration of the solution
phase with help of OpenCL, CUDA, or OpenMP technologies. Users may provide their
own backends which enables tight integration between AMGCL and the user code.


%prep
%setup

%build
%cmake

%cmake_build

%install
%cmakeinstall_std

%files
%doc README*
%_includedir/%{oname}*
%_datadir/%oname


%changelog
* Sun Nov 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1
- initial build for Sisyphus
