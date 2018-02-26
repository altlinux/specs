Name: libnfnetlink
Version: 1.0.0
Release: alt1.2
Serial: 1

Summary: libnfnetlink - low-level nfnetlink message processing functions
Url: http://netfilter.org/projects/libnfnetlink/
Packager: Avramenko Andrew <liks@altlinux.ru>
License: GPL
Group: System/Libraries

Source: %name-%version.tar

%description
libnfnetlink is the low-level library for netfilter related kernel/userspace 
communication. It provides a generic messaging infrastructure for in-kernel 
netfilter subsystems (such as nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) 
and their respective users and/or management tools in userspace.

%package devel
Summary: development part of libnfnetlink
Group: Development/C
Requires: %name = %version-%release

%description devel
Development part of libnfnetlink

%prep
%setup

%build
%autoreconf -fisv
%configure --disable-static
%make_build DESTDIR=%buildroot

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_includedir/%name
make install DESTDIR=%buildroot

%files
%_libdir/*.so.*
%doc README

%files devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.0-alt1.1
- Rebuilt for soname set-versions

* Sat Oct 30 2010 Anton Farygin <rider@altlinux.ru> 1:1.0.0-alt1
- New version
- build from upstream git
- removed gcc-c++ buildrequires

* Sun Mar 01 2009 Avramenko Andrew <liks@altlinux.ru> 1:0.0.40-alt1
- New version

* Sat Apr 19 2008 Avramenko Andrew <liks@altlinux.ru> 1:0.0.33-alt1
- New version

* Wed Aug  1 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.30-alt1
- New version

* Tue Apr 17 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt2
- Split devel package
- Disable static
- Moved to git
- Spec clean up

* Wed Apr 11 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt1
- New version build from svn snapshot
- Spec clean up

* Fri Mar 23 2007 Avramenko Andrew <liks@altlinux.ru> 0.0.16-alt1
- Initial build for Sisyphus
