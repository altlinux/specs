Name: gfs2-utils
Version: 3.5.1
Release: alt1
License: GPL-2.0+ and LGPL-2.0+
Group: System/Kernel and hardware
Summary: Utilities for managing the global file system (GFS2)
URL: https://pagure.io/gfs2-utils

Source0: https://releases.pagure.org/gfs2-utils/gfs2-utils-%{version}.tar.gz
Patch0: gfs2-utils-alt-dmsetup.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: flex
BuildRequires: libblkid-devel
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: libuuid-devel

%description
The gfs2-utils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in GFS2
file systems.

%prep
%setup
%patch0 -p2
# Set correct python3 executable in shebang                                                                           
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)

%build
%autoreconf
%configure --with-udevdir=%_udevdir
%make_build

%check
%make check

%install
%make -C gfs2 DESTDIR=%buildroot install

%files
%doc doc/*.txt doc/README.contributing doc/README.licence doc/README.tests
%_udevrulesdir/82-gfs2-withdraw.rules
%_sbindir/*
%_libexecdir/gfs2_withdraw_helper
%_man8dir/*.8*
%_man5dir/*.5*

%changelog
* Fri Aug 02 2024 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version.

* Wed Feb 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 3.1.9-alt1
- new upstream release

* Thu Mar 31 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.8-alt1
- initial release

