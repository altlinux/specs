%ifarch %ix86
%define platform x86-linux-gcc
%else
%ifarch arm
%define platform armv5te-linux-gcc
%else
%define platform %_arch-linux-gcc
%endif
%endif

Name: libvpx
Version: 1.1.0
Release: alt1
Summary: VP8 video codec
Group: Video
License: BSD
Url: http://www.webmproject.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: doxygen
%ifarch %ix86 x86_64
BuildRequires: yasm
%endif

%description
VP8 is an open video codec, originally developed by On2 and released
as open source by Google Inc. It is the successor of the VP3 codec,
on which the Theora codec was based

%package devel
Summary: VP8 Libraries and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1

%build
%ifarch %ix86 x86_64
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%endif
./configure \
	--prefix=%prefix \
	--libdir=%_libdir \
	--enable-pic \
	--target=%platform \
	--enable-shared
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS LICENSE PATENTS CHANGELOG
%_libdir/*.so.*

%files devel
%_includedir/vpx
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sat May 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Jan 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7.1-alt1
- 0.9.7-p1

* Fri Aug 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Sat Mar 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Fri Jun 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sun Jun 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt2
- GIT snapshot 2010-06-03 (7aa97a35b515bfb7d7bbcdee4db376f815343e44)

* Thu May 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- initial release

