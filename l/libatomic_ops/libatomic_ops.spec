Name: libatomic_ops
Version: 7.2d
Release: alt1

Summary: A library for accessing hardware provided atomic memory operations
Group: Development/C
License: GPLv2+ and MIT
Url: http://www.hpl.hp.com/research/linux/atomic_ops/
Source: http://www.hpl.hp.com/research/linux/atomic_ops/download/%name-%version.tar.gz

%package devel-static
Summary: A library for accessing hardware provided atomic memory operations
Group: Development/C

%description
This package provides semi-portable access to hardware provided
atomic memory operations.  These might allow you to write code:

- That does more interesting things in signal handlers.
- Makes more effective use of multiprocessors by allowing you to write
  clever lock-free code.  Note that such code is very difficult to get
  right, and will unavoidably be less portable than lock-based code.  It
  ia also not always faster than lock-based code.  But it may occasionally
  be a large performance win.
- To experiment with new and much better thread programming paradigms, etc.

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

%prep
%setup -n %name-7.2

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files devel-static
%_libdir/*.a
%_includedir/*
%_pkgconfigdir/*.pc
%exclude %_datadir/%name/
%doc AUTHORS ChangeLog README doc/[LR]*

%changelog
* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 7.2d-alt1
- Updated to 7.2d.

* Thu Jun 28 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- Initial build
