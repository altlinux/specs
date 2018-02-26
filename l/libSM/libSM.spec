Name: libSM
Version: 1.2.1
Release: alt1
Summary: X Session Management Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libICE-devel libuuid-devel xmlto xorg-xtrans-devel xorg-util-macros xorg-sgml-doctools

%description
X Session Management Library

%package devel
Summary: X Session Management Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%def_enable ipv6

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-libuuid \
	%{subst_enable ipv6} \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_docdir/%name
%_includedir/X11/SM
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Mar 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt4
- enabled ipv6

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 1.2.0-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Aug 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Nov 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt3
- updated build dependencies

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jul 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon May 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3:
  + Sanitized hex string conversion in SmsGenerateClientID().
  + Fixed some const vs non-const mix ups.
  + Don't reinvent the wheel and just use strdup().
  + Removed some global writable variables.
  + Revert "Don't reinvent the wheel and just use strdup()."
  + Another tiny char* vs const char* fix.

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

