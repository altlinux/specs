Name: libcompizconfig
Version: 0.8.8
Release: alt3
Summary: Settings library for plugins - OpenCompositing Project
License: GPL
Group: System/Libraries
Url: http://www.compiz-fusion.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: COMPIZ_CORE_ABIVERSION = %compiz_core_abi_version

BuildRequires(Pre): rpm-build-compiz
BuildRequires: compiz-devel >= %version
BuildRequires: gcc-c++ glib2-devel intltool libGL-devel libprotobuf-devel
BuildRequires: protobuf-compiler xorg-xextproto-devel xorg-xineramaproto-devel

%description
The OpenCompositing Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
through plugins and themes contributed by the community giving a
rich desktop experience.

%package devel
Summary: Development file for libcompizconfig
Group: Development/C
Requires: %name = %version-%release

%description devel
Development file for libcompizconfig

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
rm -f %buildroot%_libdir/compiz/libccp.la
rm -f %buildroot%_libdir/compizconfig/backends/libini.la


%files
%dir %_sysconfdir/compizconfig
%config(noreplace) %_sysconfdir/compizconfig/config
%dir %_libdir/compiz
%dir %_libdir/compizconfig
%dir %_libdir/compizconfig/backends
%_libdir/compiz/*.so
%_libdir/compizconfig/backends/*.so
%_libdir/*.so.*
%_datadir/compiz/ccp.xml

%files devel
%_includedir/compizconfig
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt3
- restore compiz in Sisyphus

* Thu Jul 07 2011 Mikhail Efremov <sem@altlinux.org> 0.8.8-alt2.M60P.1
- Change TRUE value of Bool type to '1' (closes: #25681).

* Thu Apr 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Sat Oct 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt3
- rebuild with libprotobuf.so.6

* Sat Dec 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- rebuild

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt3
- rebuild for new compiz ABI

* Thu Jun 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- rebuild with libprotobuf.so.4

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt5
- rebuild with compiz-0.8.0

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt4
- updated build dependencies

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- enabled expo plugin by defaults

* Tue Sep 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt2
- rebuild

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt1
- 0.6.99

* Tue Nov 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt2
- fix for buffer overflow in strncat

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Wed Aug 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- initial release

