Name: capacity-tester
Version: 0.7
Release: alt0.d

Summary: Graphical tool to detect fake USB drives

License: GPL-3.0-only
Group: Other

Url: https://github.com/c0xc/CapacityTester
Vcs: https://github.com/c0xc/CapacityTester

Source: %name-%version.tar
Source1: lib-cpp-class-logger.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ qt5-base-devel
BuildRequires: libusb-devel qt5-tools-devel

%description
Use CapacityTester to check if your USB thumb/flash drive lies about
its capacity. Graphical tool to detect fake USB drives.

- Test your new USB flash drive from China to find out if its full capacity can be used or if it's fake!
- The volume test fills the filesystem, verifying that all of it can be used. It's slow, it takes hours.
- The disk test overwrites the drive itself and is much faster (some GB/TB large USB drives can be checked in less than 10 minutes); but it's somewhat experimental.

%prep
%setup -a1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm 644 res/%name.png %buildroot%_iconsdir/hicolor/512x512/apps/%name.png
install -Dm 644 res/%name.desktop %buildroot%_datadir/applications/%name.desktop

%files
%_bindir/%name
%_iconsdir/hicolor/512x512/apps/%name.png
%_datadir/applications/%name.desktop
%doc *.md LICENSE

%changelog
* Mon Dec 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7-alt0.d
- Initial build for ALT Linux.
