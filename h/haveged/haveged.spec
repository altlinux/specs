Name: haveged
Version: 1.9.2
Release: alt1
License: GPLv3
Group: System/Kernel and hardware
Summary: Feed entropy into random pool
Url: http://www.issihosts.com/haveged/
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
  --enable-daemon\
  --disable-static \
  --enable-init=sysv.redhat
%make_build

%check
make check

%install
mkdir -p %buildroot%_initdir
ln -s rc.d/init.d %buildroot/etc/init.d
%makeinstall
#install -D -m0755 init.d/haveged %buildroot%_initdir/%name
#install -D -m0644 init.d/havege.service  %buildroot%_unitdir/%name.service

%files
%doc README
%_man8dir/haveged.8*
%_sbindir/haveged
%_initdir/%name
%_libdir/*.so.*
#_unitdir/haveged.service

%files devel
%_man3dir/libhavege.3*
%dir %_includedir/%name
%_includedir/%name/havege.h
%doc contrib/build/havege_sample.c
%_libdir/*.so

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Mon Dec 16 2013 Fr. Br. George <george@altlinux.ru> 1.7c-alt1
- Initial buildfrom upstream spec
