Name: softgun
Version: 0.22
Release: alt3

Summary: ARM Board Emulator
License: GPL
Group: Emulators

Url: http://softgun.sourceforge.net/
Source: %name-%version.tgz
Patch: softgun-0.22-alt-DSO.patch
Patch1: softgun-0.22-alt-GCC10.patch

# Automatically added by buildreq on Sun Jul 29 2012
BuildRequires: libalsa-devel zlib-devel

BuildRequires: zlib-devel

%description
Emulates three ARM9-based development boards and a wide range of peripherals.

%prep
%setup
%patch -p1
%patch1 -p1
%ifarch %e2k
sed -i 's,-O9,-O%_optlevel,g' config.mk testapps/Makefile
%endif

%build
%make_build bindir=%_bindir libdir=%_libdir/%name LDLIBS+="-ldl -lm"

%install
mkdir -p %buildroot%_bindir
make install bindir=%buildroot%_bindir libdir=%buildroot%_libdir/%name

%files
%doc README configs
%_bindir/*
%_libdir/%name

%changelog
* Sun Jan 31 2021 Fr. Br. George <george@altlinux.ru> 0.22-alt3
- Fix GCC10 build

* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 0.22-alt2
- E2K: fix superfluous optimization level
- Add Url:
- Minor spec cleanup

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 0.22-alt1
- Autobuild version bump to 0.22
- Fix patch

* Wed Nov 14 2012 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Autobuild version bump to 0.21
- Add DSO patch

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
- Remove inactual patches

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 0.16-alt1
Initial build from ancient SuSE

* Fri Nov 28 2008 - uli@suse.de
- fixed rpmlint complaint
* Fri Jun 13 2008 - uli@suse.de
- fixed to build with new toolchain
