%define _unpackaged_files_terminate_build 1

Name: lact
Version: 0.5.2
Release: alt1

Summary: Linux AMDGPU Control Application
License: MIT
Group: Monitoring

URL: https://github.com/ilya-zlobintsev/LACT
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 loongarch64

# Source-url: https://github.com/ilya-zlobintsev/LACT/archive/v%version/LACT-%version.tar.gz
Source0: LACT-%version.tar
# cargo vendor
Source1: crates.tar

Source2: config

BuildRequires: blueprint-compiler
BuildRequires: libdrm-devel
BuildRequires: libgtk4-devel
BuildRequires: rust-cargo

%description
This application allows you to control your AMD GPU on a Linux system.

Current features:

   - Viewing information about the GPU
   - Power/thermals monitoring
   - Fan curve control
   - Overclocking (GPU/VRAM clockspeed, voltage)
   - Power states configuration

%prep
%setup -n LACT-%version
tar xf %SOURCE1
%__mkdir_p cargo
%__cp %SOURCE2 cargo

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release --offline

%install
DESTDIR=%buildroot PREFIX=%prefix make install
%__chmod 644 %buildroot%_desktopdir/io.github.%name-linux.desktop
%__chmod 644 %buildroot%_pixmapsdir/io.github.%name-linux.png
%__mkdir_p %buildroot%_unitdir
%__mv %buildroot%prefix%_unitdir/%{name}d.service %buildroot%_unitdir
%__chmod 644 %buildroot%_unitdir/%{name}d.service

%files
%doc API.md LICENSE README.md
%_bindir/%name
%_desktopdir/io.github.%name-linux.desktop
%_pixmapsdir/io.github.%name-linux.png
%_iconsdir/hicolor/scalable/apps/io.github.%name-linux.svg
%_unitdir/%{name}d.service

%changelog
* Wed Feb 14 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Mon Nov 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.5.0-alt1.1
- NMU: build for LoongArch too

* Sat Nov 25 2023 Nazarov Denis <nenderus@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux

