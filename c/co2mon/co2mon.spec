Name:           co2mon
Version:        2.1.0
Release:        alt1
Summary:        CO2 monitor software
License:        GPLv3+
URL:            https://github.com/dmage/co2mon
Group:          Monitoring

Source:         %name-%version.tar
Patch0:         alt-udev-rules.patch

BuildPreReq:    cmake rpm-macros-cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

%description
Software for USB CO2 Monitor devices.

%package        devel
Summary:        Include files for CO2 monitor software
Group:          Monitoring
Requires:       %name = %version-%release

%description    devel
Development files for USB CO2 Monitor devices.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DBUILD_SHARED_LIBS=on
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_udevrulesdir
install -p -m 644 udevrules/99-co2mon.rules %buildroot%_udevrulesdir

%files
%doc README.md
%_bindir/co2mond
%_libdir/*.so.*
%_udevrulesdir/99-co2mon.rules

%files devel
%_libdir/*.so
%_includedir/%name.h

%changelog
* Thu Feb 15 2018 Andrew Savchenko <bircoph@altlinux.org> 2.1.0-alt1
- Import SRPM from Russian Fedora
- Use latest upstream snapshot
