%define _unpackaged_files_terminate_build 1

Name: his
# Due to upstream doesn't make tags we need to pull version
#based on main.cpp version discovery
Version: 0.0.1
Release: alt1
Summary: A command history utility with icons and colors.
License:  GPL-3.0
Group: Terminals
Url: https://github.com/terroo/his

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: libncurses-devel
BuildRequires: libncursesw-devel
BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: clang

%description
%summary

%prep
%setup 
%autopatch -p1

%build
export CFLAGS="%optflags"
%cmake \
   -DCMAKE_C_COMPILER=clang \
   -DCMAKE_CXX_COMPILER=clang++
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Sat Sep 06 2025 Pavel Shilov <zerospirit@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.
