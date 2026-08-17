%define        oname CCTag

Name:          cctag
Version:       1.0.4.42
Release:       alt0.2
Summary:       Detection of CCTag markers made up of concentric circles
License:       MPL-2.0
Group:         System/Libraries
Url:           https://github.com/alicevision/CCTag
Vcs:           https://github.com/alicevision/CCTag.git

Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: eigen3
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libopencv-devel


%description
Detection of CCTag markers made up of concentric circles. Implementations in
both CPU and GPU.

The library is the implementation of the paper:

* Lilian Calvet, Pierre Gurdjos, Carsten Griwodz, Simone Gasparini. Detection
  and Accurate Localization of Circular Fiducials Under Highly Challenging
  Conditions. In: Proceedings of the International Conference on Computer Vision
  and Pattern Recognition (CVPR 2016), Las Vegas, E.-U., IEEE Computer Society,
  p. 562-570, June 2016. https://doi.org/10.1109/CVPR.2016.67


%package       -n lib%{name}
Group:         System/Libraries
Summary:       %summary


%description   -n lib%{name}
Detection of CCTag markers made up of concentric circles. Implementations in
both CPU and GPU.

The library is the implementation of the paper:

* Lilian Calvet, Pierre Gurdjos, Carsten Griwodz, Simone Gasparini. Detection
  and Accurate Localization of Circular Fiducials Under Highly Challenging
  Conditions. In: Proceedings of the International Conference on Computer Vision
  and Pattern Recognition (CVPR 2016), Las Vegas, E.-U., IEEE Computer Society,
  p. 562-570, June 2016. https://doi.org/10.1109/CVPR.2016.67


%package       -n lib%{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name} = %EVR
Requires:      cmake
Requires:      gcc-c++
Requires:      eigen3
Requires:      boost-devel
Requires:      boost-program_options-devel
Requires:      boost-filesystem-devel
Requires:      libopencv-devel

%description   -n lib%{name}-devel
Detection of CCTag markers made up of concentric circles. Implementations in
both CPU and GPU.

The library is the implementation of the paper:

* Lilian Calvet, Pierre Gurdjos, Carsten Griwodz, Simone Gasparini. Detection
  and Accurate Localization of Circular Fiducials Under Highly Challenging
  Conditions. In: Proceedings of the International Conference on Computer Vision
  and Pattern Recognition (CVPR 2016), Las Vegas, E.-U., IEEE Computer Society,
  p. 562-570, June 2016. https://doi.org/10.1109/CVPR.2016.67


%prep
%setup
%autopatch -p1

%build
%cmake -DCCTAG_WITH_CUDA:BOOL=OFF \
       -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmakeinstall_std


%files
%doc README*
%_bindir/*

%files         -n lib%{name}
%_libdir/lib%{oname}*.so.*

%files         -n lib%{name}-devel
%_includedir/%{name}
%_libdir/cmake/%{oname}
%_libdir/lib%{oname}*.so


%changelog
* Mon Aug 17 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.4.42-alt0.2
- NMU: drop BR: boost-math-devel (not needed since boost 1.92.0).

* Tue Aug 04 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.4.42-alt0.1
- ^ 1.0.3 -> 1.0.4p42

* Tue Oct 21 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1.2
- FTBFS: fixed build with eigen 5.0.0.

* Sat Apr 27 2024 Ivan A. Melnikov <iv@altlinux.org> 1.0.3-alt1.1
- Fix build with boost 1.85.0

* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- initial build for Sisyphus
