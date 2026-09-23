%define _unpackaged_files_terminate_build 1

Name:    vr-tracker-overlay
Version: 0.0.2
Release: alt1

Summary: OpenXR overlay to visualize tracked devices
License: GPL-3.0-only
Group:   Graphics
URL:     https://git.insberr.com/insberr/vr-tracker-overlay

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: openxr-devel libEGL-devel

ExcludeArch: %ix86

%description
An OpenXR overlay to visualize tracked devices. Useful for debugging or
double checking that everything is calibrated properly.

%prep
%setup -a1

%build
%cmake \
    -DSKIP_INSTALL_LIBRARIES=ON \
    -DSKIP_INSTALL_HEADERS=ON

%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Wed Sep 23 2026 Sergey Palcheh <minergenon@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
