%define _unpackaged_files_terminate_build 1

Name: apt-query
Version: 0.1.0
Release: alt1

Summary: a cli tool for inspecting apt repositories
License: GPLv2+
Group: System/Configuration/Packaging
URL: https://altlinux.space/alterator/apt-cache

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libapt-devel librange-v3-devel

%description
apt-query is designed to work with both local and remote repositories,
never modifying the main apt cache.
It allows listing the contents of one or more repositories,
as well as getting various information about different package versions.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/apt-query

%changelog
* Tue Jun 30 2026 Andrey Alekseev <parovoz@altlinux.org> 0.1.0-alt1
- Initial build.
