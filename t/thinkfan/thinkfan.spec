Name: thinkfan
Version: 0.9.1
Release: alt1
Group: System/Configuration/Hardware
License: GPL3+

Url: http://sourceforge.net/projects/thinkfan/
Packager: Evgenii Terechkov <evg@altlinux.org>
Source: %name-%version.tar
Patch0:%name-%version-alt.patch

BuildRequires: cmake gcc-c++ libatasmart-devel

Summary: simple and lightweight fan control program

%description
Thinkfan is a simple, lightweight fan control program. Originally designed
specifically for IBM/Lenovo Thinkpads, it now supports any kind of system via
the sysfs hwmon interface (/sys/class/hwmon). It is designed to eat as little
CPU power as possible.

%prep
%setup -n %name-%version
%patch0 -p1

%build
pushd src
CFLAGS="%optflags" \
%cmake_insource \
                -D USE_ATASMART:BOOL=ON \
                -D CMAKE_BUILD_TYPE:STRING=Debug \
  ..

%make_build
popd

%install
install -p -D -m 755 src/%name %buildroot%_sbindir/%name
install -p -D -m 644 src/%name.1 %buildroot%_man1dir/%name.1
install -p -D -m 644 rcscripts/%name.service %buildroot/%_unitdir/%name.service

%files
%_sbindir/%name
%_unitdir/%name.service
%_man1dir/%name.1.*
%doc NEWS README examples/*

%changelog
* Sun Sep 14 2014 Terechkov Evgenii <evg@altlinux.org> 0.9.1-alt1
- Initial build for ALT Linux Sisyphus
