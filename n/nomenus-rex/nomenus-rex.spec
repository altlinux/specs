%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: nomenus-rex
Version: 0.8.1
Release: alt1

Summary: A CLI utility for the file mass-renaming
License: GPL-3.0
Group: File tools
Url: https://github.com/ANGulchenko/nomenus-rex

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libconfig++)

%description
Nomenus-rex is a CLI utility for the file mass-renaming.

%prep
%setup

%build
%cmake
%cmake_build

%install
#%%cmake_install

# copy binary
mkdir -p %buildroot/%_bindir
cp -v %_cmake__builddir/nomenus-rex %buildroot/%_bindir/

%files
%doc CHANGELOG LICENSE README
%_bindir/nomenus-rex

%changelog
* Tue Aug 26 2025 Nikolay Strelkov <snk@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus
