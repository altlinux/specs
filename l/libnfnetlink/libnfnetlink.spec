Name: libnfnetlink
Version: 1.0.1.0.8.5087
Release: alt1
Epoch: 1

Summary: Netfilter netlink userspace library
Url: https://netfilter.org/projects/libnfnetlink/
License: GPL-2.0-or-later
Group: System/Libraries
# https://git.netfilter.org/libnfnetlink/
# git://git.altlinux.org/gears/l/libnfnetlink
%define srcname %name-%version-%release
Source: %srcname.tar

%description
libnfnetlink is the low-level library for netfilter related kernel/userspace
communication.  It provides a generic messaging infrastructure for in-kernel
netfilter subsystems (such as libnetfilter_log, libnetfilter_queue, and
libnetfilter_conntrack) and their respective users and/or management tools
in userspace.

%package devel
Summary: Development part of libnfnetlink
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the development part of libnfnetlink.

%prep
%setup -n %srcname

%build
%autoreconf
%configure --disable-static
%make_build V=1

%install
%makeinstall_std V=1
rm %buildroot%_libdir/*.la

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files
%_libdir/*.so.*
%doc README

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Mar 05 2019 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.1.0.8.5087-alt1
- 1.0.1 -> 1.0.1-8-g5087de4.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1.qa1
- NMU: applied repocop patch

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 1:1.0.1-alt1
- New version

* Thu Aug 23 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.0.0-alt1.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for libnfnetlink

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
