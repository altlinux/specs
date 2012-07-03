Name: xrandr
Version: 1.3.5
Release: alt1
Summary: primitive command line interface to RandR extension
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXrandr-devel libXrender-devel xorg-util-macros

%description
Xrandr is used to set the screen size, orientation  and/or  reflection.
The  -s  option is a small integer index used to specify which size the
screen should be set to.  To find out what sizes are available, use the
-q option, which reports the sizes available, the current rotation, and
the possible rotations and reflections.  The default size is the  first
size  specified in the list.  The -o option is used to specify the ori-
entation of the screen, and can be one of "normal inverted left right 0
1 2 3".

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*.1*

%changelog
* Thu Jun 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Sat Jul 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt3
- GIT snapshot 2010-02-11 (d138c73276226ce424d36e80ce745aa9461f110e)

* Sun Sep 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt2
- removed xkeystone (closes: #21549)

* Fri Sep 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Aug 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Thu Apr 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Feb 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.99.4-alt1
- 1.2.99.4

* Tue Jan 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.99.3-alt1
- 1.2.99.3

* Wed Aug 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt2
- updated manpage

* Sat Mar 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Thu Jan 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt2
- GIT snapshot 2007-12-15 (close #13854)

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Apr 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt3
- GIT snapshot 2007-04-25 (739f01957c8ebd3b7bcecfd7ad8174884561f7db)

* Fri Apr 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- GIT snapshot 2007-04-06 (49aab1e0e4cb2226d5bcc8e4e6217309fd23ce52)

* Tue Mar 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Mar 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- CVS snapshot 2006-03-20

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

