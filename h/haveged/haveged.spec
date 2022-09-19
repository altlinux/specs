Name: haveged
Version: 1.9.18
Release: alt1
License: GPLv3
Group: System/Kernel and hardware
Summary: Feed entropy into random pool
Url: http://www.issihosts.com/haveged/
# Source0-url: https://github.com/jirka-h/haveged/archive/refs/tags/v%version.tar.gz
Source0: http://www.issihosts.com/haveged/haveged-%version.tar.gz

%description
The haveged daemon feeds the linux entropy pool with random
numbers generated from hidden processor state.

%package devel
Summary: haveged development files
Group: Development/C

%description devel
Headers and shared object symbolic links for the haveged library

This package contains the haveged implementation of the HAVEGE
algorithm and supporting features.

%prep
%setup

%build
%autoreconf
%configure \
  --enable-daemon \
  --disable-static \
  --enable-olt=no
%make_build

%check
make check

%install
%makeinstall

#Install systemd service file
sed -e 's:@SBIN_DIR@:%_sbindir:g' -i contrib/Fedora/*service
sed -i '/^ConditionKernelVersion/d' contrib/Fedora/*service

install -Dpm 0644 contrib/Fedora/haveged.service %buildroot%_unitdir/%name.service
install -Dpm 0644 contrib/Fedora/haveged-once.service %buildroot%_unitdir/%name-once.service
install -Dpm 0644 contrib/Fedora/90-haveged.rules %buildroot%_udevrulesdir/90-%name.rules

%post
%post_service haveged

%preun
%preun_service haveged
%files
%doc AUTHORS COPYING NEWS README.md ChangeLog
%_man8dir/haveged.8*
%_sbindir/haveged
%_libdir/*.so.*
%_unitdir/haveged.service
%_unitdir/haveged-once.service
%_udevrulesdir/*.rules

%files devel
%_man3dir/libhavege.3*
%dir %_includedir/%name
%_includedir/%name/havege.h
%doc contrib/build/havege_sample.c
%_libdir/*.so

%changelog
* Mon Sep 19 2022 L.A. Kostis <lakostis@altlinux.ru> 1.9.18-alt1
- 1.9.18.
- Drop init.d service (removed by upstream)
- Add -once systemd service and udev rules.

* Tue Jul 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.14-alt1
- NMU: new version 1.9.14 (with rpmrb script)

* Mon Apr 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.2-alt2
- add systemd unit file

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Mon Dec 16 2013 Fr. Br. George <george@altlinux.ru> 1.7c-alt1
- Initial buildfrom upstream spec
