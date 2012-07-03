Name: xfce4-quicklauncher-plugin
Version: 1.9.4
Release: alt4

Summary: Quicklauncher plugin for XFce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar

# http://bugzilla.xfce.org/show_bug.cgi?id=7015
Patch0: xfce4-quicklauncher-plugin-1.9.4-alt-panel-4.8.patch

# From Fedora:
# make new apps appear on the correct X screen
# http://bugzilla.xfce.org/show_bug.cgi?id=4323
Patch1: xfce4-quicklauncher-plugin-1.9.4-fix-multiscreen.patch
# apply settings without restart
# http://bugzilla.xfce.org/show_bug.cgi?id=3782
Patch2: xfce4-quicklauncher-plugin-1.9.4-save-settings.patch
# Update translations, no french language by default.
# http://bugzilla.xfce.org/show_bug.cgi?id=3783
Patch3: xfce4-quicklauncher-plugin-1.9.4-update-translations.patch
# xfce4-settings-manager instead of xfce-setting-show
# http://bugzilla.xfce.org/show_bug.cgi?id=5752
Patch4: xfce4-quicklauncher-plugin-1.9.4-xfce4-settings-manager.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel >= 4.8.0

%description
This plugin allows you to have lots of launchers in the Xfce panel,
displaying them on several lines.

%prep
%setup
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p0

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc ChangeLog TODO AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt4
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt3
- Rebuild with xfce4-panel-4.9.

* Tue Feb 01 2011 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt2
- Spec updated, tar.bz2 -> tar.
- Fix settings manager name.
- Update translations, no french language by default.
- Apply settings without restart.
- Make new apps appear on the correct X screen.
- Patch for xfce4-panel >= 4.8.
- Drop watch file.

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.9.4-alt1
- new version
- add watch file

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.81-alt1
- First build for Sisyphus.

