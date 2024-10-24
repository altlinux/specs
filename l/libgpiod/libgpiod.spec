Name: libgpiod
Version: 2.1.3
Release: alt1

Summary: Linux GPIO interacting library
License: LGPL-2.1
Group: System/Libraries
Url: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git

Source0: %name-%version-%release.tar

BuildRequires: autoconf-archive gcc-c++ help2man
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%package -n libgpiod2
Summary: Linux GPIO interacting library
Group: System/Libraries

%package c++
Summary: C++ bindings for libgpiod
Group: System/Libraries

%package devel
Summary: Linux GPIO interacting library
Group: Development/C

%package -n gpio-tools
Summary: Linux GPIO interacting tools
Group: System/Kernel and hardware
Provides: libgpiod-utils = %EVR
Obsoletes: libgpiod-utils

%package -n python3-module-gpiod
Summary: Python 3 bindings for %name
Group: Development/Python3
Provides: python3-module-libgpiod = %EVR
Obsoletes: python3-module-libgpiod

%define desc C library and tools for interacting with the linux GPIO \
character device (gpiod stands for GPIO device).\
Since linux 4.8 the GPIO sysfs interface is deprecated. User space should use\
the character device instead. This library encapsulates the ioctl calls and\
data structures behind a straightforward API.

%description
%desc

%description -n libgpiod2
%desc
This package contains libgpiod shared library.

%description c++
%desc
This package contains C++ bindings for libgpiod.

%description devel
%desc
This package contains development part of libgpiod.

%description -n gpio-tools
%desc
This package contains command-line tools.

%description -n python3-module-gpiod
%desc
This package contains Python bindings for libgpiod.

%prep
%setup

%build
%autoreconf
%configure --disable-static --enable-tools --enable-bindings-cxx
%make_build
# isn't that lovely
%pyproject_build --backend-config-settings \
	'{"--build-option": [
			"build_ext",
			"--inplace",
			"--include-dirs=../../include",
			"--library-dirs=../../lib/.libs"]}' \
	bindings/python

%install
%makeinstall_std
%pyproject_install bindings/python/dist/*.whl

%files -n libgpiod2
%doc COPYING README
%_libdir/libgpiod.so.*

%files c++
%_libdir/libgpiodcxx.so.*

%files devel
%_includedir/gpiod.h
%_includedir/gpiod.hpp
%_includedir/gpiodcxx
%_libdir/libgpiod.so
%_libdir/libgpiodcxx.so
%_pkgconfigdir/libgpiod.pc
%_pkgconfigdir/libgpiodcxx.pc

%files -n gpio-tools
%doc COPYING NEWS README TODO
%_bindir/gpio*
%_man1dir/gpio*.1*

%files -n python3-module-gpiod
%python3_sitelibdir/gpiod
%python3_sitelibdir/gpiod-*.dist-info

%changelog
* Thu Oct 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.3-alt1
- 2.1.3 released

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1.1
- NMU: added missing build dependency on setuptools.

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- 2.1.1 released

* Mon Mar 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Thu Sep 21 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

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
