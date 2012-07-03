Name: libatomic_ops
Version: 1.2
Release: alt1

Summary: library for accessing hardware provided atomic memory operations
Group: Development/C
License: Distributable
Url: http://www.hpl.hp.com/research/linux/atomic_ops

Source0: %name-%version.tar.bz2

%package devel-static
Summary: library for accessing hardware provided atomic memory operations
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
%setup

%build
%configure
%make_build

%install
%makeinstall
rm -f doc/Makefile*

%files devel-static
%doc doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_includedir/atomic_ops
%_includedir/atomic_ops.h
%_includedir/atomic_ops_malloc.h
%_includedir/atomic_ops_stack.h
%_libdir/%{name}*.a

%changelog
* Thu Jun 28 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- Initial build
