Name: grdesktop
Version: 0.23
Release: alt0.4

Summary: RDP client GUI
License: GPL
Group: Networking/Remote access
Url: http://www.nongnu.org/grdesktop/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2
#Patch0: %name-keypath-patch

# Typical environment for GNOME program
Requires(post): GConf2
BuildPreReq: GConf2
BuildPreReq: desktop-file-utils

# Automatically added by buildreq on Thu Aug 18 2005
BuildRequires: GConf2 ORBit2-devel esound fontconfig freetype2 glib2-devel gnome-vfs2-devel libGConf2-devel libart_lgpl-devel libatk-devel libbonobo2-devel libbonoboui-devel libgnome-devel libgnome-keyring libgnomecanvas-devel libgnomeui-devel libgtk+2-devel libpango-devel libpopt-devel libxml2-devel pkgconfig rdesktop scrollkeeper

Requires: rdesktop

%description
grdesktop is a frontend, written in C using the GTK+ 2 toolkit,
for the remote desktop client (rdesktop) which can be used to
access older RDP implementations (usually Windows app servers).

It can save several connections (including their options),
and browse the network for available terminal servers.

In case [g]rdesktop doesn't work for you, see also remmina.

%prep
%setup
#patch0 -p1
sed -i "s|@GETTEXT_PACKAGE@|@PACKAGE@|g" po/Makefile*
%build
#autoreconf -isfv
%configure --with-keymap-path=%_datadir/rdesktop/keymaps --disable-schemas-install
%make

%install
%makeinstall

# TODO: make a patch and report to upstream 
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=%name
GenericName=Remotedesktop Client
Comment=GTK+2 frontend for rdesktop. Connect to a remote Windows Terminal-Server
Comment[de]=Verbindet zu einem entfernten Windows Terminal-Server
Exec=grdesktop
Icon=grdesktop
Terminal=false
Actions=Full;
Categories=Network;RemoteAccess;

[Desktop Action Full]
Exec=grdesktop
EOF

%find_lang %name --with-gnome
rm -rf %buildroot%_localstatedir/scrollkeeper

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_pixmapsdir/*
#_datadir/locale/*
%_desktopdir/*.desktop
%_datadir/application-registry/*
%_datadir/mime-info/*
%config %_sysconfdir/gconf/schemas/*
%doc AUTHORS ChangeLog NEWS README TODO doc

%changelog
* Sat Jul 23 2011 Michael Shigorin <mike@altlinux.org> 0.23-alt0.4
- reintroduced long lost Requires: rdesktop (closes: #18587)
- tweaked summary and description as well

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.23-alt0.3.qa3
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for grdesktop
  * postclean-03-private-rpm-macros for the spec file

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt0.3.qa2
- NMU: .desktop file cleanup
- BR: cleanup agains new sisyphus_check

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.23-alt0.3.qa1
- NMU (by repocop): the following fixes applied:
  * desktop-mime-entry for grdesktop
  * update_menus for grdesktop
  * obsolete-call-in-post-scrollkeeper-update for grdesktop
  * postclean-05-filetriggers for spec file

* Sun Apr 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt0.3
- remove INSTALL
- set Packager
- remove Debian menu

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt0.2
- NMU: fix bug with locale install

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt0.1
- NMU: new version (GNOME build)
- update spec

* Thu Feb 06 2003 Dmitry Malenko <maldim@altlinux.ru> 0.18-alt3
- Added patch to look for rdesktop keymaps in proper place

* Wed Jan 29 2003 Dmitry Malenko <maldim@altlinux.ru> 0.18-alt2
- Spec cleanup

* Fri Jan 24 2003 Dmitry Malenko <maldim@altlinux.ru> 0.18-alt1
- Packaged for ALT
