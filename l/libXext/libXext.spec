Name: libXext
Version: 1.3.1
Release: alt1
Summary: Misc X Extension Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXau-devel xmlto xorg-xextproto-devel xorg-util-macros xorg-sgml-doctools

%description
Misc X Extension Library

%package devel
Summary: Misc X Extension Library and Header Files
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
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%dir %_docdir/%name
%_docdir/%name/*.html
%_includedir/X11
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sat May 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 1.2.0-alt4
- rebuilt for cpp.req

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 1.2.0-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt3
- rebuild

* Sun Oct 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- added conflict to xorg-xextproto-devel <= 7.0.5 (closes #23598)

* Fri Jun 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Oct 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Feb 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sun Dec 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- Coverity #467: security_error_list has fewer than XSecurityNumberErrors entries

* Fri Jan 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Sep 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt4
- CVS snapshot 2006-04-02

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

