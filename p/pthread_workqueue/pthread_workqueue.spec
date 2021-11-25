Name: pthread_workqueue
Version: 0.9.2
Release: alt1
Summary: Thread pool for libdispatch
License: BSD
Group: Development/C
Url: https://github.com/mheily/libpwq
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
libpthread_workqueue is a portable implementation of the
pthread_workqueue API first introduced in Mac OS X. It is primarily
intended for use with libdispatch but can be used as a general purpose
thread pool library for C programs.

%package -n lib%name
Summary: Thread pool for libdispatch
Group: System/Libraries

%description -n lib%name
libpthread_workqueue is a portable implementation of the
pthread_workqueue API first introduced in Mac OS X. It is primarily
intended for use with libdispatch but can be used as a general purpose
thread pool library for C programs.

%package -n lib%name-devel
Summary: Development files for thread pool of libdispatch
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
libpthread_workqueue is a portable implementation of the
pthread_workqueue API first introduced in Mac OS X. It is primarily
intended for use with libdispatch but can be used as a general purpose
thread pool library for C programs.

This package contains development files of libpthread_workqueue.

%prep
%setup

%build
%autoreconf
%configure --enable-static=no
%make_build
 
%install
%makeinstall_std

%files -n lib%name
%doc ChangeLog TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%changelog
* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sun Apr 07 2019 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

