Name: libXcomposite
Version: 0.4.3
Release: alt3
Summary: X Composite Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel libXfixes-devel xmlto xorg-compositeproto-devel xorg-util-macros

%description
X Composite Library

%package devel
Summary: X Composite Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: XFree86-devel < 4.4 xorg-x11-devel <= 6.9.0

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
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*.3*

%changelog
* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 0.4.3-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.3-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Wed Jun 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu May 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Tue Mar 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.3-alt1
- 0.3

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2-alt0.1
- initial build

