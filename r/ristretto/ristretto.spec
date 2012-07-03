Summary: Ristretto is an image-viewer for the Xfce Desktop Environment
Name: ristretto
Version: 0.6.0
Release: alt2
License: %gpl2plus
Url: http://goodies.xfce.org/projects/applications/ristretto/

# Upstream: git://git.xfce.org/apps/ristretto
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Group: Graphical desktop/XFce
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-devel libxfce4util-devel libThunar-devel libxfconf-devel
# For exo-csource (needed in maintainer mode)
BuildPreReq: libexo-devel
BuildRequires: intltool libdbus-glib-devel libexif-devel libcairo-devel

%description
Ristretto is a fast and lightweight image-viewer for the Xfce desktop
environment.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Thu Jun 07 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2
- Fix segfault when image-quality property is changed (from upstream).

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Updated to 0.6.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Tue Jan 17 2012 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Build documentation again.
- Updated to 0.3.2.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Thu Nov 17 2011 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2
- Build documentation.

* Mon Nov 14 2011 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Fri Oct 21 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Oct 13 2011 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Drop obsoleted patch.
- Updated to 0.1.1.

* Thu Mar 17 2011 Mikhail Efremov <sem@altlinux.org> 0.0.93-alt1
- Add patches from upstream:
    + Fix opening of directories from the command-line.
    + Include string.h in thumbnailer.c.
- Drop dsofix.patch (fixed in upstream).
- Updated to 0.0.93.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.0.91-alt1
- Fix DSO linking (patch from Fedora).
- Spec updated, tar.gz -> tar.
- Drop watch file.
- Updated to 0.0.91.

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 0.0.21-alt2
- fix build, update requires

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.21-alt1
- new version

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.19-alt1
- new version

* Mon Jan 28 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.16-alt1
- new version

* Wed Dec 26 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.0.15-alt1
- first build for Sisyphus

