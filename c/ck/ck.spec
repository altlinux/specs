# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    ck
Version: 0.7.1
Release: alt1
Summary: Library for high performance concurrent programming
License: BSD
URL:     https://github.com/concurrencykit/ck
Group:   Other
Source:  ck-%version.tar

BuildRequires: gcc

%description
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

%package devel
Summary: Header files and libraries for CK development
Group: Development/Other
Requires: %name = %EVR

%description devel
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

This package provides the libraries, include files, and other
resources needed for developing Concurrency Kit applications.

%prep
%setup

%build
export CFLAGS="%optflags"
./configure \
	--libdir=%_libdir \
	--includedir=%_includedir/%name \
	--mandir=%_mandir \
	--prefix=%_prefix
%make_build

%install
%makeinstall_std

# fix weird mode of the shared library
chmod 0755 %buildroot%_libdir/libck.so.*

# remove static library
rm %buildroot%_libdir/libck.a

%files
%doc LICENSE
%_libdir/libck.so.*

%files devel
%_libdir/libck.so
%_includedir/%name
%_libdir/pkgconfig/%name.pc
%_mandir/man3/*.3.*

%changelog
* Fri Jul 02 2021 Anton Midyukov <antohami@altlinux.org> 0.7.1-alt1
- new version 0.7.1
- drop old upstream patch

* Mon Mar 04 2019 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
