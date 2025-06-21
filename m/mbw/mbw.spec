%define _unpackaged_files_terminate_build 1

Name: mbw
Version: 2.0
Release: alt1

Summary: memory bandwidth benchmark program
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/raas/mbw

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
MBW determines the "copy" memory bandwidth available to userspace
programs.
Its simplistic approach models that of real applications.
It is not tuned to extremes and it is not aware of hardware 
architecture, just like your average software package.

%prep
%setup

%build
%cmake \
       -DDESTINATION=/usr
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_man1dir
install mbw.1 %buildroot%_man1dir/mbw.1

%files
%doc README
%_bindir/%name
%_man1dir/%{name}.1.*

%changelog
* Sat Jun 21 2025 Nikolay Strelkov <snk@altlinux.org> 2.0-alt1
- Initial build for Sisyphus
