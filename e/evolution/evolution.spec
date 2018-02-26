%define ver_major 3.4
%define ver_base 3.4
%def_disable static
%def_with openldap
%def_disable static_ldap
%def_with krb5
%def_with clutter
%def_disable map
%def_disable image_inline
%def_enable goa
# %define plugins experimental
%define plugins all

# Use stricter build settings than required by upstream.
%define strict_build_settings 1

Name: evolution
Version: %ver_major.3
Release: alt1

Summary: Integrated GNOME mail client, calendar and address book
License: GPLv2+
Group: Office
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Url: http://www.gnome.org/projects/%name/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

### Patches ###
# hack to properly link against ldap libs
Patch10: evolution-3.0.3-ldap_libs.patch
# Part of RH bug 170799:
Patch14: evolution-3.1.92-hide-switcher-buttons-by-default.patch
# RH bug #176400 
Patch27: evolution-2.9.1-im-context-reset.patch

%define evo_plugin_dir %_libdir/evolution/%ver_base/plugins
%define evo_module_dir %_libdir/evolution/%ver_base/modules

Provides: camel

# from configure.in
%define glib_ver 2.30.0
%define gtk_ver 3.2
%define clutter_gtk_ver 0.91.8
%define eds_ver 3.4.3
%define gnome_icon_ver 3.0.0
%define gnome_desktop_ver 2.91.6
%define gtkhtml_ver 4.4.3
%define libsoup_ver 2.33.6
%define dbus_ver 1.0.0
%define libnotify_ver 0.7.0
%define gweather_ver 2.91.6
%define ical_ver 0.43
%define gdata_ver 0.8.0
%define champlain_ver 0.12
%define goa_ver 3.1.1
%define pst_ver 0.6.54

Requires(post,preun): GConf
Requires: %name-data = %version-%release
Requires: evolution-data-server >= %eds_ver
Requires: gnome-settings-daemon

BuildPreReq: gnome-common
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgail3-devel >= %gtk_ver
BuildPreReq: gnome-icon-theme >= %gnome_icon_ver
BuildPreReq: evolution-data-server-devel >= %eds_ver
BuildPreReq: libgtkhtml4-devel >= %gtkhtml_ver
BuildPreReq: libGConf-devel libdbus-glib-devel
BuildPreReq: libgnomecanvas-devel
BuildPreReq: libgnome-desktop3-devel >= %gnome_desktop_ver
BuildPreReq: libxml2-devel
BuildPreReq: libsoup-gnome-devel >= %libsoup_ver
BuildPreReq: libdbus-devel >= %dbus_ver
BuildPreReq: libnotify-devel >= %libnotify_ver
BuildPreReq: libatk-devel
BuildPreReq: libX11-devel xorg-xproto-devel
BuildPreReq: libgweather-devel >= %gweather_ver
BuildPreReq: NetworkManager-devel >= 0.8.997
BuildPreReq: libical-devel >= %ical_ver
BuildPreReq: libgdata-devel >= %gdata_ver
BuildPreReq: libpst-devel >= %pst_ver
%{?_enable_goa:BuildPreReq: libgnome-online-accounts-devel >= %goa_ver}
%{?_with_clutter:BuildPreReq: libclutter-gtk3-devel >= %clutter_gtk_ver libmx-devel}
%{?_enable_map:BuildPreReq: libchamplain-gtk3-devel >= %champlain_ver libgeoclue-devel}
%{?_enable_image_inline:BuildRequires: libgtkimageview-devel}

# Some plugins/extensions link with others, resulting in multiple rpath entries
%set_verify_elf_method rpath=relaxed

BuildRequires: gcc-c++ docbook-utils flex intltool gnome-doc-utils gtk-doc libSM-devel libcom_err-devel gstreamer-devel
BuildRequires: python-modules-compiler python-modules-encodings libnspr-devel libnss-devel libX11-devel libcanberra-gtk3-devel
BuildRequires: zlib-devel


%if_with krb5
BuildRequires: libkrb5-devel
%endif

%if_with openldap
BuildRequires: libldap-devel
%if_enabled static_ldap
BuildRequires: libldap-devel-static libssl-devel libsasl2-devel.
%endif
%endif

%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

%package data
Summary: Evolution data files
Group: Office
BuildArch: noarch

%description data
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains common noarch files needed for  Evolution.

%package bogofilter
Group: Networking/Mail
Summary: Bogofilter plugin for Evolution
Requires: %name = %version-%release
Requires: bogofilter

%description bogofilter
This package contains the plugin to filter junk mail using Bogofilter.

%package spamassassin
Group: Networking/Mail
Summary: SpamAssassin plugin for Evolution
Requires: %name = %version-%release
Requires: spamassassin

%description spamassassin
This package contains the plugin to filter junk mail using SpamAssassin.

%package devel
Summary: Evolution development files
Group: Development/C
Requires: %name = %version-%release
Requires: evolution-data-server-devel >= %eds_ver

%description devel
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains files needed to develop Evolution plugins.

%package devel-doc
Summary: Evolution development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Evolution is the GNOME mailer, calendar, contact manager and
communications tool. The tools which make up Evolution will
be tightly integrated with one another and act as a seamless
personal information-management tool.

This package contains documentation needed to develop Evolution plugins.

%add_findprov_lib_path %_libdir/%name/%ver_base

%define _libexecdir %_prefix/libexec

%prep
%setup -q
%patch10 -b .ldaphack
%patch14 -p1 -b .hide-switcher-buttons-by-default
%patch27 -p1 -b .im-context-reset

%__subst '/use diagnostics/d' addressbook/tools/csv2vcard.in
subst 's,(Unstable),,' data/evolution.desktop*

# Remove the welcome email from Novell
for inbox in mail/default/*/Inbox; do
  echo -n "" > $inbox
done

# remove pregenerated .desktop files
rm -f data/*.desktop{,.in}

%build
%if_with openldap
%if_enabled static_ldap
%define ldap_flags --with-openldap=yes --with-static-ldap
# Set LIBS so that configure will be able to link with static LDAP libraries,
# which depend on Cyrus SASL and OpenSSL.  XXX Is the "else" clause necessary?
if pkg-config openssl ; then
    export LIBS="-lsasl2 `pkg-config --libs openssl`"
else
export LIBS="-lsasl2 -lssl -lcrypto"
fi
%else
%define ldap_flags --with-openldap=yes
%endif
%else
%define ldap_flags --without-openldap
%endif
export CPPFLAGS="-I%{_includedir}/et"
export CFLAGS="$RPM_OPT_FLAGS -fPIC -I%{_includedir}/et -Wno-sign-compare"

# Add stricter build settings here as the source code gets cleaned up. 
# We want to make sure things like compiler warnings and avoiding deprecated 
# functions in the GNOME/GTK+ libraries stay fixed. 
# 
# Please file a bug report at bugzilla.gnome.org if these settings break 
# compilation, and encourage the upstream developers to use them. 

%if %{strict_build_settings}
CFLAGS="$CFLAGS \
	-UGNOME_DISABLE_DEPRECATED \
	-fno-strict-aliasing"
%endif

#NOCONFIGURE=1 ./autogen.sh
gnome-doc-prepare -f
%autoreconf
export ac_cv_path_SENDMAIL=%_sbindir/sendmail
export KILL_PROCESS_CMD=%_bindir/killall
%configure \
    %{subst_enable static} \
    %ldap_flags \
    --with-sub-version=" (%version-%release)" \
    --with-kde-applnk-path=no \
    --enable-plugins=%plugins \
    --enable-nss \
    --enable-smime \
    --enable-audio-inline \
%if_with krb5
    --with-krb5=%_prefix \
    --with-krb5-libs=%_libdir \
    --with-krb5-includes=%_includedir/krb5 \
%endif
    --disable-schemas-install \
    --disable-schemas-compile \
    %{subst_with clutter} \
    %{?_enable_map:--enable-contact-maps} \
    %{subst_enable goa} \
    %{?_disable_image_inline:--disable-image-inline}

%make_build
#CFLAGS="$CFLAGS -UGNOME_DISABLE_DEPRECATED"

%install
%make DESTDIR=%buildroot install

# evolution command name
%__mv %buildroot%_bindir/evolution %buildroot%_bindir/evolution-%ver_major
%__ln_s evolution-%ver_major %buildroot%_bindir/evolution

# remove non-packaged files
%__rm -f %buildroot%_libdir/%name/%ver_base/*.la
%__rm -f %buildroot%_libdir/%name/%ver_base/*/*.la

