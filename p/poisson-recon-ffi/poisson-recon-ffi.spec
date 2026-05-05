%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    devel
%define        project_name PoissonRecon
%define        devel_name poisson-recon

Name:          %{devel_name}-ffi
Version:       6.13.1
Release:       alt0.2
Summary:       Poisson Surface Reconstruction
License:       BSD-Source-beginning-file and BSD-3-Clause license
Group:         Sciences/Mathematics
Url:           https://www.cs.jhu.edu/~misha/Code/PoissonRecon/Version6.13/
Vcs:           https://github.com/bokuanT/poissonReconFFI.git
Packager:      Baltix Maintainers Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: /proc
BuildRequires: libgomp-devel

%description
This code-base was born from the Poisson Surface Reconstruction code. It has
evolved to support more general adaptive finite-elements systems:

* in spaces of arbitrary dimension,
* discretized using finite-elements of arbitrary degree,
* involving arbitrary function derivatives,
* with both point-wise and integrated constraints.


%package       -n lib%{devel_name}
Version:       6.13.1
Release:       alt0.2
Summary:       Poisson Surface Reconstruction development package
Summary(ru_RU.UTF-8): Файлы для разработки буковины poisson-recon
Group:         Development/C

%description   -n lib%{devel_name}
Poisson Surface Reconstruction development package.

This code-base was born from the Poisson Surface Reconstruction code. It has
evolved to support more general adaptive finite-elements systems:

* in spaces of arbitrary dimension,
* discretized using finite-elements of arbitrary degree,
* involving arbitrary function derivatives,
* with both point-wise and integrated constraints.

%description   -n lib%{devel_name} -l ru_RU.UTF-8
Файлы для разработки буковины poisson-recon.


%if_enabled    devel
%package       -n lib%{devel_name}-devel
Version:       6.13.1
Release:       alt0.2
Summary:       Poisson Surface Reconstruction library development package
Summary(ru_RU.UTF-8): Файлы для разработки буковины poisson-recon
Group:         Development/C

%description   -n lib%{devel_name}-devel
Poisson Surface Reconstruction library development package.

This code-base was born from the Poisson Surface Reconstruction code. It has
evolved to support more general adaptive finite-elements systems:

* in spaces of arbitrary dimension,
* discretized using finite-elements of arbitrary degree,
* involving arbitrary function derivatives,
* with both point-wise and integrated constraints.

%description   -n lib%{devel_name}-devel -l ru_RU.UTF-8
Файлы для разработки буковины poisson-recon.


%package       -n %{name}-devel
Version:       6.13.1
Release:       alt0.2
Summary:       Poisson Surface Reconstruction core development package
Summary(ru_RU.UTF-8): Файлы для разработки пакета poisson-recon
Group:         Development/C

Requires:      cmake
Requires:      ctest
Requires:      gcc-c++
Requires:      libgomp-devel

%description   -n %{name}-devel
Poisson Surface Reconstruction core development package.

This code-base was born from the Poisson Surface Reconstruction code. It has
evolved to support more general adaptive finite-elements systems:

* in spaces of arbitrary dimension,
* discretized using finite-elements of arbitrary degree,
* involving arbitrary function derivatives,
* with both point-wise and integrated constraints.

%description   -n %{name}-devel -l ru_RU.UTF-8
Файлы для разработки пакета poisson-recon.
%endif


%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc license.txt Readme.md
%_bindir/%{devel_name}

%files         -n lib%{devel_name}
%doc license.txt Readme.md
%_libdir/lib%{devel_name}.*so.*

%if_enabled    devel
%files         -n lib%{devel_name}-devel
%doc license.txt Readme.md
%_includedir/%{devel_name}
%_cmakedir/%{project_name}/*
%_libdir/lib%{devel_name}*.*so
%endif


%changelog
* Tue May 05 2026 Pavel Skrylev <majioa@altlinux.org> 6.13.1-alt0.2
- !NBTFS:
 + build in c++ template for SparseMatrix and Octree codes with if clauses
 + code for Ply header

* Wed May 07 2025 Pavel Skrylev <majioa@altlinux.org> 6.13-alt2
- ! [NMU] fixed poisson-recon lib config variables settings
- ! [NMU] fixed deps in spec

* Wed Apr 30 2025 Pavel Skrylev <majioa@altlinux.org> 6.13-alt1
- + packaged for Sisyphus
