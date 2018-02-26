%define ver_major 3.2
%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_enable gtk
%def_disable orbit
%def_enable gsettings

%define _libexecdir %_prefix/libexec
%define _rpmmacrosdir %_rpmlibdir/macros.d

%define oldname GConf2

Name: GConf
Version: %ver_major.5
Release: alt1

Provides: %oldname = %version
Obsoletes: %oldname < %version

Summary: Gnome Config System
Summary(ru_RU.KOI8-R): Система конфигурации Gnome
License: %lgpl2plus
Group: System/Servers
Url: http://projects.gnome.org/gconf/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Source1: gconf.rpmmacros
Source2: gconf2_set
Source3: gconf2_add
Source4: gconf2_get
Source5: gconf_sync_state

# stylesheet for strip translations (using XInclude)
# from gconf schema files. Thanks vyt@.
Source10: gconf2-strip-locales.xsl
# gconf2-strip-locales.sh for apply gconf2-strip-locales.xsl
# (%%gconf2_stripschemas rpm macros uses it).
Source11: gconf2-strip-locales.sh

Source15: libgconf.map
Source16: libgconf.lds
Patch1: %name-2.24.0-alt-symver.patch

# from Fedora: patch to reload GConf2 every time a schema is
# added or removed (gnome bug # 333353)
Patch2: GConf-2.18.0.1-reload.patch

%define ORBit_ver 2.12.1
%define glib_ver 2.25.12
%define libxml2_ver 2.6.17
%define gnome_common_ver 2.8.0
%define gir_ver 0.6.7
%define gio_ver 2.31.0

Requires: lib%name = %version-%release
Requires: dbus-tools-gui

# for patch2 /usr/bin/killall required
# Requires: psmisc

BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildPreReq: gnome-common >= %gnome_common_ver
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: intltool >= 0.35
BuildPreReq: gettext-tools
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libgtk+3-devel
BuildPreReq: libldap-devel
BuildPreReq: libdbus-devel libdbus-glib-devel libpolkit1-devel polkit

%{?_enable_orbit:BuildPreReq: ORBit2-devel >= %ORBit_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver}
%{?_enable_gsettings:BuildPreReq: libgio-devel >= %gio_ver}

# to build manpages.
BuildPreReq: help2man

%description
GConf is the Configuration database system for GNOME. However it can be
used with plain GTK+, Xlib, KDE, or even text mode applications as well.

%package -n lib%name
Summary: Gnome Config System library package
Group: System/Libraries
Provides: lib%oldname = %version
Obsoletes: lib%oldname < %version

%description -n lib%name
GConf library package. Contains files needed for using GConf.

%package -n lib%name-devel
Summary: Gnome Config System development package
Group: Development/C
Provides: lib%oldname-devel = %version
Obsoletes: lib%oldname-devel < %version
Requires: lib%name = %version-%release
Requires: %name-sanity-check = %version-%release

%description -n lib%name-devel
GConf development package. Contains files needed for doing
development using GConf.

%package -n lib%name-devel-doc
Summary: Development documentation for GConf
Group: Development/C
Conflicts: lib%name < %version
Provides: lib%oldname-devel-doc = %version
Obsoletes: lib%oldname-devel-doc < %version
BuildArch: noarch

%description -n lib%name-devel-doc
GConf is the GNOME Configuration database system.

This package contains development documentation for GConf.

%package sanity-check
Summary: Graphical GConf utility
Group: System/Configuration/Other
Requires: %name = %version-%release

%description sanity-check
This package contains graphical GConf utility which require GTK+.

%package -n lib%name-devel-static
Summary: Gnome Config System development package
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
GConf static libraries package. Contains libraries needed for doing
development using GConf.

%package -n lib%name-gir
Summary: GObject introspection data for the GConf library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GConf library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GConf library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GConf library

%prep
%setup -q
install -p -m644 %_sourcedir/libgconf.{map,lds} gconf/
%patch1 -p1
%patch2 -p1 -b .reload

