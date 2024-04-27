Name: xboxdrv
Version: 0.8.8
Release: alt2.3

Summary: Xbox/Xbox360 USB Gamepad Driver for Userspace
License: GPLv3
Group: Other

Url: http://pingus.seul.org/~grumbel/%name/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://gitlab.com/%name/%name/-/archive/v%version/%name-v%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: boost-devel-headers
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: rpm-build-python
BuildRequires: scons

%description
Xboxdrv is a Xbox/Xbox360 gamepad driver for Linux that works in
userspace. It is an alternative to the xpad kernel driver and has
support for Xbox1 gamepads, Xbox360 USB gamepads and Xbox360 wireless
gamepads. The Xbox360 guitar and some Xbox1 dancemats might work too.
The Xbox 360 racing wheel is not supported, but shouldn't be to hard
to add if somebody is interested.

Some basic support for the Xbox360 Chatpad on USB controller is
provided, Chatpad on wireless ones is not supported. The headset is
not supported, but you can dump raw data from it.

This driver is only of interest if the xpad kernel driver doesn't work
for you or if you want more configurabity. If the xpad kernel driver
works for you there is no need to try this driver.

%prep
%setup -n %name-v%version
%patch0 -p1

%build
scons \
	-j%_smp_build_ncpus \
	BUILD=custom \
	CFLAGS='%optflags' \
	CXXFLAGS='%optflags' \
	PREFIX=%_prefix


%install
%makeinstall_std PREFIX=%_prefix

%files
%doc AUTHORS COPYING NEWS PROTOCOL README.md TODO examples
%_bindir/%name
%_bindir/%{name}ctl
%_man1dir/%name.1*

%changelog
* Sat Apr 27 2024 Ivan A. Melnikov <iv@altlinux.org> 0.8.8-alt2.3
- NMU: fix building with boost 1.85.0+.

* Thu Feb 08 2024 Ivan A. Melnikov <iv@altlinux.org> 0.8.8-alt2.2
- NMU: respect %%optflags when building
  (fixes build with boost 1.84.0+).

* Tue May 04 2021 Nazarov Denis <nenderus@altlinux.org> 0.8.8-alt2.1
- Update build requires to fix FTBFS

* Sat Jan 18 2020 Nazarov Denis <nenderus@altlinux.org> 0.8.8-alt2
- Fix 60 seconds delay
- Fix build with python

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.8.8-alt0.M70P.1
- Build for branch p7

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.8.8-alt0.M70T.1
- Build for branch t7

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.8.8-alt1
- Version 0.8.8

* Mon Nov 09 2015 Nazarov Denis <nenderus@altlinux.org> 0.8.6-alt0.M70P.1
- Build for branch p7

* Sun Nov 08 2015 Nazarov Denis <nenderus@altlinux.org> 0.8.6-alt0.M70T.1
- Build for branch t7

* Sat Nov 07 2015 Nazarov Denis <nenderus@altlinux.org> 0.8.6-alt1
- Version 0.8.6

* Sun May 25 2014 Nazarov Denis <nenderus@altlinux.org> 0.8.5-alt0.M70P.1
- Build for branch p7

* Thu May 22 2014 Nazarov Denis <nenderus@altlinux.org> 0.8.5-alt0.M70T.1
- Build for branch t7

* Wed May 21 2014 Nazarov Denis <nenderus@altlinux.org> 0.8.5-alt1
- Initial build for ALT Linux
