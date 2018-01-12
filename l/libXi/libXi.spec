Name: libXi
Version: 1.7.9
Release: alt1%ubt
Summary: X Input Extension Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: asciidoc libX11-devel libXext-devel libXfixes-devel xmlto xorg-inputproto-devel
BuildRequires: xorg-sgml-doctools xorg-util-macros

%description
X Input Extension Library

%package devel
Summary: X Input Extension Library and Header Files
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
* Fri Jan 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.7.9-alt1%ubt
- 1.7.9 (closes: #34447)

* Fri Sep 05 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Tue Jul 16 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Jun 28 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.7.1.901-alt1
- 1.7.2 RC1

* Fri Apr 05 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Thu Mar 07 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt1
- 1.7

* Thu Jan 17 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Thu May 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.5.99.3-alt1
- 1.5.99.3

* Tue Mar 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Dec 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Fri Dec 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Tue Jun 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Sat Mar 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Sat Mar 19 2011 Alexey Tourbin <at@altlinux.ru> 1.4.1-alt3
- disabled symbol versioning

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 1.4.1-alt2
- rebuilt for debuginfo

* Wed Jan 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Nov 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt3
- devel: fixed pkg-config requires

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt2
- rebuild

* Thu Aug 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt1
- 1.3

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Dec 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- defined _XiGetDevicePresenceNotifyEvent

* Wed Dec 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Nov 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sun Aug 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt3
- calculate the length field correctly

* Fri Nov 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt2
- Coverity #743/744: Returned without freeing storage bufp/savp

* Sat Sep 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.1.3
- drop upstream patches

* Thu May 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt3
- added libXi-1.0.2-git-XiGetExtensionVersion.patch

* Thu May 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- added libXi-1.0.2-git-UnlockDisplay.patch

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

