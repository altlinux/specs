Name: wallpapoz
Version: 0.6.2
Release: alt1
Group: Graphical desktop/GNOME
License: GPLv2+
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Url: https://vajrasky.wordpress.com/

# Automatically added by buildreq on Sun May 29 2016
# optimized out: python-base python-modules python3 python3-base
BuildRequires: python3-module-yieldfrom

BuildRequires:  python-module-pygtk-libglade python-module-pygtk 
BuildRequires:  python-module-pygnome python-module-imaging


BuildRequires:  xwininfo sh

# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)

Requires:  python-module-pygtk-libglade python-module-pygtk 
Requires:  python-module-pygnome python-module-imaging
Requires:  xwininfo sh

BuildArch: noarch

Summary: Gnome Desktop wallpaper configuration tool

# Source from https://github.com/vajrasky/wallpapoz
Source0: %name-%version-%release.tar
Source10: daemon_wallpapoz-wrapper
Source11: wallpapoz-autostart.desktop

# Install daemon_wallpapoz wrapper script, which may
# fix 584980, 597687?
# and 711541
Source12:	daemon_wallpapoz-wrapper
# Misc fixes for daemon_wallpapoz under compiz working,
# containing fix for bug 531342, 542244, bug 567437, bug 573642
Patch0:         wallpapoz-0.6.1-workspace-num-respawn.patch
# Check if selected item is really a directory when adding directory
# bug 549219
Patch2:         wallpapoz-0.6.1-dircheck.patch
# Avoid backtrace in case no item is selected yet (bug 555181)
Patch3:         wallpapoz-0.4.1-rev92-noitem_selected.patch
# Intialization for pasting selected items
Patch4:         wallpapoz-0.4.1-rev92-paste-initialization.patch
# Kill daemon_wallpapoz when X resource is no longer available
# bug 531343, 538533, 541434, 556377, 569135, 571827
# (and bug 566594)
# (and bug 711541)
Patch5:         wallpapoz-0.6.2-kill-daemon-without-x.patch
# Kill other daemon_wallpapoz if running
Patch6:         wallpapoz-0.6.1-kill-multiple-daemon.patch
# Make wallpapoz gui handle animated image file
# bug 602921
Patch7:		wallpapoz-0.6.1-animated-image.patch
# Non-utf8 directory can return NoneType with filechooser_widget.get_filename
# bug 603351
Patch8:		wallpapoz-0.6.1-nonutf8-directory.patch
# Don't remove a wallpaper from a workspace if there is only one
# wallpaper left.
# bug 567136
# Also some fixes about gtk menu sensitive issue (after doing some movement
# for wallpapers)
Patch9:		wallpapoz-0.6.1-delete-one-wallpaper.patch
# Fix backtrace when deleting first element in desktop (not workspace) mode
# bug 597959
Patch10:	wallpapoz-0.6.1-delete-first-in-desktop-mode.patch
# Port to gsettings
#Patch11:	wallpapoz-0.5-gsettings.patch
# At startup, wallpapoz will try to show workspace name as "images"
Patch12:	wallpapoz-0.5-startup-warn-about-workspace-name.patch
# Fix backtrace when switching from desktop style XML to workspace style one
# with workspace number increased
# bug 708769
Patch13:	wallpapoz-0.6.1-switch-from-wallpaper-to-desktop-with-workspace-increase.patch
# Return to set default WM to GNOME3 when proper WM is not found
# (bug 857587)
Patch14:	wallpapoz-0.6.2-wm-return-to-default.patch
# Don't import Image directory and import PIL instead for
# F-19 Pillow conversion
# (bug 895217)
Patch15:	wallpapoz-0.6.2-import-PIL-for-Image.patch
# Support LXDE
Patch16:	wallpapoz-0.6.2-LXDE.patch
# Support MATE
# https://bugzilla.redhat.com/show_bug.cgi?id=1029554#c31
# https://bugzilla.redhat.com/show_bug.cgi?id=1029554#c38
Patch17:	wallpapoz-0.6.2-MATE.patch
# Support CINNAMON
# https://bugzilla.redhat.com/show_bug.cgi?id=1029554#c44
Patch18:	wallpapoz-0.6.2-CINNAMON.patch



%description
Wallpapoz application enables you to configure Gnome desktop wallpapers
in unique way. You could have Gnome desktop wallpaper changes when the
specified time has passed.


%prep
%setup -n %name-%version-%release

%patch0 -p1 -b .respawn
%patch2 -p1 -b .dircheck
%patch3 -p1 -b .noitem
%patch4 -p1 -b .patch_init
%patch5 -p1 -b .kill_nox
%patch6 -p1 -b .kill_multi
%patch7 -p1 -b .anime
%patch8 -p1 -b .nonutf8
%patch9 -p1 -b .deletelastone
%patch10 -p1 -b .deletefirst
%patch12 -p1 -b .workspace_img
%patch13 -p1 -b .workspace_num_incr
%patch14 -p1 -b .default
%patch15 -p1 -b .pil
%patch16 -p1 -b .LXDE
%patch17 -p1 -b .MATE
%patch18 -p1 -b .CINNAMON

# Umm... permission fix
find . -type f -print0 | xargs -0 chmod 0644
grep -rl --null '#!/usr/bin' . | xargs -0 chmod 0755

# For setup
mkdir TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true xwininfo
popd

# Install C gnome help documents (bug 651522)
ln -sf c share/gnome/help/wallpapoz/C

%install
mkdir -p %buildroot%prefix

./setup.py install --installdir %buildroot%prefix

install -dp -m755 %buildroot%_libexecdir
mv %buildroot%_bindir/daemon_wallpapoz \
	%buildroot%_libexecdir
install -p -m755 %SOURCE10 \
	%buildroot%_bindir/daemon_wallpapoz

install -dp -m755 %buildroot%_sysconfdir/xdg/autostart

install -p -m644 %SOURCE11  %buildroot%_sysconfdir/xdg/autostart 

%find_lang %name --with-gnome

%files -f %name.lang
%doc README CHANGELOG
%_bindir/daemon_wallpapoz
%_bindir/wallpapoz
%_bindir/launcher_wallpapoz.sh
%_libexecdir/daemon_wallpapoz
%_datadir/wallpapoz
%_datadir/pixmaps/wallpapoz.png
%_datadir/applications/wallpapoz.desktop
%_sysconfdir/xdg/autostart/wallpapoz-autostart.desktop
%_datadir/gnome/help/%name/


%changelog
* Mon May 30 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.2-alt1
- New Version

* Sat May 28 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.6.2-alt1.git932c
- Update from https://github.com/vajrasky/wallpapoz

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.svn20100424.1
- Rebuild with Python-2.7

* Sat Apr 24 2010 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.1-alt1.svn20100424
- Build for ALTLinux

* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.1-5mdv2010.0
+ Revision: 445731
- rebuild
