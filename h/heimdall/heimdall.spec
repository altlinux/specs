# SPEC file for heimdall package

Name:    heimdall
Version: 2.2.2
Release: alt1

Summary: tool suite to flash firmware onto Samsung smartphones

License: %bsdstyle
Group:   Other
URL:     https://git.sr.ht/~grimler/Heimdall

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source:  %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Feb 12 2026
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-widgets libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base qt6-base-common sh5 vulkan-headers
BuildRequires: libusb-devel qt6-base-devel zlib-devel

%description
Heimdall is a cross-platform open-source tool suite used to flash
firmware (aka ROMs) onto Samsung Galaxy S devices and some other
Samsung smartphones.

This software attempts to flash your Galaxy S device. The very
nature of flashing is dangerous. As with all flashing software,
Heimdall has the potential to damage (brick) your phone if not
used carefully. If you're concerned, don't use this software.

%package frontend
Summary: graphic fronted to the Heimdall
Group: Other
License: %bsdstyle
Requires: %name

%description frontend
Heimdall is a cross-platform open-source tool suite used to flash
firmware (aka ROMs) onto Samsung Galaxy S devices and some other
Samsung smartphones.

This package contains graphic frontend to the Heimdall utility.


%prep
%setup
%patch0 -p1


%build
%cmake
%cmake_build

%install
mkdir -p -- %buildroot%_bindir
install -m 0755 %_cmake__builddir/bin/* %buildroot%_bindir/

mkdir -p -- %buildroot%_udevrulesdir
install -m 0664 %name/60-%name.rules %buildroot%_udevrulesdir/

%files
%doc README.md LICENSE
%doc doc/*.md

%_bindir/%name

%_udevrulesdir/60-heimdall.rules

%files frontend
%_bindir/%name-frontend

%changelog
* Thu Feb 12 2026 Nikolay A. Fetisov <naf@altlinux.org> 2.2.2-alt1
- New version
  - Build with QT6
- Update upstream URL

* Fri Mar 01 2024 Ildar Mulyukov <ildar@altlinux.ru> 2.0.2-alt1
- build from the fork: https://git.sr.ht/~grimler/Heimdall

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.4.2-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.4.2-alt1
- New version (Closes: 33468)

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt2
- New version (release 1.4.1)

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt1.rc2
- New version

* Sun Sep 09 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.2-alt1
- Initial build for ALT Linux
