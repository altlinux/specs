%define _unpackaged_files_terminate_build 1
%define short_name ueberzug

Name: ueberzugpp
Version: 2.9.6
Release: alt1

Summary: Drop in replacement for ueberzug written in C++
License: GPL-3.0
Group: Other
Url: https://github.com/jstkdng/ueberzugpp

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: libvips-devel
BuildRequires: libsixel-devel
BuildRequires: chafa-devel
BuildRequires: libssl-devel
BuildRequires: tbb-devel
BuildRequires: cli11-devel
BuildRequires: nlohmann-json-devel
BuildRequires: libfmt-devel
BuildRequires: libspdlog-devel
BuildRequires: librange-v3-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: libopencv-devel
BuildRequires: libwayland-client-devel
BuildRequires: wayland-protocols

%description
Uberzug++ is a command line utility written in C++ which allows to draw images
on terminals by using X11/wayland child windows, sixels, kitty and iterm2..

%prep
%setup

%build
%cmake \
-DENABLE_WLROOTS=ON
%cmake_build

%install
%cmakeinstall_std
rm -v %buildroot%_man1dir/ueberzug.1
ln -s %_man1dir/ueberzugpp.1 %buildroot%_man1dir/ueberzug.1

%files
%doc README.md LICENSE
%_bindir/%short_name
%_bindir/%{short_name}pp
%_man1dir/%short_name.1.*
%_man1dir/%{short_name}pp.1.*

%changelog
* Mon Jun 24 2024 Anton Kurachenko <srebrov@altlinux.org> 2.9.6-alt1
- Initial build for Sisyphus.
