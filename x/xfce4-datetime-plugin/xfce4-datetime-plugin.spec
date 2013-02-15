Name: xfce4-datetime-plugin
Version: 0.6.2
Release: alt1

Summary: Datetime plugin for the XFce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util
# Automatically added by buildreq on Sat Jan 05 2008
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel >= 4.8

%description
%name is the datetime plugin for the XFce panel.

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
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Fri Feb 15 2013 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Drop remained USE_GTK_TOOLTIP_API.
- Drop obsoleted patches.
- Updated to 0.6.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt4
- Fix build: Replace BM_DEBUG_SUPPOR with XDT_FEATURE_DEBUG.
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt3
- Rebuild with xfce4-panel-4.9.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt2
- Fix plugindir path for xfce4-panel >= 4.8.
- Fix desktop file path for xfce4-panel >= 4.8.
- Remove watch file.
- Port to libxfce4ui.
- Spec updated, tar.bz2 -> tar.
- Add patches from Fedora.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.1-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt1
- new version
- add watch file

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.1-alt2
- Rebuilt with new xfce4-panel.

* Sat Dec 25 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Thu Feb 05 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt2
- Fixed BuildRequires.

* Mon Feb 02 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2-alt1
- 0.2

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
