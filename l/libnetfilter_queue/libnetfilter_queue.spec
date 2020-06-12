Name: libnetfilter_queue
Version: 1.0.5
Release: alt1

Summary: Netfilter queue userspace library
Url: https://www.netfilter.org/projects/libnetfilter_queue/
License: GPL-2.0-or-later and GPL-2.0-only
Group: System/Libraries
Source: %name-%version.tar

BuildRequires: libnfnetlink-devel libmnl-devel

%description
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter.  It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%package devel
Summary: Development part of libnetfilter_queue
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the development part of libnetfilter_queue.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files
%_libdir/*.so.*
%doc COPYING

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Jun 12 2020 Dmitry V. Levin <ldv@altlinux.org> 1.0.5-alt1
- 1.0.3 -> 1.0.5.

* Tue Mar 05 2019 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- 1.0.2 -> 1.0.3.

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- New version
- cleanup spec

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1.4
- Fixed build

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1.3
- Fixed build

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1.2
- Removed bad RPATH

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.15-alt1.1
- rebuild (with the help of girar-nmu utility)

* Wed Aug  8 2007 Avramenko Andrew <liks@altlinux.ru> 0.0.15-alt1
- Initial build for Sisyphus
