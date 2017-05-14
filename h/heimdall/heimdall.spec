# SPEC file for heimdall package

Name:    heimdall
Version: 1.4.2
Release: alt1

Summary: tool suite to flash firmware onto Samsung smartphones

License: %bsdstyle
Group:   Other
URL:     https://github.com/Benjamin-Dobell/Heimdall
#URL:    http://www.glassechidna.com.au/heimdall

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun May 14 2017
# optimized out: cmake-modules gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-widgets libstdc++-devel python-base python-modules python3 python3-base
BuildRequires: cmake libusb-devel qt5-base-devel zlib-devel

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
install -m 0755 BUILD/bin/* %buildroot%_bindir/

mkdir -p -- %buildroot%_udevrulesdir
install -m 0664 %name/60-%name.rules %buildroot%_udevrulesdir/


%files
%doc README.md LICENSE Linux/README

%_bindir/%name

%_udevrulesdir/60-heimdall.rules

%files frontend
%_bindir/%name-frontend

%changelog
* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.4.2-alt1
- New version (Closes: 33468)

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt2
- New version (release 1.4.1)

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt1.rc2
- New version

* Sun Sep 09 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.2-alt1
- Initial build for ALT Linux
