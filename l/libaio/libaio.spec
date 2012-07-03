Name: libaio
Version: 0.3.109
Release: alt2

Summary: Linux-native asynchronous I/O access library
License: LGPLv2+
Group: System/Libraries
URL: http://pkgs.fedoraproject.org/gitweb/?p=libaio.git
Packager: Victor Forsiuk <force@altlinux.org>
Source: ftp://ftp.kernel.org/pub/linux/libs/aio/libaio-%version.tar.bz2
Patch1: libaio-install-to-slash.patch
Patch2: libaio-deb-man-errors.patch

# 0.3.109 supports ARM architecture.
#ExclusiveArch: %ix86 x86_64

%description
The Linux-native asynchronous I/O facility ("async I/O", or "aio") has a richer
API and capability set than the simple POSIX async I/O facility. This library,
libaio, provides the Linux-native API for async I/O. The POSIX async I/O
facility requires this library in order to provide kernel-accelerated async I/O
capabilities, as do applications which require the Linux-native async I/O API.

%package devel
Summary: Development files for Linux-native asynchronous I/O access
Group: Development/C
Requires: libaio = %version-%release

%description devel
This package provides header files to include and libraries to link with
for the Linux-native asynchronous I/O facility ("async I/O", or "aio").

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
#subst 's/ -O./ %optflags/' Makefile
%make_build

%install
%make install destdir=%buildroot \
	libdir=/%_lib usrlibdir=%_libdir includedir=%_includedir
# Convert absolute symlink into relative.
v=`readlink %buildroot%_libdir/%name.so`
ln -snf ../../%_lib/${v##*/} %buildroot%_libdir/%name.so
%set_verify_elf_method strict

%files
/%_lib/*.so.*

%files devel
%_libdir/*.so
%exclude %_libdir/*.a
%_includedir/*

%changelog
* Thu Aug 11 2011 Dmitry V. Levin <ldv@altlinux.org> 0.3.109-alt2
- Imported manpage fixes from Debian.
- Made %name.so symlink relative.
- Rebuilt for debuginfo.

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 0.3.109-alt1
- 0.3.109

* Wed Aug 26 2009 Victor Forsyuk <force@altlinux.org> 0.3.107-alt2
- Move library to /lib (close: ALT#21230).

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 0.3.107-alt1
- 0.3.107

* Mon Apr 07 2008 Victor Forsyuk <force@altlinux.org> 0.3.106-alt2
- One-letter spec fix, library symlink should be owned only by -devel.

* Mon Apr 10 2006 Victor Forsyuk <force@altlinux.ru> 0.3.106-alt1
- 0.3.106

* Fri Jul 29 2005 Victor Forsyuk <force@altlinux.ru> 0.3.104-alt1
- Initial build.
