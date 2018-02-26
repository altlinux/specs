Name: xfce4-eyes-plugin
Version: 4.4.1
Release: alt3

Summary: Eyes plugin for XFce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel libxfce4util-devel
BuildRequires: intltool libxml2-devel

Requires: xfce4-panel >= 4.8

%description
Eyes is a xfce4 panel plugin that adds eyes which watch your every step.
Scary!

%prep
%setup 

%build
# Fix desktop file path for xfce4-panel >= 4.8
sed -i 's|^desktopdir = \$(datadir)/xfce4/panel-plugins|desktopdir = \$(datadir)/xfce4/panel/plugins|' \
   panel-plugin/Makefile.am

%xfce4reconf
%configure \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc ChangeLog README AUTHORS
%_libexecdir/xfce4/panel-plugins/%name
%_datadir/xfce4/eyes/
%_datadir/xfce4/panel/plugins/*.desktop
%_liconsdir/*.png

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 4.4.1

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt1
- new version
- add watch file

* Mon Dec 18 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.3.0-alt1
- First build for Sisyphus.

