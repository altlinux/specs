Name:           xdotool
Version:        20110530.1
Release:        alt2
Summary:        Fake keyboard/mouse input for X

Group:          System/X11
License:        BSD
URL:            http://www.semicomplete.com/projects/xdotool/
Source0:        %{name}.tar
Patch:		xdotool-recursion-continue.patch

BuildRequires:  libXtst-devel       
BuildRequires:	libXinerama-devel
BuildRequires:	perl-podlators

%description
This tool lets you simulate keyboard input and mouse activity, move and
resize windows, etc. It does this using X11's XTEST extension and other
Xlib functions.  Additionally, you can search for windows and move,
resize, hide, and modify window properties like the title. If your
window manager supports it, you can use xdotool to switch desktops, move
windows between desktops, and change the number of desktops.

%package -n xdotool-devel
Summary: Library for fake keyboard/mouse input for X
Group: Development/C

%description -n xdotool-devel
libxdo helps you send fake mouse and keyboard input, search for windows,
perform various window managment tasks such as desktop changes, window
movement, etc.

Development files.

%prep
%setup -q -n %name
%patch

%build
%make_build

%install
%make	DESTDIR=%buildroot \
	PREFIX=%prefix \
	INSTALLMAN=%_mandir \
	INSTALLINCLUDE=%_includedir \
	INSTALLLIB=%_libdir \
	install

%files
%doc CHANGELIST COPYRIGHT README
%doc examples
%_bindir/*
%_man1dir/*
%_libdir/libxdo.so.*

%files -n xdotool-devel
%_libdir/libxdo.so
%_includedir/xdo.h

%changelog
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

