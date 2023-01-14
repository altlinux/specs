# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_enable GUI
%def_enable OPENMP

Name:     nextpnr
Version:  0.5
Release:  alt1

Summary:  portable FPGA place and route tool
License:  ISC
Group:    Engineering
Url:      https://github.com/YosysHQ/nextpnr

# Source-url: %url/archive/refs/tags/%name-%version.tar.gz
Source: %name-%version.tar

ExcludeArch: %arm

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: eigen3
# gowin
BuildRequires: python3-module-apycula
# # machxo2, ecp5
#BuildRequires: trellis-devel
# check
BuildRequires: ctest

%{?_enable_GUI:BuildRequires: qt5-base-devel}
%{?_enable_OPENMP:BuildRequires: libgomp-devel}

%description
nextpnr aims to be a vendor neutral, timing driven, FOSS FPGA place and
route tool.

%prep
%setup

%build
%cmake \
	-DCURRENT_GIT_VERSION=%version \
	-DARCH=gowin \
	-DGOWIN_BBA_EXECUTABLE=%_bindir/gowin_bba \
	-DBUILD_TESTS=ON \
	-DSTATIC_BUILD=OFF \
	%{?_enable_OPENMP:-DUSE_OPENMP=ON} \
	%{?_enable_GUI:-DBUILD_GUI=ON}

%cmake_build

%install
%cmake_install

%check
%make_build -C %_cmake__builddir test

%files
%_bindir/nextpnr-gowin
%doc *.md docs/*

%changelog
* Sat Jan 14 2023 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- new version (0.5) with rpmgs script

* Fri Oct 07 2022 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- new version (0.4) with rpmgs script

* Sat Apr 30 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt2
- fix show version (Closes: 42644)
- enable OPENMP

* Tue Apr 12 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- new version (0.3) with rpmgs script
- enable GUI
- enable check
- ExcludeArch: %arm

* Wed Apr 06 2022 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
