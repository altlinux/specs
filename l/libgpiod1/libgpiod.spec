Name: libgpiod1
Version: 1.6.4
Release: alt2

Summary: Linux GPIO interacting library
License: LGPL-2.1
Group: System/Legacy libraries
Url: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/

Source0: %name-%version-%release.tar

BuildRequires: autoconf-archive gcc-c++ help2man
BuildRequires: python3-devel python3-module-setuptools

%define desc C library and tools for interacting with the linux GPIO \
character device (gpiod stands for GPIO device).\
Since linux 4.8 the GPIO sysfs interface is deprecated. User space should use\
the character device instead. This library encapsulates the ioctl calls and\
data structures behind a straightforward API.

%description
%desc

%prep
%setup

%build
%autoreconf
%configure --disable-tools --disable-static

%make_build

%install
%makeinstall_std

%files
%doc COPYING README
%_libdir/libgpiod.so.*

%changelog
* Mon Mar 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.4-alt2
- rebuilt as legacy library

* Fri Feb 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.4-alt1
- 1.6.4 released

* Fri Mar 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 reelased

* Mon Dec 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt1
- 1.6.2 released

* Wed Sep 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.4-alt1
- 1.4.4 released

* Thu Jan 16 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- initial build for ALT
