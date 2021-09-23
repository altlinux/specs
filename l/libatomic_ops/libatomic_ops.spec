%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%define rawname		atomic_ops
%define major		1
%define libname		lib%{rawname}%{major}
%define libgpl		lib%{rawname}_gpl%{major}
%define libname_devel	lib%{rawname}-devel

%def_enable shared

Name:		libatomic_ops
Version:	7.6.12
Release:	alt1
Summary:	A library for accessing hardware provided atomic memory operations
Group:		Development/C
# libatomic_ops MIT, libatomic_ops_gpl GPLv2
License:	GPLv2+ and MIT
URL:		https://github.com/ivmai/libatomic_ops
Source0:	https://github.com/ivmai/libatomic_ops/releases/download/v%{version}/%{name}-%{version}.tar

%description
Multiplatform atomic memory operation library.

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n	%{libgpl}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libgpl}
This package contains the shared library for %{name}.

%package -n	%{libname_devel}
Summary:	Multiplatform atomic memory operation library
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgpl} = %{version}-%{release}
# Cross-arch provides
Provides:	%{name}-devel = %{version}
Provides:	%{rawname}-devel = %{version}

%description -n	%{libname_devel}
Provides implementations for atomic memory update operations on a number of
architectures. This allows direct use of these in reasonably portable code.
Unlike earlier similar packages, this one explicitly considers memory barrier
semantics, and allows the construction of code that involves minimum overhead
across a variety of architectures.

The package has been at least minimally tested on X86, Itanium, Alpha,
PA-RISC, PowerPC, and SPARC, with Linux, Microsoft Windows, HP/UX, Solaris
and MACOSX operating systems. Some implementations are more complete than
others.

It should be useful both for high performance multi-threaded code which can't
afford to use the standard locking primitives, or for code that has to access
shared data structures from signal handlers. For details, see README.txt in
the distribution.

The most recent version adds support for operations on data of different
sizes, and adds an optional library providing almost-lock-free stacks (see
Boehm, "An almost non-blocking stack", also here) and a signal-handler-safe
memory allocator based on it. See README_stack.txt and README_malloc.txt for
details.

%package devel-static
Summary: A library for accessing hardware provided atomic memory operations
Group: Development/C
Requires: %{libname_devel} = %EVR

%description devel-static
This package provides semi-portable access to hardware provided
atomic memory operations.  These might allow you to write code:

- That does more interesting things in signal handlers.
- Makes more effective use of multiprocessors by allowing you to write
  clever lock-free code.  Note that such code is very difficult to get
  right, and will unavoidably be less portable than lock-based code.  It
  ia also not always faster than lock-based code.  But it may occasionally
  be a large performance win.
- To experiment with new and much better thread programming paradigms, etc.

It should be useful both for high performance multi-threaded code which can't
afford to use the standard locking primitives, or for code that has to access
shared data structures from signal handlers. For details, see README.txt in
the distribution.

The most recent version adds support for operations on data of different
sizes, and adds an optional library providing almost-lock-free stacks (see
Boehm, "An almost non-blocking stack", also here) and a signal-handler-safe
memory allocator based on it. See README_stack.txt and README_malloc.txt for
details.

%prep
%setup -q

%build
%autoreconf
%configure \
	--enable-static \
	%{subst_enable shared}
%make_build

%install
%makeinstall_std

%check
%ifarch armv5tl
# Not SMP safe on armv5, which is fine has armv5 has no SMP support, but we
# build armv5 on an armv7 kernel with SMP...
taskset -c 0 make check
%else
%make_build -k check
%endif

%files devel-static
%_libdir/*.a

%if_enabled shared
%files -n %{libname}
%_libdir/lib%{rawname}.so.%{major}*

%files -n %{libgpl}
%_libdir/lib%{rawname}_gpl.so.%{major}*

%files -n  %{libname_devel}
%endif

%doc AUTHORS ChangeLog README.md doc/[LR]*
%exclude %_datadir/doc/%name/
%_includedir/*.h
%dir %_includedir/%{rawname}
%_includedir/%{rawname}/*.h
%dir %_includedir/%{rawname}/sysdeps
%_includedir/%{rawname}/sysdeps/*.h
%dir %_includedir/%{rawname}/sysdeps/gcc
%_includedir/%{rawname}/sysdeps/gcc/*.h
%dir %_includedir/%{rawname}/sysdeps/hpc
%_includedir/%{rawname}/sysdeps/hpc/*.h
%dir %_includedir/%{rawname}/sysdeps/ibmc
%_includedir/%{rawname}/sysdeps/ibmc/*.h
%dir %_includedir/%{rawname}/sysdeps/icc
%_includedir/%{rawname}/sysdeps/icc/*.h
%dir %_includedir/%{rawname}/sysdeps/loadstore
%_includedir/%{rawname}/sysdeps/loadstore/*.h
%dir %_includedir/%{rawname}/sysdeps/msftc
%_includedir/%{rawname}/sysdeps/msftc/*.h
%dir %_includedir/%{rawname}/sysdeps/sunc
%_includedir/%{rawname}/sysdeps/sunc/*.h
%dir %_includedir/%{rawname}/sysdeps/armcc
%_includedir/%{rawname}/sysdeps/armcc/*.h
%_libdir/pkgconfig/%{rawname}.pc
%_libdir/lib%{rawname}*.so

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 7.6.12-alt1
- new version 7.6.12

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 7.6.8-alt2
- fixed build with LTO

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 7.6.8-alt1
- new version 7.6.8
- added devel subpackage

* Tue Sep 26 2017 Vladimir Lettiev <crux@altlinux.org> 7.4.6-alt1
- Updated to 7.4.6

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 7.2d-alt1
- Updated to 7.2d.

* Thu Jun 28 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- Initial build
