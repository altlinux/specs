%define _unpackaged_files_terminate_build 1

Name: zutty
Version: 0.14
Release: alt1

Summary: A high-end terminal for low-end systems
License: GPLv3+
Group: Terminals
Url: https://tomscii.sig7.se/zutty/
Vcs: https://github.com/tomscii/zutty

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: freetype2-devel
BuildRequires: libglvnd-devel
BuildRequires: libXmu-devel
BuildRequires: python3

%description
An X terminal emulator rendering through OpenGL ES Compute Shaders. It focuses
on low-latency rendering and compatibility with commonly found terminal
protocols.

%prep
%setup

%build
export CFLAGS="%optflags"
export CXXFLAGS="${CFLAGS}"
./waf configure --prefix=%_prefix --bindir=%_bindir
./waf -j %__nprocs

%install
./waf install --destdir=%buildroot

%files
%doc LICENSE README.org doc/*.org
%_bindir/zutty

%changelog
* Mon Mar 13 2023 Anton Golubev <golubevan@altlinux.org> 0.14-alt1
- bugfixes & improvements

* Mon Jan 23 2023 Anton Golubev <golubevan@altlinux.org> 0.13-alt1
- Initial build.
