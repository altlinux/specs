Name: libxcb
Version: 1.8.1
Release: alt1
Summary: The X C Binding (XCB) library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: doxygen fonts-ttf-freefont graphviz libXau-devel libXdmcp-devel xorg-xcbproto-devel xsltproc libselinux-devel

%description
libxcb provides an interface to the X Window System protocol, slated to
replace the current Xlib interface. It has several advantages over
Xlib, including:
  - size: small library and lower memory footprint
  - latency hiding: batch several requests and wait for the replies later
  - direct protocol access: one-to-one mapping between interface and protocol
  - proven thread support: transparently access XCB from multiple threads
  - easy extension implementation: interfaces auto-generated from XML-XCB

Xlib can also use XCB as a transport layer, allowing software to make
requests and receive responses with both, which eases porting to XCB.
However, client programs, libraries, and toolkits will gain the most
benefit from a native XCB port.

%package devel
Summary: XCB Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-xinput \
	--enable-selinux \
	--disable-xprint \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot htmldir=%_docdir/%name-devel install

%files
%doc NEWS README
%_libdir/*.so.*

%files devel
%doc %_docdir/%name-devel
%_includedir/xcb
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Wed Jan 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.8-alt1
- 1.8

* Sun Feb 27 2011 Alexey Tourbin <at@altlinux.ru> 1.7-alt6
- rebuilt for pkgconfig

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 1.7-alt5
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt4
- devel: fixed pkg-config requires

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt3
- rebuild

* Sat Aug 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt2
- enabled SELinux support

* Fri Aug 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt1
- 1.7

* Fri Apr 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt1
- 1.6

* Fri Dec 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt1
- 1.5

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4-alt2
- added DRI2 support

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4-alt1
- 1.4

* Fri May 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt1
- 1.3

* Wed Feb 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt2
- disabled XCB Xprint Extension
- enabled XCB XInput Extension

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Tue Jan 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.93-alt1
- 1.1.93

* Wed Dec 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.92-alt1
- 1.1.92

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt6
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sat Sep 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt4.M41.1
- build for branch 4.1

* Thu Sep 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt5
- drop libxcb-1.0-abstract-socket.patch

* Tue Dec 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt4
- rebuild

* Sun Nov 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt3
- make IPv6 optional

* Fri Nov 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt2
- update libxcb-1.1-alt-ndebug.patch

* Mon Nov 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Mon Oct 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt6
- GIT snaphot 2007-10-28 (a29fbc2645fabb96d02c382ffef499b48fb1514a)

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt5
- fixed xlib.lock
- drop libxcb-1.0-lock-unlock.patch

* Sun Oct 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt4
- libxcb-1.0-abstract-socket.patch: When connecting to the X server, prefer
  abstract-namespace unix sockets to filesystem-bound sockets.

* Thu Sep 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt3
- GIT snapshot 2007-07-19 (09045eaac34973662aaa820a94ca8ed66d9dcb4e)

* Thu May 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt2
- added libxcb-1.0-lock-unlock.patch

* Wed May 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- 1.0

* Fri Nov 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.93-alt1
- initial release

