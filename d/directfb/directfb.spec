%define realname DirectFB

Name: directfb
Version: 1.1.0
Release: alt4

Summary: %realname - drivers and binaries
License: GPL
Group: System/Libraries
Url: http://www.directfb.org

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %realname-%version.tar.gz

Patch0:	%realname-am.patch
Patch1:	%realname-pmake.patch
Patch2:	%realname-fix.patch

# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=462626&msg=35
Patch3:	%realname-tty.patch

# http://bugs.gentoo.org/show_bug.cgi?id=200661
Patch4:	%realname-0.9.25.1-sysfs.patch

Patch5: %realname-alt-libadd-fix.patch

# Automatically added by buildreq on Sun Dec 14 2008
BuildRequires: gcc-c++ glibc-devel-static libX11-devel libXext-devel libfreetype-devel libjpeg-devel libpng-devel libsysfs-devel man

%description
%realname is a graphics library which was designed with embedded systems
in mind. It offers maximum hardware accelerated performance at a minimum
of resource usage and overhead.

%package -n lib%name
Summary: %realname - graphics and windowing library on Linux framebuffer
Group: System/Libraries

%description -n lib%name
%realname is a graphics library which was designed with embedded systems
in mind. It offers maximum hardware accelerated performance at a minimum
of resource usage and overhead.

%package -n lib%name-devel
Summary: Includes and other files for devel %realname applications
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%description -n lib%name-devel
Devel for %realname is a graphics library which was designed with embedded systems
in mind. It offers maximum hardware accelerated performance at a minimum
of resource usage and overhead.

%package -n lib%name-devel-static
Summary: Static libraries for devel %realname applications
Group: Development/C
Requires: %name = %version-%release

%description -n lib%name-devel-static
Static libraries for devel %realname applications

%prep
%setup -q -n %realname-%version
%patch0 -p1 -b .fix0
%patch1 -p1 -b .fix1
%patch2 -p1 -b .fix2
%patch3 -p1 -b .fix3
%patch4 -p1 -b .fix4
%patch5 -p1 -b .fix5

%build
%autoreconf
%configure \
	--enable-fbdev \
	--enable-shared \
	--enable-static \
	--with-pic \
	--with-gfxdrivers=all \
	#
%make_build

%install
%make install DESTDIR=%buildroot

find %buildroot -name \*.la -delete
{
	find %buildroot%_libdir/%name-* -name '*.so' -print
	find %buildroot%_libdir/%name-* -type d -printf '%%%%dir %%p\n'
} |
	sed -e 's#%{buildroot}##' |
	sort -u > %name.files
find \
	%buildroot%_libdir/lib*.a \
	%buildroot%_libdir/%name-* \
	-type f \( -name '*.a' -o -name '*.o' \) |
		sed -e 's#^%{buildroot}##' |
		sort -u > %name-static.files

%files -f %name.files
%doc TODO fb.modes
%_bindir/mk*
%_bindir/dfb*
%_datadir/%name-*
%_man1dir/dfb*
%_man5dir/*

%files -n lib%name
%doc AUTHORS NEWS README
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_bindir/%{name}*
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_man1dir/%{name}*

%files -n lib%name-devel-static -f %name-static.files

%changelog
* Sun Dec 19 2010 Alexey Gladkov <legion@altlinux.ru> 1.1.0-alt4
- Rebuilt for new depends.

* Mon Dec 15 2008 Alexey Gladkov <legion@altlinux.ru> 1.1.0-alt3
- Update build requires (Dmitry V. Levin).

* Fri Apr 04 2008 Alexey Gladkov <legion@altlinux.ru> 1.1.0-alt2
- Fix directfb to able use virtual console.
- Add gfxdrivers.
- Add static libs.
- Update build requires.

* Sun Oct 14 2007 Alexey Gladkov <legion@altlinux.ru> 1.1.0-alt1
- New version (1.1.0).
- Changed libraries sonames from lib*-0.9.so.25 to lib*-1.1.so.0

* Fri Sep 01 2006 Alexey Gladkov <legion@altlinux.ru> 0.9.25.1-alt1
- New version (0.9.25.1).
- Soname change.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.24-alt2.1.1
- Rebuilt for new pkg-config dependencies.

* Tue Dec 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.24-alt2.1
- Rebuild with libsysfs.so.2.0.0 .

* Tue Dec 13 2005 Anton D. Kachalov <mouse@altlinux.org> 0.9.24-alt2
- x86_64 support

* Sun Oct 30 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.9.24-alt1
- 0.9.24
- rename %name-devel subpackage to lib%name-devel
- fixed BuildRequires
- cleanup spec

* Fri Dec 10 2004 Grigory Milev <week@altlinux.ru> 0.9.21-alt1.20041024
- new snapshot version released

* Tue Feb 24 2004 Grigory Milev <week@altlinux.ru> 0.9.20-alt1
- new version released

* Fri Dec 12 2003 Grigory Milev <week@altlinux.ru> 0.9.17-alt2
- remove *.la files due policy

* Tue Apr 15 2003 Grigory Milev <week@altlinux.ru> 0.9.17-alt1
- new version released

* Fri Feb 28 2003 Grigory Milev <week@altlinux.ru> 0.9.16-alt1
- new version released

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 0.9.13-alt1
- new version released
- rebuild with gcc3
- remover perl from build requires

* Mon Apr 29 2002 Grigory Milev <week@altlinux.ru> 0.9.9-alt2
- libification

* Tue Apr  9 2002 Grigory Milev <week@altlinux.ru> 0.9.9-alt1
- new version released
- remove all examples, now in separated package

* Fri Oct 12 2001 AEN <aen@logic.ru> 0.9.6-alt2
- rebuilt with libpng.so.3

* Mon Oct  8 2001 Grigory Milev <week@altlinux.ru> 0.9.6-alt1
- new version released
- move development files to separated package

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.5-alt2
- Built with system libtool.

* Fri Sep 14 2001 Grigory Milev <week@altlinux.ru> 0.9.5-alt1
- New version 0.9.5.

* Tue Aug 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.4-alt2
- Enabled libmpeg3 support.

* Fri Jul 27 2001 Grigory Milev <week@altlinux.ru> 0.9.4-alt1
- First build for Sisyphus


