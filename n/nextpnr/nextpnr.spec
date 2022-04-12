# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_enable GUI

Name:     nextpnr
Version:  0.3
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
#BuildRequires: python3-module-pytrellis
# check
BuildRequires: ctest

%{?_enable_GUI:BuildRequires: qt5-base-devel}

%description
nextpnr aims to be a vendor neutral, timing driven, FOSS FPGA place and
route tool.

%prep
%setup

%build
%cmake  -DARCH=gowin \
	%{?_enable_GUI:-DBUILD_GUI=ON -DGOWIN_BBA_EXECUTABLE=%_bindir/gowin_bba} \
	-DBUILD_TESTS=ON \
	-DBUILD_PYTHON=ON \
	-DSTATIC_BUILD=OFF

%cmake_build

%install
%cmake_install

%check
%make_build -C %_cmake__builddir test

%files
%_bindir/nextpnr-gowin
%doc *.md docs/*

%changelog
* Tue Apr 12 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- new version (0.3) with rpmgs script
- enable GUI
- enable check
- ExcludeArch: %arm

* Wed Apr 06 2022 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
