%define rname USBqemu-wheel

Name: pcsx2-plugin-usbqemu-wheel
Version: 0.10.0
Release: alt1

Summary: PCSX2 usb plugin for wheels and increasingly more stuff
License: Unlicense
Group: Emulators

Url: https://github.com/jackun/%rname
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: %ix86

# https://github.com/jackun/%rname/archive/%version/%rname-%version.tar.gz
Source: %rname-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libXfixes-devel
BuildRequires: libgtk+2-devel
BuildRequires: libpulseaudio-devel

Requires: pcsx2

Provides: pcsx2-plugin-usb = %EVR

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%prep
%setup -n %rname-%version

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%_libdir/pcsx2 \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files
%doc README.md
%_libdir/pcsx2/lib%rname-*.so

%changelog
* Tue Aug 04 2020 Nazarov Denis <nenderus@altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Tue Jun 02 2020 Nazarov Denis <nenderus@altlinux.org> 0.9.2.0-alt1
- Version 0.9.2-0

* Mon May 25 2020 Nazarov Denis <nenderus@altlinux.org> 0.9.1.0-alt1
- Initial build for ALT Linux
