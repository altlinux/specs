Name:          vlfeat
Version:       0.9.21
Release:       alt1.1
Summary:       VLFeat is a cross-platform open source collection of vision algorithms
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://www.vlfeat.org
Vcs:           git://github.com/vlfeat/vlfeat.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Source1:       CMakeLists.txt
Source2:       FindVLFeat.cmake
Patch:         patch.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: octave-devel
BuildRequires: libgomp-devel

%description
VLFeat is a cross-platform open source collection of vision algorithms
with a special focus on visual features (for instance SIFT and MSER) and
clustering (k-means, hierarchical k-means, agglomerative information
bottleneck). It bundles a MATLAB toolbox, a clean and portable C library and a
number of command line utilities. Thus it is possible to use the same algorithm
both from MATLAB, the command line, and your own programs.


%package       -n lib%{name}
Group:         System/Libraries
Summary:       Library code for %name

%description   -n lib%{name}
%summary.


%package       -n lib%{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name} = %EVR

%description   -n lib%{name}-devel
%summary.


%prep
%setup
%patch
cp %SOURCE1 CMakeLists.txt
%ifarch %e2k
# must be another LCC
sed -i "s/defined(__LCC__)/0/" vl/host.h
# LCC cannot work with expressions inside openmp pragmas
sed -i -E ":a;/\\\\$/{N;ba};\
/^[[:space:]]*#pragma omp .*[[:space:]](num_threads|if)\(/{s/#/for(long &/;\
s/(#.*num_threads\()([^()]*(\(\))*)\)/_xxxn=\\2,\\1_xxxn)/;\
s/(#.*if\()([^()]*)\)/_xxxi=\\2,\\1_xxxi)/;\
s/#/_xxxc=1;_xxxc;_xxxc=0)\n&/}" vl/*.c
# -fopenmp also needs to be specified for linking
sed -i "/add_definitions(-fopenmp)/a add_link_options(-fopenmp)" CMakeLists.txt
%endif

%build
%cmake
%cmake_build -j1

%install
%cmakeinstall_std
install -Dm644 %SOURCE2 %buildroot%_datadir/cmake/Modules/FindVLFeat.cmake

%files
%doc README*
%_bindir/*
%_mandir/man1/*
%_mandir/man7/*

%files         -n lib%{name}
%doc README*
%_libdir/lib%{name}*.so.*

%files         -n lib%{name}-devel
%_includedir/vl
%_libdir/lib%{name}.so
%_datadir/cmake/Modules/*.cmake

%changelog
* Wed Aug 23 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.9.21-alt1.1
- Fixed build for Elbrus

* Wed Aug 26 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.21-alt1
- initial build for Sisyphus
