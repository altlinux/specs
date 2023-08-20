# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qtilitools
Version: 0.1.1
Release: alt1.20230810

Summary: Scripts/commands used in the Qtilities organization
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/qtilities/picom-conf
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/qtls-translate
%_datadir/cmake/%name
%doc COPYING README.md

%changelog
* Sun Aug 20 2023 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1.20230810
- initial build
