%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mystran
Version: 19.0.0
Release: alt1

Summary: General purpose finite element analysis solver
License: MIT
Group: Engineering
Url: https://github.com/MystranSolver/MYSTRANSolver

Source: %name-%version.tar

Source1: submodules-%name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel

%description
MYSTRAN is a general purpose finite element analysis computer program
for structures that can be modeled as linear (i.e. displacements,
forces and stresses proportional to applied load). MYSTRAN is an
acronym for "My Structural Analysis", to indicate its usefulness in
solving a wide variety of finite element analysis problems.

%prep
%setup -a1
sed -i "s/ -march=native//g" submodules/metis/conf/gkbuild.cmake

%build
%cmake
mkdir -p include
%cmake_build

%install
%cmake_install
find %buildroot -name "*.a" -print -delete

install -Dpm755 Binaries/mystran %buildroot%_bindir/mystran

%files
%doc LICENSE.txt README.md
%_bindir/mystran
%exclude %_includedir
%exclude %_libdir

%changelog
* Sun Jul 19 2026 Nikolay Strelkov <snk@altlinux.org> 19.0.0-alt1
- Initial build for Sisyphus