# disable localization for gconfd
%__subst 's,\(setlocale (.* \"\),\1C,' gconf/gconfd.c

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable static} \
	%{subst_enable introspection} \
	%{subst_enable orbit} \
	%{?_enable_gsettings:--enable-gsettings-backend} \
	%{subst_enable gtk}

# SMP-incompatible build
%make

%install
%make_install DESTDIR=%buildroot install

cat <<__EOF__ >%buildroot%_sysconfdir/gconf/schema-install-source
xml:readwrite:%_cachedir/gconf/gconf.xml.defaults
__EOF__

cat <<__EOF__ >>%buildroot%_sysconfdir/gconf/2/path
xml:readonly:%_cachedir/gconf/gconf.xml.defaults
__EOF__

mkdir -p %buildroot%_datadir/gconf
install -m644 %SOURCE10 %buildroot%_datadir/gconf/
install -m755 %SOURCE11 %buildroot%_datadir/gconf/

mkdir -p %buildroot%_cachedir/gconf/gconf.xml.{defaults,mandatory,system}
mkdir -p %buildroot%_sysconfdir/gconf/{schemas,gconf.xml.system}
chmod 755 %buildroot{%_sysconfdir,%_cachedir}/gconf/gconf.xml.{defaults,mandatory,system}

install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat <<__EOF__ >%buildroot%_sysconfdir/buildreqs/files/ignore.d/gconf
^%_rpmmacrosdir/%name
__EOF__

mkdir -p %buildroot{%_bindir,%_sbindir}
install -p -m755 %SOURCE2 %SOURCE3 %SOURCE4 %buildroot%_bindir/
install -p -m755 %SOURCE5 %buildroot%_sbindir/

cat <<__EOF__ >%buildroot%_sbindir/gconf_install_schema
#!/bin/sh -e

export GCONF_CONFIG_SOURCE=\$(gconftool-2 --get-default-source)
for S in \$*; do
    gconftool-2 --makefile-install-rule "%gconf_schemasdir/\$S.schemas" >/dev/null
done
%_sbindir/gconf_sync_state
__EOF__

cat <<__EOF__ >%buildroot%_sbindir/gconf_uninstall_schema
#!/bin/sh -e

export GCONF_CONFIG_SOURCE=\$(gconftool-2 --get-default-source)
for S in \$*; do
    gconftool-2 --makefile-uninstall-rule "%gconf_schemasdir/\$S.schemas" >/dev/null
done
%_sbindir/gconf_sync_state
__EOF__

chmod 755 %buildroot%_sbindir/gconf_{,un}install_schema

# build man page for gconftool-2
LD_LIBRARY_PATH=gconf/.libs \
help2man -N --name="is a tool to control GConf from the command line" \
	    --manual="Gnome Config System" \
	    gconf/.libs/gconftool-2 > gconftool-2.man

install -pD -m644 gconftool-2.man %buildroot%_man1dir/gconftool-2.1

%find_lang GConf2

