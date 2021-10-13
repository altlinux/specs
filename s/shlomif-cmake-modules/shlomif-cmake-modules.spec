%define _unpackaged_files_terminate_build 1

Name: shlomif-cmake-modules
Version: 0
Release: alt1.git.7525914

Summary: CMake modules which are used across Shlomi Fishs projects
License: MIT
Group: Development/Other
Url: https://github.com/shlomif/shlomif-cmake-modules

Source: %name-%version.tar 
BuildArch: noarch

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/cmake/Modules
cp %name/Shlomif_Common.cmake %buildroot%_datadir/cmake/Modules/

%files
%_datadir/cmake/Modules/*.cmake
%doc LICENSE README.md

%changelog
* Tue Oct 12 2021 Konstantin Rybakov <kastet@altlinux.org> 0-alt1.git.7525914
- Updated from upstream git

* Mon Feb 10 2020 Konstantin Rybakov <kastet@altlinux.org> 0-alt1.git.89f05ca
- Initial build for ALT.


