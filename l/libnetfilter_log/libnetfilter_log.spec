Name: libnetfilter_log
Version: 0.0.15
Release: alt1.1
Serial: 1

Summary: libnfnetlink receive to-be-logged packets from the kernel nfnetlink_log subsystem
Url: http://netfilter.org/projects/libnetfilter_log/
Packager: Avramenko Andrew <liks@altlinux.ru>
License: %gpl2plus
Group: System/Libraries
Source: %name-%version.tar
Requires: libnfnetlink >= 0.0.40

BuildRequires: gcc-c++ libnfnetlink-devel >= 0.0.40 rpm-build-licenses

%description
libnetfilter_log is a userspace library providing interface to packets that have been
logged by the kernel packet filter. It is is part of a system that deprecates the old
syslog/dmesg based packet logging.

%package devel
Summary: Development part of libnetfilter_log.
Group: Development/C
Requires: %name = %version-%release

%description devel 
Development part of libnetfilter_log.

%prep
%setup

%build
#./autogen.sh
%configure --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%_includedir/%name
make install DESTDIR=%buildroot

%files
%_libdir/*.so.*
%doc COPYING

%files devel
%_includedir/%name/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
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
