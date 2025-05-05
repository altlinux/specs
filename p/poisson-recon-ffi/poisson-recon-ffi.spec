%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    devel
%define        project_name PoissonRecon
%define        devel_name poisson-recon

Name:          poisson-recon-ffi
Version:       6.13
Release:       alt1
Summary:       Poisson Surface Reconstruction
License:       BSD-Source-beginning-file and BSD-3-Clause license
Group:         Sciences/Mathematics
Url:           https://www.cs.jhu.edu/~misha/Code/PoissonRecon/Version6.13/
Vcs:           https://github.com/bokuanT/poissonReconFFI.git
Packager:      Baltix Maintainers Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
#BuildRequires: eigen3
#BuildRequires: eigen
BuildRequires: /proc
#BuildRequires: cmake(eigen3)
#BuildRequires: zlib-devel
#BuildRequires: libpng-devel
#BuildRequires: libjpeg-devel
#BuildRequires: boost-asio-devel
#BuildRequires: libvtk-devel
#BuildRequires: libgsl-devel
BuildRequires: libgomp-devel

%description
This code-base was born from the Poisson Surface Reconstruction code. It has
evolved to support more general adaptive finite-elements systems:

* in spaces of arbitrary dimension,
* discretized using finite-elements of arbitrary degree,
* involving arbitrary function derivatives,
* with both point-wise and integrated constraints.


%package       -n lib%{devel_name}
Version:       6.13
Release:       alt1
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
Version:       6.13
Release:       alt1
Summary:       Poisson Surface Reconstruction development package
Summary(ru_RU.UTF-8): Файлы для разработки буковины poisson-recon
Group:         Development/C

%description   -n lib%{devel_name}-devel
Poisson Surface Reconstruction development package.

This code-base was born from the Poisson Surface Reconstruction code. It has
evolved to support more general adaptive finite-elements systems:

* in spaces of arbitrary dimension,
* discretized using finite-elements of arbitrary degree,
* involving arbitrary function derivatives,
* with both point-wise and integrated constraints.

%description   -n lib%{devel_name}-devel -l ru_RU.UTF-8
Файлы для разработки буковины poisson-recon.
%endif


%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

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
* Wed Apr 30 2025 Pavel Skrylev <majioa@altlinux.org> 6.13-alt1
- + packaged for Sisyphus
