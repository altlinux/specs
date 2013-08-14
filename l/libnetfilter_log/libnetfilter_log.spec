Name: libnetfilter_log
Version: 1.0.1
Release: alt1
Serial: 1

Summary: libnfnetlink receive to-be-logged packets from the kernel nfnetlink_log subsystem
Url: http://netfilter.org/projects/libnetfilter_log/
License: %gpl2plus
Group: System/Libraries
#git://git.netfilter.org/libnetfilter_log
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libnfnetlink-devel >= 0.0.40

%description
libnetfilter_log is a userspace library providing interface to packets
that have been logged by the kernel packet filter. It is is part of
a system that deprecates the old syslog/dmesg based packet logging.

%package devel
Summary: Development part of libnetfilter_log.
Group: Development/C
Requires: %name = %{?epoch:%epoch:}%version-%release

%description devel
Development part of libnetfilter_log.

%prep
%setup
%patch -p1

%build
# Use nfnetlink_log.h from glibc-kernheaders
KERNEL_DIR=%_includedir/linux-default/ ./autogen.sh distrib
%configure \
	--disable-static
%make_build

%install
#mkdir -p %buildroot%_libdir/%name
#mkdir -p %buildroot%_includedir/%name
%makeinstall_std

%files
%_libdir/*.so.*
%doc COPYING

%files devel
%_includedir/%name/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Wed Aug 14 2013 Mikhail Efremov <sem@altlinux.org> 1:1.0.1-alt1
- autogen.sh: Use mktemp instead of tempfile.
- Updated to 1.0.1.

* Thu Aug 23 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.0.15-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for libnetfilter_log

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.15-alt1.1
- Removed bad RPATH

* Sun Mar 01 2009 Avramenko Andrew <liks@altlinux.ru> 1:0.0.15-alt1
- New version

* Fri Apr 13 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt2
- Moved to git repo
- Split devel package
- Disable static
- Spec clean up

* Wed Apr 11 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt1
- New version build from svn snapshot
- Spec clean up

* Fri Mar 23 2007 Avramenko Andrew <liks@altlinux.ru> 0.0.13-alt1
- Initial build for Sisyphus
