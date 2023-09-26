%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define _cmake__builddir BUILD

Name: cleaver
Version: 2.4
Release: alt1

Group: Development/Tools
Summary: Cleaver is an open-source multi-material tetrahedral meshing tool
License: MIT
Url: https://www.sci.utah.edu/cibc-software/cleaver.html
VCS: https://github.com/SCIInstitute/Cleaver.git

Source: %name-%version.tar

Patch1: %name-%version-alt.patch
Patch2: %name-%version-googletest.patch

BuildRequires: cmake
BuildRequires: rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libgmock-devel
BuildRequires: libgtest-devel

%define _description \
Cleaver creates conforming tetrahedral meshes for multimaterial or multiphase volumetric data using the Lattice Cleaving algorithm. \
\
The software was initially developed by the NIH Center for \
Integrative Biomedical Computing at the University of Utah \
Scientific Computing and Imaging (SCI) Institute.

%description
%_description

%package devel
Summary: Development files for Cleaver
Group: Development/C

%description devel
This package contains Cleaver development files.
%_description

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD:STRING=17 \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DUSE_ITK:BOOL=OFF \
  -DBUILD_CLI:BOOL=OFF \
  -DBUILD_GUI:BOOL=OFF \
  -DBUILD_TESTING:BOOL=ON \
  -S %_builddir/%name-%version/src \
  -B %_cmake__builddir \
  %nil

%ninja_build -C %_cmake__builddir

%install
mkdir -p %buildroot%_libdir/
install -m644 %_cmake__builddir/lib/lib%name.a %buildroot%_libdir/

%check
%ninja_build -C %_cmake__builddir test/all

%files devel
%doc README.md
%doc LICENSE
%_libdir/lib%name.a


%changelog
* Tue May 30 2023 Elizaveta Morozova <morozovaes@altlinux.org> 2.4-alt1
- Initial build for ALT
- Built using bundled Teem to avoid circular dependency with ITK.

