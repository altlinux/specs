Name: xfce4-mixer
Version: 4.18.1
Release: alt1

Summary: A volume control application and plugin for the Xfce panel
License: GPL-2.0+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/apps/xfce4-mixer/start
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: https://gitlab.xfce.org/apps/xfce4-mixer.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools >= 0.1.1-alt1
BuildRequires: intltool
BuildRequires: libxfce4ui-gtk3-devel libxfce4util-devel libxfconf-devel
BuildRequires: libxfce4panel-gtk3-devel >= 4.14.0
BuildRequires: gstreamer1.0-devel libkeybinder3-devel
BuildRequires: libpulseaudio-devel libalsa-devel

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
This package contains a volume control application based on GStreamer written
to conceptually fit into the Xfce desktop environment. It includes a plugin for
the Xfce panel.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfce4_mixer_version_tag configure.ac.in
%xfce4reconf
%configure \
	--with-host=linux \
	--enable-keybinder=yes \
	--enable-pulse \
	--disable-oss \
	--enable-alsa \
	--disable-sndio \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS
%_bindir/*
%_libdir/xfce4/panel/plugins/*
%_desktopdir/*
%_pixmapsdir/*
%_datadir/xfce4/mixer/
%_xfce4data/panel/plugins/*.desktop
%_man1dir/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Tue May 02 2023 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt1
- Enabled debug (minimum level).
- Updated summary and description.
- Updated BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Updated to 4.18.1 (resurrected to Sisyphus).

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt2
- Rebuild with libxfce4util-4.12.

* Thu Apr 10 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFce -> Xfce,XFCE).
- Updated to 4.11.0.

* Tue Apr 23 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2.git20130324
- Fix he.po.
- Upstream git snapshot.

* Wed Oct 10 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Fri Sep 28 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Updated from upsteam git (91598f7c34).
- Drop obsoleted patch.
- Updated to 4.9.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt4
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt3
- Rebuild with xfce4-panel-4.9.

* Tue Sep 13 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt2
- Fix plugin crash on mousewheel (closes: #26243).

* Tue Mar 08 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Drop obsoleted patches.
- Fix changelog entries.
- Updated to 4.8.0.

* Tue Feb 22 2011 Mikhail Efremov <sem@altlinux.org> 4.6.1-alt5
- Patches from upstream:
    + fix window's width.
    + Avoid disconnecting 0 handler.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 4.6.1-alt4
- Fix desktop file path for xfce4-panel >= 4.8.
- Fix page size (patch from Ubuntu).
- Remove 01_volume_hotkeys.patch (obsoleted).
- Spec updated, tar.bz2 -> tar.

* Fri Sep 11 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Added depency for xfce4-panel and gst-plugins base (fix for bug #21384)

* Sat May 09 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Updated russian translation

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
- Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release
- fix restore level (patch from Ubuntu)
- change audio subsystem from oss to alsa

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt3
- Fix buildreq and cleanup spec

* Sun Oct 01 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt2
- Removed libxfce4lixer.so from requires list.

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
