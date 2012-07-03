Name: rpm-build-gnome
Version: 2.0
Release: alt2

Summary: RPM macros and helper scripts for GNOME packages building
License: %gpl3plus
Group: Development/GNOME and GTK+

BuildArch: noarch

BuildPreReq: rpm-build-licenses

%description
This package contains RPM macros and helper scripts that ease labour of a maintainer of GNOME packages.

%install
cat <<__EOF__ >gnome.rpmmacros
%%gnome_ftp ftp://ftp.gnome.org/pub/gnome/sources
%%gconf_schemasdir %%_sysconfdir/gconf/schemas
%%gnome_helpdir %%_datadir/gnome/help
%%nautilus_extdir %%_libdir/nautilus/extensions-3.0
%%gnome_appletsdir %%_libdir/gnome-applets
%%gedit_pluginsdir %%_libdir/gedit/plugins
%%gnome_autostartdir %%_datadir/gnome/autostart
%%_omfdir %%_datadir/omf

# deprecated
%%gnome_vfsmodulesdir %%_libdir/gnome-vfs-2.0/modules
%%gnomevfs_modulesdir %%gnome_vfsmodulesdir
%%_sklocalstatedir %%_localstatedir/scrollkeeper
%%gnomehelpdir %%gnome_helpdir
%%bonobo_serversdir %%_libdir/bonobo/servers
__EOF__
install -D -m644 gnome.rpmmacros %buildroot/%_rpmmacrosdir/gnome

%files
%_rpmmacrosdir/gnome

%changelog
* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt2
- restored %%bonobo_serversdir

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- Updated macros for GNOME 3

* Fri Jun 19 2009 Alexey Rusakov <ktirf@altlinux.org> 1.0-alt1
- Moved the macros file from %%_sysconfdir/rpm/macros.d to %%_rpmmacrosdir
  (where it should should reside).

* Sat Apr 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.9-alt1
- Updated %%nautilus_extdir macro for GNOME 2.22.

* Mon Jan 07 2008 Alexey Rusakov <ktirf@altlinux.org> 0.8.1-alt1
- Renamed %%gnomehelpdir to %%gnome_helpdir, according to ALT Bug #13919.
  %%gnomehelpdir is still available, but deprecated.

* Sat Jan 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.8-alt1
- added %%_omfdir and (deprecated) %%_sklocalstatedir for compatibility
  with Scrollkeeper.

* Mon Nov 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7-alt1
- added %%gnome_autostartdir

* Mon Jul 23 2007 Alexey Rusakov <ktirf@altlinux.org> 0.6-alt1
- added %%gedit_pluginsdir

* Sun Jul 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.5-alt1
- added %%gconf_schemasdir

* Sat Jul 07 2007 Alexey Rusakov <ktirf@altlinux.org> 0.4-alt1
- added %%bonobo_serverdir and %%gnome_appletsdir macros, for GNOME applets.
- deprecated %%gnomevfs_modulesdir in favor of %%gnome_vfsmodulesdir.

* Mon Jul 02 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt1
- added %%gnomevfs_modulesdir macro.

* Sat Jun 30 2007 Alexey Rusakov <ktirf@altlinux.org> 0.2-alt1
- added a macro for the path to nautilus extensions;
- fixed %%_datadir accidentally expanded in the definition of %%gnomehelpdir

* Thu May 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.1-alt1
- Initial Sisyphus build
- Contains a very useful macro: GNOME FTP site shortcut :)

