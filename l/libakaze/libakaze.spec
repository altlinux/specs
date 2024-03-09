%define        _unpackaged_files_terminate_build 1
%define        cname AKAZE
%define        oname akaze

Name:          lib%{oname}
Version:       0.1.1
Release:       alt1
Summary:       Accelerated-KAZE Features
License:       BSD-3-Clause
Group:         System/Libraries
Url:           http://www.robesafe.com/personal/pablo.alcantarilla/kaze.html
Vcs:           https://github.com/pablofdezalc/akaze.git

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libtbb-devel
BuildRequires: libgomp-devel
BuildRequires: libopencv-devel

%description
KAZE Features is a novel 2D feature detection and description method that
operates completely in a nonlinear scale space. Previous methods such as SIFT or
SURF find features in the Gaussian scale space (particular instance of linear
diffusion). However, Gaussian blurring does not respect the natural boundaries
of objects and smoothes in the same degree details and noise when evolving the
original image through the scale space.

By means of nonlinear diffusion we can detect and describe features in nonlinear
scale spaces keeping important image details and removing noise as long as we
evolve the image in the scale space. We use variable conductance diffusion
which is one of the simplest cases of nonlinear diffusion. The nonlinear scale
space is build efficiently by means of Additive Operator Splitting (AOS)
schemes, which are stable for any step size and are parallelizable.

Accelerated-KAZE Features uses a novel mathematical framework called Fast
Explicit Diffusion (FED) embedded in a pyramidal framework to speed-up
dramatically the nonlinear scale space computation. In addition, we compute a
robust Modified-Local Difference Binary (M-LDB) descriptor that exploits
gradient information from the nonlinear scale space. A-KAZE obtains comparable
results to KAZE in some datasets, while being several orders of magnitude
faster.

Our results reveal a big improvement in repeatability and distinctiviness, for
common 2D image matching applications.


%package       -n %oname
Summary:       Accelerated-KAZE Features executables
Group:         Development/Other
Requires:      %name = %version-%release

%description   -n %oname
Accelerated-KAZE Features executables.

KAZE Features is a novel 2D feature detection and description method that
operates completely in a nonlinear scale space. Previous methods such as SIFT or
SURF find features in the Gaussian scale space (particular instance of linear
diffusion). However, Gaussian blurring does not respect the natural boundaries
of objects and smoothes in the same degree details and noise when evolving the
original image through the scale space.

By means of nonlinear diffusion we can detect and describe features in nonlinear
scale spaces keeping important image details and removing noise as long as we
evolve the image in the scale space. We use variable conductance diffusion
which is one of the simplest cases of nonlinear diffusion. The nonlinear scale
space is build efficiently by means of Additive Operator Splitting (AOS)
schemes, which are stable for any step size and are parallelizable.

Accelerated-KAZE Features uses a novel mathematical framework called Fast
Explicit Diffusion (FED) embedded in a pyramidal framework to speed-up
dramatically the nonlinear scale space computation. In addition, we compute a
robust Modified-Local Difference Binary (M-LDB) descriptor that exploits
gradient information from the nonlinear scale space. A-KAZE obtains comparable
results to KAZE in some datasets, while being several orders of magnitude
faster.

Our results reveal a big improvement in repeatability and distinctiviness, for
common 2D image matching applications.


%package       -n %name-devel
Summary:       Accelerated-KAZE Features library development files
Group:         Development/Other
Requires:      %name = %version-%release

Requires:      cmake
Requires:      gcc-c++
Requires:      doxygen
Requires:      graphviz
Requires:      libtbb-devel
Requires:      libgomp-devel
Requires:      libopencv-devel

%description   -n %name-devel
Accelerated-KAZE Features library development files.

KAZE Features is a novel 2D feature detection and description method that
operates completely in a nonlinear scale space. Previous methods such as SIFT or
SURF find features in the Gaussian scale space (particular instance of linear
diffusion). However, Gaussian blurring does not respect the natural boundaries
of objects and smoothes in the same degree details and noise when evolving the
original image through the scale space.

By means of nonlinear diffusion we can detect and describe features in nonlinear
scale spaces keeping important image details and removing noise as long as we
evolve the image in the scale space. We use variable conductance diffusion
which is one of the simplest cases of nonlinear diffusion. The nonlinear scale
space is build efficiently by means of Additive Operator Splitting (AOS)
schemes, which are stable for any step size and are parallelizable.

Accelerated-KAZE Features uses a novel mathematical framework called Fast
Explicit Diffusion (FED) embedded in a pyramidal framework to speed-up
dramatically the nonlinear scale space computation. In addition, we compute a
robust Modified-Local Difference Binary (M-LDB) descriptor that exploits
gradient information from the nonlinear scale space. A-KAZE obtains comparable
results to KAZE in some datasets, while being several orders of magnitude
faster.

Our results reveal a big improvement in repeatability and distinctiviness, for
common 2D image matching applications.


%package       -n %name-devel-static
Summary:       Accelerated-KAZE Features library development files
Group:         Development/Other
Requires:      %name = %version-%release

Requires:      %name-devel = %EVR

%description   -n %name-devel-static
Accelerated-KAZE Features library development static files.

KAZE Features is a novel 2D feature detection and description method that
operates completely in a nonlinear scale space. Previous methods such as SIFT or
SURF find features in the Gaussian scale space (particular instance of linear
diffusion). However, Gaussian blurring does not respect the natural boundaries
of objects and smoothes in the same degree details and noise when evolving the
original image through the scale space.

By means of nonlinear diffusion we can detect and describe features in nonlinear
scale spaces keeping important image details and removing noise as long as we
evolve the image in the scale space. We use variable conductance diffusion
which is one of the simplest cases of nonlinear diffusion. The nonlinear scale
space is build efficiently by means of Additive Operator Splitting (AOS)
schemes, which are stable for any step size and are parallelizable.

Accelerated-KAZE Features uses a novel mathematical framework called Fast
Explicit Diffusion (FED) embedded in a pyramidal framework to speed-up
dramatically the nonlinear scale space computation. In addition, we compute a
robust Modified-Local Difference Binary (M-LDB) descriptor that exploits
gradient information from the nonlinear scale space. A-KAZE obtains comparable
results to KAZE in some datasets, while being several orders of magnitude
faster.

Our results reveal a big improvement in repeatability and distinctiviness, for
common 2D image matching applications.


%prep
%setup
%autopatch -p1

%build
%cmake_insource
%cmake_build

%install
%cmakeinstall_std

%files
%doc *.md LICENSE CHANGES
%_libdir/lib%{oname}*.so.*


%files         -n %oname
%doc *.md LICENSE CHANGES
%_bindir/%{oname}_*

%files         -n %name-devel
%doc *.md LICENSE CHANGES
%_libdir/lib%{oname}*.so
%_includedir/%oname/
%_cmakedir/%{cname}
%_datadir/cmake/Modules/%{oname}*.cmake

%files         -n %name-devel-static
%doc *.md LICENSE CHANGES
%_libdir/lib%{oname}*.a

%changelog
* Thu Mar 07 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- Initial build v0.1.1 for Sisyphus
