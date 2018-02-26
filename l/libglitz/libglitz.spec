Name: libglitz
Version: 0.5.7
Release: alt4
Serial: 1
Summary: OpenGL compositing library
Group: System/Libraries
URL: http://www.freedesktop.org/Software/glitz
License: BSD

Source: glitz-%version.tar
Patch: glitz-%version-%release.patch

BuildRequires: libGL-devel libICE-devel libX11-devel

%description
OpenGL compositing library

%package glx
Summary: OpenGL compositing library (GLX backend)
Group: System/Libraries
Requires: %name = %version-%release

%description glx
OpenGL compositing library (GLX backend)

%package devel
Summary: Headers for developing programs that will use glitz
Group: Development/C
Requires: %name = %version-%release %name-glx = %version-%release

%description devel
This package contains the headers that programmers will need to develop
applications which will use glitz library.

%prep
%setup -q -n glitz-%version
%patch -p1

%build
%autoreconf
%configure \
    --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS README TODO COPYING
%_libdir/%name.so.*

%files glx
%_libdir/%name-glx.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue May 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.7-alt4
- fixed URL, License

* Fri Dec 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.7-alt3
- moved glx backend to subpackage (close #17071)

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.7-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Nov 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.7-alt1
- 0.5.7

* Tue Dec 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.6-alt2
- added glitz-glx-get-proc-address.diff

* Mon Jun 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.6-alt1
- 0.5.6

* Sat Apr 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.4-alt1
- 0.5.4

* Wed Mar 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Tue Feb 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Sat Jul 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Fri Apr 29 2005 Anton D. Kachalov <mouse@altlinux.org> 0.4.0-alt1.1
- reconfigure

* Sat Feb 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Tue Aug 24 2004 Kachalov Anton <mouse@altlinux.ru> 0.1.3-alt2
- rebuild

* Thu Jul 08 2004 Kachalov Anton <mouse@altlinux.ru> 0.1.3-alt1
- first build for Sisyphus

