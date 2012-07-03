%add_findprov_lib_path %_libdir/pidgin
%add_findprov_lib_path %_libdir/purple-2

%define pidgin_ver 2.0.0
%def_enable xmms

Summary: Plugin Pack for libpurple and derived IM clients
Name: purple-plugin_pack
Version: 2.7.0
Release: alt1
License: GPLv2+
Group: Networking/Instant messaging
Url: http://plugins.guifications.org/

Source: purple-plugin-pack-%version.tar.bz2
Patch4: purple-plugin_pack-build-fixspell.patch
Patch5: purple-plugin_pack-2.6.2-alt-disable-def-debug.patch
Patch6: purple-plugin_pack-2.7.0-fix-libs.patch

Requires: libpurple >= %pidgin_ver

BuildRequires: intltool libtalkfilters-devel
BuildRequires: libgtk+2-devel perl-XML-Parser libaspell-devel 
BuildRequires: libgtkspell-devel  >= 2.0.2
BuildRequires: libpixman-devel libcairo-devel
# TODO: select enchant or aspell
BuildRequires: libenchant-devel 
BuildRequires: pidgin-devel >= %pidgin_ver
BuildRequires: python-modules
BuildRequires: libjson-glib-devel
BuildRequires: zlib-devel

%if_enabled xmms
BuildRequires: libxmms-devel gtk+-devel
%endif

Obsoletes: gaim-plugin_pack

%description
All the other plugins for all libpurple derived clients.

%package -n pidgin-plugin_pack
Summary:    Plugin Pack for Pidgin
Group:      Networking/Instant messaging
Requires:   pidgin >= %pidgin_ver

Obsoletes: gaim-plugin_pack
Provides: gaim-plugin_pack = %version-%release

%description -n pidgin-plugin_pack
All the other plugins for Pidgin

%if_enabled xmms
%package -n pidgin-plugin-xmms
Summary:    XMMS plugin for Pidgin
Group:      Networking/Instant messaging
Requires:   pidgin >= %pidgin_ver

%description -n pidgin-plugin-xmms
xmms-remote - Control xmms from Pidgin conversations
%endif

%prep
%setup -q -n purple-plugin-pack-%version
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%autoreconf
%configure --disable-debug --enable-nls
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang plugin_pack

%files -f plugin_pack.lang
%doc AUTHORS ChangeLog COPYING README
%_libdir/purple-2/*.so
%exclude %_libdir/purple-2/*.la

%files -n pidgin-plugin_pack
%doc AUTHORS ChangeLog COPYING README
%_libdir/pidgin/*.so
%exclude %_libdir/pidgin/*.la
%exclude %_libdir/pidgin/xmmsremote.so
%dir %_datadir/pixmaps/pidgin/plugin_pack
%_datadir/pixmaps/pidgin/protocols/??/*
%exclude %_datadir/pixmaps/pidgin/plugin_pack/xmmsremote

%if_enabled xmms
%files -n pidgin-plugin-xmms
%_libdir/pidgin/xmmsremote.so
%_datadir/pixmaps/pidgin/plugin_pack/xmmsremote
%endif

%changelog
* Tue Mar 13 2012 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Fri Feb 05 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2
- fix build with ONE spell library (ALT #22777). thx to ildar@
- disable debug build
- update buildreq

* Tue Oct 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Apr 20 2009 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Mon Dec 22 2008 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Apr 21 2008 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- separate xmms plugin to individual package (because required gtk+-1)

* Fri Dec 28 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt3
- fix build with automake-1.10 (run aclocal)

* Tue Nov 20 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt2
- fix undefined symbol in "timelog" plugin

* Sun Oct 28 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0
- add libaspell-devel,libgtkspell-devel to BuildRequires for build switchspell module
- add patch1 for fix undefined symbol from libaspell in switchspell module (fix #13205)

* Sat Aug 25 2007 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1
- changed version numbering scheme

* Tue May 08 2007 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt2
- 1.0 release
- rename gaim-plugin_pack -> purple-plugin_pack and pidgin-plugin_pack

* Thu Mar 01 2007 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1beta6
- initial build for ALT Linux Sisyphus