%files -f GConf2.lang
%_bindir/*
%_sbindir/gconf*
%_libexecdir/gconfd-2
%_libexecdir/gconf-defaults-mechanism
%_datadir/sgml/gconf
%dir %_datadir/gconf
%dir %_datadir/GConf
%_datadir/GConf/*
%_datadir/gconf/gconf2-strip-locales.sh
%_datadir/gconf/gconf2-strip-locales.xsl
%_datadir/dbus-1/services/org.gnome.GConf.service
%_datadir/dbus-1/system-services/org.gnome.GConf.Defaults.service
%_datadir/polkit-1/actions/org.gnome.gconf.defaults.policy
%dir %_sysconfdir/gconf
%dir %_sysconfdir/gconf/2
%dir %_sysconfdir/gconf/gconf.xml.defaults
%dir %_sysconfdir/gconf/gconf.xml.mandatory
%dir %_sysconfdir/gconf/gconf.xml.system
%dir %_sysconfdir/gconf/schemas
%dir %_cachedir/gconf
%dir %_cachedir/gconf/gconf.xml.defaults
%dir %_cachedir/gconf/gconf.xml.mandatory
%dir %_cachedir/gconf/gconf.xml.system
%_sysconfdir/xdg/autostart/gsettings-data-convert.desktop
%config(noreplace) %_sysconfdir/gconf/2/path
%config(noreplace) %_sysconfdir/gconf/2/evoldap.conf
%config(noreplace) %_sysconfdir/gconf/schema-install-source
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.gnome.GConf.Defaults.conf
%_man1dir/*
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/GConf
%dir %_libdir/GConf/2
%_libdir/GConf/2/*.so
%_libdir/gio/modules/libgsettingsgconfbackend.so

%exclude %_libdir/gio/modules/libgsettingsgconfbackend.la

%files sanity-check
%_libexecdir/gconf-sanity-check-2

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/aclocal/*
%_rpmmacrosdir/%name
%_sysconfdir/buildreqs/files/ignore.d/gconf

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%_libdir/GConf/2/*.a
%endif

%exclude %_libdir/GConf/*/*.la

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%changelog
* Sun Mar 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.5-alt1
- 3.2.5

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt1.1
- Rebuild with Python-2.7

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Jul 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.5-alt2
- added dbus-tools-gui to rqs (ALT #25844)

* Fri Jul 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.5-alt1
- 2.32.5
- ORBit-free build

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.4-alt1
- 2.32.4

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt2
- build gconf-sanity-check against gtk+3 for GNOME3

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Thu Feb 17 2011 Alexey Tourbin <at@altlinux.ru> 2.32.0-alt3
- rebuilt for debuginfo
- disabled symbol versioning

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- rebuild for update dependencies

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.7-alt1
- 2.31.7

* Fri Apr 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.2-alt1
- 2.31.2
- introspection support
- build gsettings backend
- updated version script for GCONF_2.31.2

* Fri Apr 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt2
- applied a lost patch to reload gconfd every time a schema is added or
  removed (gnome bug #333353)

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.0-alt1
- 2.27.1

* Tue Sep 01 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt3.1
- rebuild with libldap2.4

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt3
- don't use "which" in gconf2_* scripts (closes #21036)

* Fri Jun 19 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt2
- Don't use rpm-build-spec2macro.
- Fix file references in ignore.d directory.

* Thu May 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Wed May 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Feb 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- 2.25.1

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.0-alt1
- 2.25.0

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt3
- removed obsolete %%post{,un}_ldconfig
- packaged lost %%_sysconfdir/gconf/gconf.xml.system directory
- moved dependent on GTK+ gconf-sanity-check to separate -sanity-check subpackage
- rpm macros moved to %%_rpmlibdir/macros.d
- moved GConf and libraries to System/Servers and System/Libraries rpm
  groups respectively
- don't rebuild documentation
- added lost "Obsoletes" tag for lib%%name-devel-doc subpackage

* Mon Oct 06 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt2
- add versioning
- define libexec dir as /usr/libexec

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- New version (2.24.0).
- build with PolicyKit support
- build lib%name-devel-doc as noarch

* Wed Mar 12 2008 Alexey Rusakov <ktirf@altlinux.org> 2.22.0-alt1
- New version (2.22.0).

* Mon Feb 25 2008 Alexey Rusakov <ktirf@altlinux.org> 2.21.90-alt1
- New version (2.21.90).
- Fixed ALT Bug 14633.

* Tue Feb 05 2008 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt3
- Updated gconf_sync_state script; now it checks that /proc exists before
  start-stop-daemon invocation.

* Wed Jan 09 2008 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt2
- Fixed gconf_sync_state (ALT Bug #13934).

* Tue Nov 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- New version (2.20.1).
- Use macros from rpm-build-gnome and rpm-build-licenses.
- Added gconf_sync_state, gconf_install_schema and gconf_uninstall_schema
  scripts, to facilitate working with schemas from command line. RPM macros
  are now defined in terms of these scripts.
- gconf2_install and gconf2_uninstall macros are now defined in terms of
  these scripts. The macros notify all GConf daemons running in the
  system about applied changes.

* Thu Sep 20 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.0.1 -> 2.20.0

* Sat May 19 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0.1-alt1
- new version (2.18.0.1)
- replaced %%__ macros with respective commands.
- added /etc/gconf/schemas directory to the files list.
- renamed gconf2 source to gconf.rpmmacros.
- updated dependencies (no more libpopt dep, among others).

* Thu Mar 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt1
- new version (2.16.1)
- spec cleanup
- bzipped ChangeLog (Bug #11073)
- updated dependencies

* Thu Jun 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt2
- removed '2' from the package name
- fixed bug #9681

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5-alt1
- new version
- updated dependencies
- minor spec improvements

* Thu Nov 03 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed excess buildreqs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sat Feb 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1.1
- create /var/gconf/{gconf.xml.defaults,gconf.xml.mandatory}
  with right permissions.

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Mon Dec 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Tue Dec 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt2
- changed default schemas install source from /etc to /var.
- documentation moved to devel-doc subpackage.

* Fri Nov 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1.1
- disable localization for gconfd (#5480).

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Thu Aug 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Sun Jul 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Jan 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Jun 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3
- gconf2_uninstall macro.

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Thu Jan 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt2
- doesn't provides old GConf.

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Jan 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Tue Dec 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt9
- Some fixes and updates from cvs.

* Sun Dec 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt8
- %%default_source macro renamed to %%gconf2_default_source (#1648)

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt7
- %%post/%%postun fixed.

* Fri Oct 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt6
- gconf2_set script modified (tested in gedit package).
- new gconf2_{set_new,unset,unset_r} macros. Only gconf2_set_new
  tested in gnome-panel package.
- gconf2_get auxiliary script/macro added.

* Fri Oct 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt5.1
- Localized output from gconftool-2 disabled.

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.1-alt5
- fixed gconf2_set macro:
   * fix gconftool-2 call,
   * have to create separate script to avoid rpm spec preprocessing problems
- spec improvements (%%setup -q)

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt4
- rebuild with new pango.

* Tue Oct 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt3.2
- gconf2_set macro added to %_sysconfdir/rpm/macros.d/gconf2 macrofile.
- Added %_sysconfdir/rpm/macros.d/gconf2 to buildreq ignores.
- Manpage for gconftool-2 added.

* Fri Sep 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt3
- %_sysconfdir/rpm/macros.d/gconf2 macrofile added (ldv). It provides
  gconf2_install macro for schemas installation. Requires: rpm >=
  4.0.4-alt1
- (Igor Androsov)
    - Improved dependencies.
    - Added provides GConf, can replace GConf.
- Partiallly applied patch from Igor Androsov to get gconfd messages
  readable while we can't use .utf8 locales.

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt2
- %install section fixed.

* Sun Sep 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Jun 12 2002 Igor Androsov <blake@altlinux.ru> 1.2.0-alt1
- New version

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 1.1.11-alt1.1
- Other fix BuildRequires
- Fixes %files

* Mon Jun 03 2002 Igor Androsov <blake@altlinux.ru> 1.1.11-alt1
- New version
- Fix BuildRequires

* Fri May 31 2002 Igor Androsov <blake@altlinux.ru> 1.1.10-alt1
- Initial build for AltLinux

* Thu May 23 2002 Igor Androsov <blace@mail.ru> 1.1.10-blk1
- Change GConf-devel to libGConf2-devel
- Fixes spec

* Sat May 11 2002 Igor Androsov <blace@mail.ru> 1.1.10-blk0.2
- New version from CVS
- Minor changes spec file

* Wed May 08 2002 Igor Androsov <blace@mail.ru> 1.1.10-blk0.1
- New soruces from CVS
- Spec for AltLinux
- Moved static libs to devel-static
- Moved libs to libGConf2
