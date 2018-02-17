%define _unpackaged_files_terminate_build 1
%define theme_virt_dir lxde

%define theme_name upstream
#define theme_version 0.1

%define theme_fullname lxde-settings-%theme_name
%define gtkver 2
Name: lxde-common
Version: 0.99.2
Release: alt3
BuildArch: noarch

Summary: Basic infrastructure for LXDE.
License: %gpl2plus
Group: Graphical desktop/Other
Url: https://git.lxde.org/gitweb/?p=lxde/lxde-common.git
BuildArch: noarch

Source: %name-%version.tar
Source1: lxde.wm
Source2: panel
Patch: keybinding.patch

AutoReq: yes,nosymlinks

Requires: lxde-settings
Requires: wm-common-freedesktop
# Automatically added by buildreq on Sat May 21 2016
# optimized out: perl perl-Encode perl-XML-Parser python-base python-modules xml-common xml-utils
BuildRequires: docbook-dtds xsltproc

BuildPreReq: rpm-build-licenses intltool libgtk+%gtkver-devel

%description
Pprovides infrastructure for LXDE components

%package -n %theme_fullname
#Version: theme_version
Summary: provides unmodified LXDE configuration from upstream
Group: Graphical desktop/Other
Provides: lxde-settings

### GRRRR!!! for appliance-desktop-lxde
Provides: lxde-default-theme

%description -n %theme_fullname
Default graphics theme for LXDE.

This package contains unmodified configuration from upstream.

%prep
%setup
%patch -p1

%build
sed -i 's,lxde.conf,LXDE.conf,' Makefile.am
sed -i 's,XDG_CONFIG_HOME/pcmanfm,XDG_CONFIG_HOME/pcmanfm/LXDE,;s,pcmanfm/LXDE.conf,pcmanfm/lxde.conf,;s,default/LXDE.conf,pcmanfm.conf,;' startlxde.in
sed -i '/XDG_MENU/ a\\n# Since shared-mime-info-0.90-alt3 XDG_DATA_DIRS not exported. We need to define\n# the set of base directories explicitly.\nexport XDG_DATA_DIRS="/usr/share/lxde:/usr/share:/usr/local/share"' startlxde.in

%autoreconf
%configure --enable-man

%make_build

%install
%makeinstall_std

install -m644 -D %SOURCE1 %buildroot%_x11sysconfdir/wmsession.d/09LXDE

