# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 4

Name: xdotool
Epoch: 1
Version: 4.20260303.1
Release: alt1

Summary: Fake keyboard/mouse input for X

Group: System/X11
License: BSD
URL: https://www.semicomplete.com/projects/xdotool/
VCS: https://github.com/jordansissel/xdotool

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXtst-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libXinerama-devel
BuildRequires: perl-podlators

%description
This tool lets you simulate keyboard input and mouse activity, move and
resize windows, etc. It does this using X11's XTEST extension and other
Xlib functions.  Additionally, you can search for windows and move,
resize, hide, and modify window properties like the title. If your
window manager supports it, you can use xdotool to switch desktops, move
windows between desktops, and change the number of desktops.

%package -n libxdo%sover
Summary: Library for fake keyboard/mouse input for X
Group: System/Libraries
Requires: libxdo%sover = %EVR

%description -n libxdo%sover
libxdo helps you send fake mouse and keyboard input, search for windows,
perform various window managment tasks such as desktop changes, window
movement, etc.

Shared Library.

%package -n xdotool-devel
Summary: Library for fake keyboard/mouse input for X
Group: Development/C
Requires: libxdo%sover = %EVR

%description -n xdotool-devel
libxdo helps you send fake mouse and keyboard input, search for windows,
perform various window managment tasks such as desktop changes, window
movement, etc.

Development files.

%prep
%setup
%autopatch -p1

%build
%make_build \
	WITHOUT_RPATH_FIX=1

%install
%make	DESTDIR=%buildroot \
	PREFIX=%prefix \
	INSTALLMAN=%_mandir \
	INSTALLINCLUDE=%_includedir \
	INSTALLLIB=%_libdir \
	install

%files
%doc CHANGELIST COPYRIGHT README.md
%doc examples
%_bindir/*
%_man1dir/*.1.*

%files -n libxdo%sover
%_libdir/libxdo.so.%sover

%files -n xdotool-devel
%_libdir/libxdo.so
%_libdir/pkgconfig/libxdo.pc
%_includedir/xdo.h

%changelog
* Sat Nov 07 2026 Anton Midyukov <antohami@altlinux.org> 1:4.20260303.1-alt1
- Build from upstream git tag.
- Fix version.
- Separate subpackage libxdo4 with shared library.

* Mon Jun 11 2018 Vitaly Lipatov <lav@altlinux.ru> 20160805.1-alt1
- new version 20160805.1 (with rpmrb script)

* Wed Feb 18 2015 Fr. Br. George <george@altlinux.ru> 20110530.1-alt2
- Fix invalid early recursion return

* Sat Nov 02 2013 Afanasov Dmitry <ender@altlinux.org> 20110530.1-alt1
- 2.20110530.1

* Fri Feb 04 2011 Afanasov Dmitry <ender@altlinux.org> 20101012-alt2
- fix mandir

* Thu Feb 03 2011 Afanasov Dmitry <ender@altlinux.org> 20101012-alt1
- 20101012

* Tue Oct 07 2008 Nick S. Grechukh <gns@altlinux.org> 20080606-alt1
- first build for ALT Linux

