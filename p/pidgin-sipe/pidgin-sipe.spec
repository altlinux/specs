%def_with vv
%def_with krb5
%def_enable purple
%def_disable telepathy

Name: pidgin-sipe
Version: 1.13.1
Release: alt1
Summary: Pidgin plugin for connecting to MS Communications Server

Group: Networking/Instant messaging
License: GPLv2+
Url: http://sipe.sourceforge.net/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: %name-%version.tar
Patch1: %name-%version-git_snapshot.patch

Requires: libpurple pidgin

BuildRequires: intltool libxml2-devel
BuildRequires: glib2-devel >= 2.28.0
BuildRequires: libpurple-devel >= 2.8.0
%{?_with_vv:BuildRequires: libnice-devel >= 0.1.0 gstreamer-devel}
%{?_with_krb5:BuildRequires: libkrb5-devel}
%{?_enable_telepathy:BuildRequires: libtelepathy-glib-devel}
BuildRequires: libnss-devel
BuildRequires: libgmime-devel >= 2.4.16

%description
Provides an Open Implementation of SIP/Simple protocol for connecting Pidgin to
Live Communications Server 2003/2005 and Office Communications Server 2007.

%prep
%setup -q
%patch1 -p1

%build
export KRB5_CFLAGS=`krb5-config --cflags`
%autoreconf
%configure \
	--disable-quality-check \
	%{subst_enable purple} \
	%{subst_enable telepathy} \
	%{subst_with vv} \
	%{subst_with krb5}

%make_build

%install
%make DESTDIR=%buildroot install
rm -f %buildroot%_libdir/purple-2/*.la
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog HACKING COPYING NEWS README TODO
%_libdir/purple-2/libsipe.so
%_pixmapsdir/pidgin/protocols/*/sipe.*

%changelog
* Fri May 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1.13.1-alt1
- 1.13.1

* Wed Mar 21 2012 Alexey Shabalin <shaba@altlinux.ru> 1.13.0-alt1
- 1.13.0

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt2.bc511e4
- git snapshot bc511e4d34c71a5025f3b884ae803bb5356deff9

* Mon Aug 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Wed Jun 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.11.2-alt2
- upstream snapshot ac3d61915fe3976502718baf40ca3ef72b7f7642
- build without voice and video support

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.11.2-alt1
- 1.11.2

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- stable 1.10.1
- build without voice and video support

* Wed May 26 2010 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt2.git_dcc66501
- git snapshot dcc665015b63e9c77de6573c63fa747d59ef968a (pre 1.11.0)
- build with voice and video support

* Mon Apr 19 2010 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1.git15372
- 1.9.0
- git snapshot 1537295681eaf3457716ab2ae9cae04a44b25a9e

* Thu Feb 11 2010 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1.git5a9509
- 1.8.0 + git snaphot 20100211

* Thu Dec 24 2009 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- Initial packaging
