Name: softgun
License: GPL
Group: Emulators
Version: 0.20
Release: alt1
Summary: ARM Board Emulator
Source: %name-%version.tgz
# Automatically added by buildreq on Sun Jul 29 2012
BuildRequires: libalsa-devel zlib-devel

BuildRequires: zlib-devel

%description
Emulates three ARM9-based development boards and a wide range of peripherals.

%prep
%setup

%build
%make_build bindir=%_bindir libdir=%_libdir/%name

%install
mkdir -p %buildroot%_bindir
make install bindir=%buildroot%_bindir libdir=%buildroot%_libdir/%name

%files
%doc README configs
%_bindir/*
%_libdir/%name

%changelog
* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
- Remove inactual patches

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 0.16-alt1
Initial build from ancient SuSE

* Fri Nov 28 2008 - uli@suse.de
- fixed rpmlint complaint
* Fri Jun 13 2008 - uli@suse.de
- fixed to build with new toolchain
