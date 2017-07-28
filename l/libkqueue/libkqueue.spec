%set_verify_elf_method unresolved=strict

Name: libkqueue
Version: 2.0.1
Release: alt2
Summary: Portable implementation of the kqueue() and kevent() system calls
License: MIT / BSD
Group: System/Libraries
Url: https://sourceforge.net/projects/libkqueue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

Patch1: %name-%version-alt-gcc6.patch

%description
A user space implementation of the kqueue(2) kernel event notification
mechanism. libkqueue acts as a translator between the kevent structure
and the native kernel facilities.

%package devel
Summary: Development files of libkqueue
Group: Development/C
Requires: %name = %EVR

%description devel
A user space implementation of the kqueue(2) kernel event notification
mechanism. libkqueue acts as a translator between the kevent structure
and the native kernel facilities.

This package contains development files of libkqueue.

%prep
%setup
%patch1 -p2

%build
%add_optflags %optflags_shared
%configure --disable-static
%make_build
 
%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man2dir/*

%changelog
* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt2
- Fixed build with new toolchain

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus

