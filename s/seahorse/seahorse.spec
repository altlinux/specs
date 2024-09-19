%def_disable snapshot

%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%define ver_major 47
%define beta %nil
%define xdg_name org.gnome.seahorse

%def_disable debug
%def_enable ldap
%def_enable hkp
%def_enable gnome_keyring
%def_enable pkcs11
%def_enable ssh
%def_enable introspection
%def_enable man

%if_enabled hkp
# disabled by default and will possibly be removed in the future
%def_disable sharing
%endif

Name: seahorse
Version: %ver_major.0.1
Release: alt1%beta

Summary: A password and encryption key manager
License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Seahorse

Vcs: https://gitlab.gnome.org/GNOME/seahorse.git

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.66
%define gtk_ver 3.24
%define soup3_ver 3.0.0
%define secret_ver 0.16
%define avahi_ver 0.6
%define gcr_ver 3.38
%define gpgme_ver 1.14
%define handy_ver 1.5.0
%define gnupg_ver 2.4.0

Requires: dconf
Requires: gnupg2 > %gnupg_ver gcr >= %gcr_ver
Requires: pinentry-x11
%{?_enable_ssh:Requires: openssh-clients}
%{?_enable_sharing:Requires: avahi-daemon}

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson yelp-tools libappstream-glib-devel
BuildRequires: gtk-doc desktop-file-utils
BuildRequires: gcc-c++ glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: gnupg2 >= %gnupg_ver
BuildRequires: libgpgme-devel >= %gpgme_ver
BuildRequires: libgpg-error-devel
BuildRequires: vala-tools
BuildRequires: pkgconfig(pwquality)
%{?_enable_ldap:BuildRequires: libldap-devel}
%{?_enable_hkp:BuildRequires: libsoup3.0-devel >= %soup3_ver}
%{?_enable_gnome_keyring:BuildRequires: libsecret-devel >= %secret_ver}
%{?_enable_pkcs11:BuildRequires: gcr-libs-devel >= %gcr_ver gcr-libs-vala}
%{?_enable_sharing:BuildRequires:libsoup3.0-devel >= %soup3_ver libavahi-glib-devel >= %avahi_ver libavahi-devel}
%{?_enable_ssh:BuildRequires: openssh openssh-clients}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_man:BuildRequires: xsltproc docbook-dtds docbook-style-xsl}

%description
Seahorse is a password and encryption key manager for GNOME desktop.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{subst_enable_meson_bool ldap ldap-support} \
    %{subst_enable_meson_bool pkcs11 pkcs11-support} \
    %{subst_enable_meson_bool hkp hkp-support} \
    %{subst_enable_meson_bool sharing key-sharing} \
    %{subst_enable_meson_bool man manpage}
%nil
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/ssh-askpass
%_libexecdir/%name/xloadimage
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/*/*.*
%_desktopdir/*.desktop
%{?_enable_man:%_man1dir/*}
%_datadir/dbus-1/services/org.gnome.seahorse.Application.service
%_datadir/gnome-shell/search-providers/seahorse-search-provider.ini
%config %_datadir/glib-2.0/schemas/org.gnome.seahorse.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.seahorse.manager.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.seahorse.window.gschema.xml
%_datadir/metainfo/%{xdg_name}*.appdata.xml
%doc NEWS README* THANKS

%changelog
* Wed Sep 18 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0.1-alt1
- 47.0.1

* Wed Aug 16 2023 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt3
- updated to 43.0-15-g034ddf2b (fixed build with GnuPG-2.4.x)

* Thu Feb 09 2023 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt2
- 43.0-6-g9260c747 (updated translations)

* Fri Oct 14 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sat May 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0
- enabled LTO

* Wed Sep 29 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sat Aug 28 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt2
- updated to 40.0-8-g6f799c36
- disabled LTO

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Mon Feb 15 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Nov 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0.1-alt1
- 3.38.0.1

* Sun Aug 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.37.2-alt1
- 3.37.2

* Sat Jun 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- updated to 3.36.2-1-ge5bac093

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36-alt1
- 3.36

* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Oct 01 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34-alt1
- 3.34

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1
- enabled ldap support

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32-alt1
- 3.32

* Tue Feb 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.91-alt1
- 3.31.91

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1.1-alt1
- 3.30.1.1

* Fri Oct 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30-alt2
- fixed regression where progress window is not shown, see
  https://gitlab.gnome.org/GNOME/seahorse/issues/108 (ALT #35231)

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30-alt1
- 3.30

* Wed May 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- updated to 3.20.0-312-g77df305 from master branch, 3.20 totally obsolete

* Fri Mar 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sat Sep 05 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.4-alt1
- 3.17.4

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Apr 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.92-alt1
- 3.15.92
- built with gpg, not gpg2, due to incompatible upstream changes

* Wed Mar 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.90-alt1
- 3.15.90

* Sat Feb 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Jan 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Thu Oct 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Tue Oct 23 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- updated from upstream git (7fafa3ccd)

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Thu Apr 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 30 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Fri Oct 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Sep 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4
- new gir{,-devel} subpackages

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Thu Jul 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- fix build against gpgme with LFS (tnx gentoo)
- fixed http://bugzilla.gnome.org/show_bug.cgi?id=583356

* Thu May 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Wed May 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt3
- requires gnupg2-gpg not gnupg2

* Thu Apr 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- use gnupg2
- requires avahi-daemon if sharing enabled

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92
- removed obsolete %%post{,un} scripts
- updated buildreqs
- enabled ldap support
- new libseahorse-devel-doc noarch subpackage

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)
- cleanup configure options

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for seahorse
 * update_menus for seahorse

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Sun Mar 23 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.3-alt1
- new version (2.20.3)
- add Packager
- update License
- fix files (for find_lang)

* Mon Dec 03 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add package epiphany-extension-seahorse (build with firefox gecko), but disabled build default
- move found %%name.lang to main package

* Fri Jul 27 2007 Alexey Rusakov <ktirf@altlinux.org> 1.0.1-alt2
- added libSM-devel to buildreqs
- use macros from rpm-build-gnome

* Mon Apr 30 2007 Alexey Rusakov <ktirf@altlinux.org> 1.0.1-alt1
- new version (1.0.1)
- updated dependencies

* Wed Mar 14 2007 Alexey Rusakov <ktirf@altlinux.org> 1.0-alt1
- new version (1.0)
- enabled cryptui tests building

* Thu Mar 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.92-alt1
- new version 0.9.92 (with rpmrb script)

* Sat Feb 17 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.91-alt1
- new version 0.9.91 (with rpmrb script)

* Sat Jan 27 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.10-alt4
- Another replacement of %%_libexecdir with %%_libdir.

* Fri Jan 26 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.10-alt3
- %%_libdir instead of %%_libexecdir in libseahorse, to fix building on x86_64.

* Sun Jan 07 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.10-alt2
- added def_enable debug, enabled by default.
- minor update of buildreqs.
- fixed insufficient buildreqs and reqs (openssh-clients was missed out)

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.10-alt1
- new version (0.9.10)

* Tue Jan 02 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.9-alt2
- no more manual setup of seahorse-agent necessary, the appropriate script is
  installed to /etc/X11/profile.d/ directory.
- seahorse-agent replaces gpg-agent functionality, a warning about this is put
  into %%post script.

* Sun Dec 24 2006 Alexey Rusakov <ktirf@altlinux.org> 0.9.9-alt1
- new version (0.9.9)
- removed a patch that fixes linking, as it is not correct anymore (wonder why
  it still applies)
- files list updated
- enabled _unpackaged_files_terminate_build macro

* Thu Apr 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.9.1-alt1
- new version

* Mon Apr 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.9.0-alt1
- new version (0.9.0)
- removed Debian menu support
- updated dependencies
- introduced many switches, to control various Seahorse features.
- for backporters: older gedit is supported again.

* Tue Jan 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.8-alt1
- new version

* Tue Oct 25 2005 Sir Raorn <raorn@altlinux.ru> 0.7.9-alt2
- Fix gedit requirements

* Sat Aug 27 2005 Sir Raorn <raorn@altlinux.ru> 0.7.9-alt1
- [0.7.9]

* Mon May 23 2005 Sir Raorn <raorn@altlinux.ru> 0.7.8-alt1
- [0.7.8]

* Tue Oct 19 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.3-alt1.1
- Updated build dependencies (libgpgme-compat-devel).

* Wed May 12 2004 Sir Raorn <raorn@altlinux.ru> 0.6.3-alt1
- [0.6.3]

* Tue Jun 12 2001 AEN <aen@logic.ru> 0.5.0-alt1
- 0.5.0
- russian po-file fixed

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 0.4.9-ipl1mdk
- RE adaptions.

* Mon Jan 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9-1mdk
- updated to 0.4.9

* Fri Sep 15 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.6-2mdk
- macros
- bm
- menu

* Mon Apr 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.6-1mdk
- fix group
- used srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Sun Mar 19 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.3.6
- specfile changes for spec-helper

* Fri Feb 11 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources
- bzip manpages




