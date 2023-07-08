%define        oname opengv

Name:          lib%{oname}
Version:       0.0.1
Release:       alt0.1
Summary:       OpenGV is a collection of computer vision methods for solving geometric vision problems
License:       NCSA
Group:         System/Libraries
Url:           http://laurentkneip.github.io/opengv/
Vcs:           https://github.com/laurentkneip/opengv.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: eigen3
BuildRequires: gcc-c++
BuildRequires: boost-devel
%add_optflags -g0

%description
OpenGV is a collection of computer vision methods for solving geometric vision
problems. It is hosted and maintained by the Mobile Perception Lab of
ShanghaiTech.

These versions have been added around March 2016, so please be aware that later
additions may not be included in this distribution. You can go immediately to
Use under Matlab to receive further instructions on the Matlab interface.

The OpenGV library aims at unifying geometric computer vision algorithms for
calibrated camera pose computation within a single efficient C++-library. OpenGV
stands for Open Geometric Vision. It contains classical central and more recent
non-central absolute and relative camera pose computation algorithms, as well as
triangulation and point-cloud alignment functionalities, all extended by
non-linear optimization and RANSAC contexts. It contains a flexible
C++-interface as well as Matlab and Python wrappers, and eases the comparison of
different geometric vision algorithms. A benchmark to compare the various
solutions for one particular problem against each other is included in the
Matlab stuff.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      %name = %EVR
Requires:      cmake
Requires:      eigen3
Requires:      gcc-c++
Requires:      boost-devel

%description   devel
%summary.


%prep
%setup
%patch

%build
%cmake -DBUILD_PYTHON:BOOL=OFF \
       -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmakeinstall_std
%find_lang %name


%files         -f %name.lang
%doc README*
%_libdir/%{name}*.so.*

%files         devel
%_libdir/%{name}*.so
%_includedir/%{oname}
%_libexecdir/cmake/%{oname}-1.0


%changelog
* Tue Aug 4 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt0.1
- initial build for Sisyphus
