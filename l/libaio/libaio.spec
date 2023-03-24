Name: libaio
Version: 0.3.113
Release: alt1

Summary: Linux-native asynchronous I/O access library
License: LGPLv2+
Group: System/Libraries
Url: https://pagure.io/libaio
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: /proc

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

%package devel-static
Summary: Linux-native asynchronous I/O access static library
Group: Development/C
Requires: libaio-devel = %version-%release

%description devel-static
This package contains static library for
the Linux-native asynchronous I/O facility ("async I/O", or "aio").

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std \
	prefix=%_prefix libdir=/%_lib usrlibdir=%_libdir

%check
%make partcheck

%files
/%_lib/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 0.3.113-alt1
- new version 0.3.113

* Thu Jun 24 2021 Alexey Shabalin <shaba@altlinux.org> 0.3.112-alt1
- new version 0.3.112

* Wed Jun 27 2018 Alexey Shabalin <shaba@altlinux.ru> 0.3.111-alt1
- 0.3.111
- add package with static library
- add patches from debian for support more arches

* Sat Jan 28 2017 Michael Shigorin <mike@altlinux.org> 0.3.110-alt1.1
- E2K: partially added mcst patch.

* Tue Aug 19 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.110-alt1
- New version.

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
