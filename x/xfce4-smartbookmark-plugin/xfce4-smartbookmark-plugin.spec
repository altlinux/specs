Name: xfce4-smartbookmark-plugin
Version: 0.4.4
Release: alt2

Summary: Smart bookmarks for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel

BuildRequires: intltool libXt-devel libgtk+2-devel perl-XML-Parser xorg-cf-files

Requires: xfce4-panel >= 4.8

%description
A plugin which allows you to do a search directly on Internet on sites
like Google or ALT Linux Bugzilla. It allows you to send requests
directly to your browser and perform custom searches.

%prep
%setup
%patch -p1

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
%doc README ChangeLog AUTHORS
%_libdir/xfce4/panel-plugins/*.so
%exclude %_libdir/xfce4/panel-plugins/*.la
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Feb 06 2012 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Use ALT bugzilla link instead of Debian's.
- Fix location of the desktop file.
- Updated to 0.4.4.

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- First build for Sisyphus.

