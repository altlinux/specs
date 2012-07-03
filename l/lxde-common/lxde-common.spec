%define _unpackaged_files_terminate_build 1
%define theme_virt_dir lxde

%define theme_name upstream
#define theme_version 0.1

%define theme_fullname lxde-settings-%theme_name

Name: lxde-common
Version: 0.5.5
Release: alt16
BuildArch: noarch

Summary: Basic infrastructure for LXDE.
License: %gpl2plus
Group: Graphical desktop/Other
Url: http://lxde.sf.net
BuildArch: noarch

Source: %name-%version.tar.bz2
Source1: lxde.wm

AutoReq: yes,nosymlinks

Requires: lxde-settings
Requires: wm-common-freedesktop

# Automatically added by buildreq on Wed May 05 2010
BuildRequires: docbook-dtds docbook-style-xsl xsltproc
BuildPreReq: rpm-build-licenses

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

%build
sed -i 's,lxde.conf,LXDE.conf,' Makefile.am
sed -i 's,XDG_CONFIG_HOME/pcmanfm,XDG_CONFIG_HOME/pcmanfm/LXDE,;s,pcmanfm/LXDE.conf,pcmanfm/lxde.conf,;s,default/LXDE.conf,pcmanfm.conf,;' startlxde.in
sed -i '/XDG_MENU/ a\\n# Since shared-mime-info-0.90-alt3 XDG_DATA_DIRS not exported. We need to define\n# the set of base directories explicitly.\nexport XDG_DATA_DIRS="/usr/share/lxde:/usr/share:/usr/local/share"' startlxde.in
sed -i 's,pcmanfm --desktop,pcmanfm --daemon-mode --desktop,' autostart

%autoreconf
%configure --enable-man

%make_build

%install
%makeinstall_std

install -m644 -D %SOURCE1 %buildroot%_x11sysconfdir/wmsession.d/20LXDE

pushd %buildroot%_datadir

mv lxde %theme_fullname

mv %buildroot%_sysconfdir/xdg/lxsession/LXDE/desktop.conf %theme_fullname
ln -s %_datadir/%theme_virt_dir/desktop.conf %buildroot%_sysconfdir/xdg/lxsession/LXDE/desktop.conf

mkdir %theme_fullname/pcmanfm
mkdir %theme_fullname/pcmanfm/LXDE
mv %buildroot%_sysconfdir/xdg/pcmanfm/LXDE/pcmanfm.conf %theme_fullname/pcmanfm/LXDE/lxde.conf
ln -s %_datadir/%theme_virt_dir/pcmanfm/LXDE/lxde.conf %buildroot%_sysconfdir/xdg/pcmanfm/LXDE/

mv lxpanel/profile/LXDE %theme_fullname/lxpanel
ln -s ../../%theme_virt_dir/lxpanel lxpanel/profile/LXDE
popd

mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme_fullname << __EOF__
%_datadir/%theme_virt_dir %_datadir/%theme_fullname 1
__EOF__

%find_lang %name

%pre
if [ -d %_datadir/lxpanel/profile/LXDE ] && [ ! -L %_datadir/lxpanel/profile/LXDE ] ; then
 rm -fR %_datadir/lxpanel/profile/LXDE
fi

%files -f %name.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_x11sysconfdir/wmsession.d/*
%_sysconfdir/xdg/lxsession/LXDE/autostart
%_datadir/xsessions/*.desktop
%_man1dir/*
### themeable
%_sysconfdir/xdg/lxsession/LXDE/desktop.conf
%_sysconfdir/xdg/pcmanfm/LXDE/lxde.conf
%_datadir/lxpanel/profile/LXDE

%files -n %theme_fullname
%config /etc/alternatives/packages.d/%theme_fullname
%_datadir/%theme_fullname

#_iconsdir/nuoveXT2

%changelog
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
