Name: picoc
Version: 2.1
Release: alt1

Summary: PicoC is a very small C interpreter for scripting

License: New BSD License
Group: Development/C
Url: http://code.google.com/p/picoc/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://picoc.googlecode.com/files//%name-%version.tar

# Automatically added by buildreq on Fri Oct 25 2013
BuildRequires: libreadline-devel

%description
PicoC is a very small C interpreter for scripting.
It was originally written as the script language
for a UAV's on-board flight system.
It's also very suitable for other robotic, embedded and non-embedded applications.

The core C source code is around 4500 lines of code.
It's not intended to be a complete implementation of ISO C
but it has all the essentials. When compiled it only takes a few k of code space
and is also very sparing of data space.
This means it can work well in small embedded devices.
It's also a fun example of how to create a very small language implementation
while still keeping the code readable.

picoc has been tested on x86-32, x86-64, powerpc, arm,
ultrasparc, HP-PA and blackfin processors and is easy to port to new targets.

%prep
%setup

%build
%make_build

%install
install -D %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/%name

%changelog
* Fri Oct 25 2013 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- initial build for ALT Linux Sisyphus