# temporarily fix for other applications that requires thease libraries
for f in %buildroot%_libdir/%name/%ver_base/{libeshell*,libeutil*}; do
%__ln_s %name/%ver_base/`basename $f` %buildroot%_libdir/`basename $f`
done

# remove scrollkeeper files 
rm -rf %buildroot%_localstatedir/scrollkeeper

%find_lang --with-gnome --output=%name.lang %name %name-%ver_base

%define schemas apps-evolution-attachment-reminder apps-evolution-mail-notification apps-evolution-mail-prompts-checkdefault apps-evolution-template-placeholders apps_evolution_addressbook apps_evolution_calendar apps_evolution_email_custom_header apps_evolution_eplugin_face apps_evolution_shell evolution-mail

%post data
%gconf2_install %schemas

%preun data
if [ $1 = 0 ]; then
%gconf2_uninstall %schemas
fi

%post bogofilter
%gconf2_install evolution-bogofilter

%preun bogofilter
if [ $1 = 0 ]; then
%gconf2_uninstall evolution-bogofilter
fi

%post spamassassin
%gconf2_install evolution-spamassassin

%preun spamassassin
if [ $1 = 0 ]; then
%gconf2_uninstall evolution-spamassassin
fi

%files
%_bindir/*
%_libdir/%name/
%_libexecdir/%name/%ver_base/csv2vcard
%_libexecdir/%name/%ver_base/evolution-addressbook-export
%_libexecdir/%name/%ver_base/evolution-alarm-notify
%_libexecdir/%name/%ver_base/evolution-backup
%_libexecdir/%name/%ver_base/killev
%doc AUTHORS ChangeLog NEWS README

%exclude %evo_module_dir/libevolution-module-bogofilter.so
%exclude %evo_module_dir/libevolution-module-spamassassin.so

%files data -f %name.lang
%_datadir/applications/*
%_datadir/mime-info/*
%_datadir/%name

%_sysconfdir/xdg/autostart/evolution-alarm-notify.desktop
%_sysconfdir/gconf/schemas/apps-evolution-attachment-reminder.schemas
%_sysconfdir/gconf/schemas/apps-evolution-mail-notification.schemas
%_sysconfdir/gconf/schemas/apps-evolution-mail-prompts-checkdefault.schemas
%_sysconfdir/gconf/schemas/apps-evolution-template-placeholders.schemas
%_sysconfdir/gconf/schemas/apps_evolution_addressbook.schemas
%_sysconfdir/gconf/schemas/apps_evolution_calendar.schemas
%_sysconfdir/gconf/schemas/apps_evolution_email_custom_header.schemas
%_sysconfdir/gconf/schemas/apps_evolution_eplugin_face.schemas
%_sysconfdir/gconf/schemas/apps_evolution_shell.schemas
%_sysconfdir/gconf/schemas/evolution-mail.schemas

%_datadir/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.itip.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.mail-notification.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml
%_datadir/GConf/gsettings/evolution.convert
%_iconsdir/hicolor/*/*/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files devel-doc
%_datadir/gtk-doc/html/*

%files bogofilter
%evo_module_dir/libevolution-module-bogofilter.so
%_sysconfdir/gconf/schemas/evolution-bogofilter.schemas
%_datadir/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml

%files spamassassin
%evo_module_dir/libevolution-module-spamassassin.so
%_sysconfdir/gconf/schemas/evolution-spamassassin.schemas
%_datadir/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml

%changelog
* Mon Jun 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt2
- fixed pst-import plugin for libpst-0.6.54

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- temporarily disabled maps in contacts preview via libchamplain

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt2
- 3.0.3 ftp release

* Wed Jun 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3 snapshot

* Wed Jun 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- fixed schemas list

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Apr 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt2
- added x-scheme-handler/mailto mimetype to evolution.desktop
- updated translations

* Fri Apr 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt2
- updated buildreqs
- fixed build with newer GTK+

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- redefine %%_libexecdir to make evolution work on x86_64

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Thu Aug 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3
- remove pregenerated .desktop files (closes #23665)

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.2-alt2
- removed obsolete depenedece on gnome-spell

* Wed Apr 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.2-alt1
- 2.30.1.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90
- new -data noarch subpackage
- libpst support enabled

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6
- new devel-doc subpackage
- updated buildreqs

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0
- radically relaxed %%strict_build_settings

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri May 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt2
- fixed build with new libtool_2.2

* Wed Apr 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt1
- 2.26.1.1

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- NetworkManager support enabled

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post{,un} scripts

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1
- add COPYING to %%doc (see NEWS)
- attempt to properly link exchange plugin -- patch2 (shaba@)

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- drop patches for bugs that fixed in upstream

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3
- remove patches CVE-2008-1108 and CVE-2008-1109 (fixed upstream)

* Thu Jun 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt2
- Add patches for fix CVE-2008-1108 and CVE-2008-1109 (buffer overflow vulnerabilities)
- Remove the welcome email from Novell

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Fri May 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- 2.22.1.1
- drop patch18 for check line status (fixed upstream)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for evolution

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Thu Mar 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.3-alt1
- 2.12.3
- Removed patches:
  + RH bug #215467 / GNOME bug #380644 (fixed upstream)
  + GNOME bug #363695 (causes issues)
- Add patch for GNOME bug #454465 (fix Save button in task dialog)
- Revise patch for GNOME bug #417999

* Thu Nov 29 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Thu Oct 25 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt1
- 2.12.1
- Disable patch for GNOME bug #376991 for now. It may be contributing
  to password prompting problems as described in RH bug #296671.
- Revise patch for GNOME bug #362638 to fix GNOME bug #357175
  (Evolution fails to close after IMAP alert has been displayed).
- remove require perl-devel (ALT #13168)

* Fri Oct 12 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Evolution no longer requires libgnomeprint[ui].
- require libgtkhtml3 >= 3.16.0
- Revised patch for linking with krb5
- removed patches:
  + evolution-2.6.0-prototypes.patch (obsolete)
  + RH bug #157400 / GNOME bug #303877 (fixed upstream)
  + RH bug #157505 / GNOME bug #303878 (fixed upstream)
  + RH bug #190359 (fixed upstream)
  + RH bug #161885 / GNOME bug #309166 (fixed upstream)
  + RH bug #202751 / GNOME bug #355766 (fixed upstream)
  + RH bug #182247 (fixed upstream)
  + GNOME bug #373837 (fixed upstream)
  + RH bug #218801 (fixed upstream)
  + GNOME bug #373116 (fixed upstream)
  + RH bug #218898 / GNOME bug #385414 (fixed upstream)
  + GNOME bug #419469 (fixed upstream)
  + GNOME bug #419524 (fixed upstream)
  + GNOME bug #418971 (fixed upstream)
  + RH bug #234315 (fixed upstream)
  + RH bug #236399 (fixed upstream)
  + RH bug #236860 (fixed upstream)
  + RH bug #238155 (fixed upstream)
  + RH bug #240147 (fixed upstream)
- Add patches:
  + GNOME bug #476040 (fix attachment icon)
  + GNOME bug #477045 (use standard icon names)

* Mon Sep 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.10.3-alt2
- added Requires: gnome-settings-daemon (ALT Bug #12225)

* Fri Aug 17 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.3-alt1
- Update to 2.10.3
- change packager
- add/remove patches from fc7
- mini fix spec
- fix build with krb5 (patch1)

* Wed May 02 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt3
- CVE-2007-1002 (Shared memo categories format string vulnerability)
- fixed #11672 (crash during startup) 
 
* Sun Mar 11 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt2
- add some patches from Fedora updates

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt1
- new version 2.8.3

* Thu Jan 04 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.2.1-alt1
- new version 2.8.2.1

* Fri Dec 29 2006 Ilya Mashkin <oddity@altlinux.ru> 2.8.1.1-alt2
- rebuild with new dbus

* Fri Oct 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.1.1-alt1
- new version 2.8.1.1 (with rpmrb script)

* Tue Sep 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.0-alt1
- Release 2.8.0
- Updated Patch0
- Patch1 has gone upstream

* Fri Sep 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.3-alt1
- Release 2.6.3

* Sun Jul 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt2
- Rebuilt without GStreamer 0.8; no inline audio as of yet

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt1
- Release 2.6.2

* Sat May 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.1-alt1
- Release 2.6.1

* Wed Apr 19 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.0-alt2.1
- Rebuild with dbus-0.61-alt1 .

* Sat Mar 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- x86_64 fix: make sure that %%_libexecdir and %%_libdir are the same

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- Release 2.6.0

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.92-alt2
- Added gnome-icon-theme to the build dependencies
- Patch1: resolve undefined symbols

* Sun Mar 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.92-alt1
- 2.5.92
- Patch1 has gone upstream

* Sat Feb 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.91-alt1
- Updated to 2.5.91
- Removed Debian-style menu
- Patch1: fix a crash on opening a new message composer (GNOME bug 331680)
- Buildreq

* Wed Dec 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.2.1-alt1
- 2.4.2.1
- Gnome Spell GConf key patch from Vital Khilko

* Wed Nov 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.2-alt1
- 2.4.2
- Compile with separately installed libnspr and libnss

* Wed Nov 23 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt2.1
- Spec cosmetics
- Drop explicit nspr/nss configure flags, relying on mozilla .pc files instead

* Sat Oct 22 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt2
- Version required for libsoup bumped to 2.2.6
- Dropped gal dependencies
- Buildreq

* Tue Oct 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Thu Sep 22 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.0-alt2
- Added /usr/bin/evolution symlink (bug 7918)

* Tue Sep 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Aug 26 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Mon Aug 08 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.7-alt0.1
- 2.3.7

* Fri Jul 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.6.1-alt0.1
- Updated to 2.3.6.1

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Thu Mar 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1.1
- put symlinks to libeshell É libeutil in %%_libdir
  so connector can find thease libararies. (reported by Alex Gorbachenko).

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Mon Jan 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt2
- remove 'use diagnostics' from addressbook/tools/csv2vcard.
- don't use setgid for camel-lock-helper.
- fixed CAN-2005-0102.
- requres mozilla, mozilla-psm (#5444).

* Sat Dec 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3
- fixed #5452 (thanks mhz@).

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt0.5
- 2.0.2

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt0.5
- 2.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt0.5
- 2.0.0

* Sun Sep 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.94.1-alt0.5
- new version.

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.92.1-alt0.5
- 1.5.92.1

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.92-alt0.5
- 1.5.92

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.91-alt0.5
1.5.91

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.90-alt0.5
- 1.5.90

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.9.2-alt0.5
- 1.5.9.2

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.9.1-alt0.5
- 1.5.9.1

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.8-alt0.5
- 1.5.8

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.7-alt0.5
- 1.5.7

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.6.2-alt0.5
- 1.5.6.2

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.6-alt0.5
- 1.5.6

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.5-alt0.5
- 1.5.5
- devel subpackage.

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt0.6
- fix build for new krb5 libs location.
- fix buildreqs.

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt0.5
- 1.5.4

* Sat Jan 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.3-alt0.5
- 1.5.3

* Wed Aug 06 2003 AEN <aen@altlinux.ru> 1.4.4-alt1
- new version

* Mon Jul 14 2003 AEN <aen@altlinux.ru> 1.4.3-alt2
- PreReq and BuildPreReq on liborbi2 & libbonobo2 added (thnks to Vyt)

* Fri Jul 11 2003 AEN <aen@altlinux.ru> 1.4.3-alt1
- release

* Tue Jul 08 2003 AEN <aen@altlinux.ru> 1.4.1-alt0.2
- libexecdir fixed

* Thu Jul 03 2003 AEN <aen@altlinux.ru> 1.4.1-alt0.1
- new version from cvs

* Wed Jul 02 2003 AEN <aen@altlinux.ru> 1.4.0-alt2
- wombat patch from mdk

* Mon Mar 31 2003 AEN <aen@altlinux.ru> 1.2.3-alt1
- new version

* Tue Mar 18 2003 AEN <aen@altlinux.ru> 1.2.2-alt2
- security patch

* Sat Feb 15 2003 AEN <aen@altlinux.ru> 1.2.2-alt1
- new version

* Wed Feb 05 2003 AEN <aen@altlinux.ru> 1.2.1-alt3
- new ru.po from CVS added

* Wed Jan 15 2003 AEN <aen@altlinux.ru> 1.2.1-alt2
- requires fixed

* Mon Dec 23 2002 AEN <aen@altlinux.ru> 1.2.1-alt1
- new version

* Mon Dec 02 2002 AEN <aen@altlinux.ru> 1.2.0-alt3
- added Requires on gnome-vfs >= 1.0.5

* Tue Nov 19 2002 AEN <aen@altlinux.ru> 1.2.0-alt2
- fixed permissions

* Mon Nov 18 2002 AEN <aen@altlinux.ru> 1.2.0-alt1
- new version

* Thu Oct 24 2002 AEN <aen@altlinux.ru> 1.0.8-alt3
- scrollkeeper patch from MDK
- build with pilot

* Tue Oct 22 2002 AEN <aen@altlinux.ru> 1.0.8-alt2
- rebuilt with mozilla-1.2a
- pilot temporary disabled

* Mon Jul 01 2002 AEN <aen@logic.ru> 1.0.8-alt1
- new version

* Mon Jun 17 2002 AEN <aen@logic.ru> 1.0.7-alt1
- new version
- patch2 removed

* Wed Jun 05 2002 AEN <aen@logic.ru> 1.0.5-alt3
- rebuild with mozilla-1.0
- patch2 from CVS

* Wed May 15 2002 AEN <aen@logic.ru> 1.0.5-alt2
- enable-file-locking=fcntl

* Mon May 13 2002 AEN <aen@logic.ru> 1.0.5-alt1
- new version

* Tue Mar 26 2002 AEN <aen@logic.ru> 1.0.3-alt1
- new version
- build with external nss

* Wed Mar 13 2002 AEN <aen@logic.ru> 1.0.2-alt3
- *.desktop converted

* Sun Mar 10 2002 AEN <aen@logic.ru> 1.0.2-alt2
- rebuild with static nss-1.1.3

* Mon Feb 04 2002 AEN <aen@logc.ru> 1.0.2-alt1
- new version

* Fri Jan 25 2002 AEN <aen@logic.ru> 1.0.1-alt5
- BuildRequires generated

* Fri Jan 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt4
- Updated buildrequires.

* Thu Jan 17 2002 AEN <aen@logic.ru> 1.0.1-alt3
- requires: gtkhtml added

* Tue Jan 15 2002 AEN <aen@logic.ru> 1.0.1-alt2
- updates russian translation

* Mon Jan 14 2002 AEN <aen@logic.ru> 1.0.1-alt1
- new version
- patches 0-1 removed, patch2 refreshed

* Wed Dec 05 2001 AEN <aen@logic.ru> 1.0-alt1
- release

* Wed Nov 21 2001 AEN <aen@logic.ru> 0.99.2-alt2
- official RC2
- rebuild with new gnome-pilot

* Mon Nov 19 2001 AEN <aen@logic.ru> 0.99.2-alt1
- snapshot

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.99-alt2
- w/o font patch

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.99-alt1
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 0.16-alt0.1
- build snapshot

* Tue Oct 09 2001 AEN <aen@logic.ru> 0.15-alt2
- fonts patch

* Tue Oct 09 2001 AEN <aen@logic.ru> 0.15-alt1
- new version

* Wed Sep 12 2001 AEN <aen@logic.ru> 0.13-alt3
- requires bonobo-conf
* Mon Sep 10 2001 AEN <aen@logic.ru> 0.13-alt2
- i18n patch from MDK

* Fri Sep 07 2001 AEN <aen@logic.ru> 0.13-alt1
- release 0.13

* Wed Sep 05 2001 AEN <aen@logic.ru> 0.13-alt0.1
- snapshot

* Wed Sep 05 2001 AEN <aen@logic.ru> 0.12-alt3
- rebuild with new libgal/gtkhtml
- oaf-slay added to %post

* Tue Aug 23 2001 AEN <aen@logic.ru> 0.12-alt2
- rebuild with new libtool/autoconf

* Thu Aug 09 2001 AEN <aen@logic.ru> 0.12-alt1
- new version
* Wed Jul 24 2001 AEN <aen@logic.ru> 0.11-alt1
- new version
- w/o movemail

* Wed Jul 17 2001 AEN <aen@logic.ru> 0.10.99-alt3
- new snapshot with  gtkhtml-0.10.0

* Thu Jul 12 2001 AEN <aen@logic.ru> 0.10.99-alt2
- new snapshot

* Mon Jul 9 2001 AEN <aen@logic.ru> 0.10.99-alt1
- new version with db-3.1.17

* Thu May 24 2001 AEN <aen@logic.ru> 0.10-alt5
- built cvs version with libgal-0.8 and gtkhtml-0.9.3+
- built w/o pilot, ssl, nspr

* Thu May 17 2001 AEN <aen@logic.ru> 0.10-alt4
- build with pilot support

* Wed May 16 2001 AEN <aen@logic.ru> 0.10-alt3
- charset patch
- ru.po fixed

* Tue May 15 2001 AEN <aen@logic.ru> 0.10-alt2
- %files fixed

* Tue May 15 2001 AEN <aen@logic.ru> 0.10-alt1
- 0.10
* Mon Apr 9 2001 AEN <aen@logic.ru> 0.9-ipl3mdk
- sync with MDK
- rebuild in Gnome-1.4 environment

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9-ipl2mdk
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 AEN <aen@logic.ru> 0.9-ipl1mdk
- 0.9

* Thu Feb 22 2001 AEN <aen@logic.ru> 0.8-ipl3mdk
- build ximean snapsot 2001/02/16

* Thu Feb 22 2001 AEN <aen@logic.ru> 0.8-ipl2mdk
- rebuild with new libraries
- gal-0.5 patch

* Sat Dec 16 2000 AEN <aen@logic.ru>
- 0.8
- adopted for RE
* Thu Nov 16 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-3mdk
- Really remove dependency on old libstdc++

* Sat Nov  4 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6-2mdk
- simple rebuild (new libstdc++)

* Fri Oct 27 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-1mdk
- Release 0.6
- Disable LDAP (OpenLDAP 2.0 not supported yet)

* Mon Sep 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5.1-1mdk
- Release 0.5.1

* Fri Sep 15 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-2mdk
- add missing icons

* Thu Sep 14 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-1mdk
- Release 0.5 (+ merge from Helix 0mdk_helix_1)

* Mon Aug 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.4.1-1mdk
- Release 0.4.1 (merge from Helix 0_helix_1)
- no longer conflict with gnome-pim

* Fri Aug 11 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.3.1-2mdk
- add dependency on gnome-vfs
- add menu entry

* Thu Aug  3 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.3.1-1mdk
- Release 0.3.1
- first mandrake package : BM + macroszification
- Build without GConf

* Sun May 21 2000 Ross Golder <rossigee@bigfoot.com>
- created spec file