mv %buildroot%_datadir/lxde %buildroot%_datadir/%theme_fullname
mkdir -p %buildroot%_datadir/%theme_fullname/pcmanfm
mv %buildroot%_sysconfdir/xdg/pcmanfm/LXDE/pcmanfm.conf %buildroot%_datadir/%theme_fullname/pcmanfm/lxde.conf
mv %buildroot%_sysconfdir/xdg/lxsession/LXDE/desktop.conf %buildroot%_datadir/%theme_fullname
mkdir -p %buildroot%_datadir/%theme_fullname/openbox
mv %buildroot%_sysconfdir/xdg/openbox/LXDE/* %buildroot%_datadir/%theme_fullname/openbox
rm -fR %buildroot%_sysconfdir/xdg/openbox/LXDE
mkdir -p %buildroot%_datadir/%theme_fullname/lxpanel
mv %buildroot%_sysconfdir/xdg/lxpanel/LXDE/* %buildroot%_datadir/%theme_fullname/lxpanel
rm -fR %buildroot%_sysconfdir/xdg/lxpanel/LXDE
ln -s %_datadir/%theme_virt_dir/desktop.conf %buildroot%_sysconfdir/xdg/lxsession/LXDE/desktop.conf
ln -s %_datadir/%theme_virt_dir/pcmanfm/lxde.conf %buildroot%_sysconfdir/xdg/pcmanfm/LXDE/pcmanfm.conf
ln -s %_datadir/%theme_virt_dir/pcmanfm/lxde.conf %buildroot%_sysconfdir/xdg/pcmanfm/LXDE/lxde.conf
ln -s %_datadir/%theme_virt_dir/lxpanel/ %buildroot%_sysconfdir/xdg/lxpanel/LXDE
ln -s %_datadir/%theme_virt_dir/openbox %buildroot%_sysconfdir/xdg/openbox/LXDE

mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme_fullname << __EOF__
%_datadir/%theme_virt_dir %_datadir/%theme_fullname 1
__EOF__

# Install desktop files
mkdir -p %buildroot%_desktopdir/
cp -v debian/*.desktop %buildroot%_desktopdir/

#Install panel config
install -m644 %SOURCE2 %buildroot%_datadir/%theme_fullname/lxpanel/panels/

%find_lang %name

%pre
if [ -d %_datadir/lxpanel/profile/LXDE ] && [ ! -L %_datadir/lxpanel/profile/LXDE ] ; then
 rm -fR %_datadir/lxpanel/profile/LXDE
fi

rm -fR %_sysconfdir/xdg/lxsession/LXDE/desktop.conf \
       %_sysconfdir/xdg/pcmanfm/LXDE \
       %_sysconfdir/xdg/lxpanel/LXDE \
       %_sysconfdir/xdg/openbox/LXDE    

%files -f %name.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_x11sysconfdir/wmsession.d/*
%_sysconfdir/xdg/*
%dir %_datadir/xsessions
%_datadir/xsessions/*.desktop
%_man1dir/*

%_desktopdir/*.desktop

%files -n %theme_fullname
%_sysconfdir/alternatives/packages.d/%theme_fullname
%_datadir/%theme_fullname

#_iconsdir/nuoveXT2

%changelog
* Sat Feb 17 2018 Anton Midyukov <antohami@altlinux.org> 0.99.2-alt3
- Replacement screengrab to screenshot-tool.

* Tue Aug 01 2017 Anton Midyukov <antohami@altlinux.org> 0.99.2-alt2
- Added keybinding.patch
- Added requires screengrab.

* Wed Jan 11 2017 Anton Midyukov <antohami@altlinux.org> 0.99.2-alt1
- New version 0.99.2

* Fri Nov 25 2016 Anton Midyukov <antohami@altlinux.org> 0.99.1-alt4
- Added volume control on the panel.

* Wed Jun 29 2016 Anton Midyukov <antohami@altlinux.org> 0.99.1-alt3
- Replace config files to /usr/share/lxde
- Fix config panel.

* Thu May 26 2016 Anton Midyukov <antohami@altlinux.org> 0.99.1-alt2
- Added xkb-switch on the panel. 

* Sat May 21 2016 Anton Midyukov <antohami@altlinux.org> 0.99.1-alt1
- New version 0.99.1
- Fix unowned files.

* Tue Feb 26 2013 Andrey Cherepanov <cas@altlinux.org> 0.5.5-alt18
- Add desktop files for logout and screen lock
- Fix black wallpaper by default
- Fix first run of PCManFM fail
- Mark configuratin files as config files

* Sun Jan 20 2013 Michael Shigorin <mike@altlinux.org> 0.5.5-alt17
- changed wmsession priority from 20 to 09 (closes: #28393)

* Tue May 22 2012 Radik Usupov <radik@altlinux.org> 0.5.5-alt16
- Updated lxde-icon-theme

* Mon Sep 05 2011 Radik Usupov <radik@altlinux.org> 0.5.5-alt15
- Fixed export XDG_DATA_DIRS, thanks naf@! (closes: #26223)

* Mon May 30 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt14
- starting pcmanfm with --daemon-mode (closes: #25687)

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt13
- added /usr/share/lxde to XDG_DATA_DIRS

* Sun Apr 17 2011 Radik Usupov <radik@altlinux.org> 0.5.5-alt12
- added requires (Closes: 25305)

* Thu Mar 03 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt11
- upstream changes merged
- fixed handling of pcmanfm config (closes: #24549)

* Wed Dec 01 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt10
- libfm.conf handling

* Thu Sep 02 2010 Radik Usupov <radik@altlinux.org> 0.5.5-alt9
- package is now noarch

* Wed May 05 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt8
- stupid error fixed

* Wed May 05 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt7.1
- spec cleanup

* Wed May 05 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt7
- package layout revisited to allow concurrent branding packages

* Tue May 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt1
- new upstream version

* Sun May 02 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt7
- graphical theme updated

* Mon Dec 28 2009 Nick S. Grechukh <gns@altlinux.ru> 0.5.0-alt5
- default configs updated

* Tue Dec 22 2009 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt4
- icon-theme in separated tarball

* Sun Dec 13 2009 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt2
- fixed lxsession crash while trying to autorun

* Sat Dec 12 2009 Nick S. Grechukh <gns@altlinux.ru> 0.5.0-alt1
- new version

* Fri Jul 24 2009 Nick S. Grechukh <gns@altlinux.org> 0.4.1-alt3
- openbox / lxpanel configs fixed

* Wed May 20 2009 Nick S. Grechukh <gns@altlinux.org> 0.4.1-alt2
- Packager fixed

* Tue May 19 2009 Nick S. Grechukh <gns@altlinux.org> 0.4.1-alt1
- new version

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2.1-alt2
- Change default terminal emulator to lxde-lxterminal
- remove obsoletes %%update_menu and %%update_wms macros

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2.1-alt1
- First version of RPM package for Sisyphus.
