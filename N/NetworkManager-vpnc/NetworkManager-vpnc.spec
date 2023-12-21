%define nm_version 1.1.90
#define git_hash %nil
%define git_hash .g7e01b1d

%def_with gtk4

%define _unpackaged_files_terminate_build 1

%ifarch %e2k
%define more_warnings no
%else
%define more_warnings error
%endif

Name: NetworkManager-vpnc
Version: 1.2.9
Release: alt1%git_hash
License: GPLv2+
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for vpnc
Url: https://networkmanager.dev/docs/vpn/
Vcs: https://gitlab.gnome.org/GNOME/NetworkManager-vpnc.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel
BuildRequires: libgtk+3-devel
%{?_with_gtk4:BuildRequires: libgtk4-devel >= 4.6.3 libnma-gtk4-devel}
BuildRequires: libsecret-devel
BuildRequires: intltool gettext

Requires: NetworkManager-daemon   >= %nm_version
Requires: vpnc             >= 0.4

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager

%package gtk-common
License: GPLv2+
Summary: Common part of %name GTK support
Group: Graphical desktop/GNOME
Requires: NetworkManager-vpnc = %version-%release

%description gtk-common
This package contains common part for %name GTK support.

%package gtk3
License: GPLv2+
Summary: Files for GTK3 applications to use %name
Group: Graphical desktop/GNOME
Requires: %name-gtk-common = %version-%release

Obsoletes: %name-gnome < 0.9.8.6
Provides: %name-gnome = %version-%release

Obsoletes: %name-gtk < 1.2.8-alt1
Provides: %name-gtk = %version-%release

%description gtk3
This package contains files for GTK3 applications to use %name.

%if_with gtk4
%package gtk4
License: GPLv2+
Summary: Files for GTK4 applications to use %name
Group: Graphical desktop/GNOME
Requires: %name-gtk-common = %version-%release

%description gtk4
This package contains files for GTK4 applications to use %name.
%endif

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--without-libnm-glib \
	%{subst_with gtk4} \
	--enable-more-warnings=%more_warnings
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files
%doc AUTHORS
%_libexecdir/NetworkManager/nm-vpnc-service
%_libexecdir/NetworkManager/nm-vpnc-service-vpnc-helper
%_libdir/NetworkManager/libnm-vpn-plugin-vpnc.so
%config %_datadir/dbus-1/system.d/nm-vpnc-service.conf
%config %_libexecdir/NetworkManager/VPN/nm-vpnc-service.name

%files gtk-common -f %name.lang
%_libexecdir/NetworkManager/nm-vpnc-auth-dialog
%_datadir/metainfo/*.xml

%files gtk3
%_libdir/NetworkManager/libnm-vpn-plugin-vpnc-editor.so

%if_with gtk4
%files gtk4
%_libdir/NetworkManager/libnm-gtk4-vpn-plugin-vpnc-editor.so
%endif

%exclude %_libdir/NetworkManager/*.la

%changelog
* Thu Dec 21 2023 Mikhail Efremov <sem@altlinux.org> 1.2.9-alt1.g7e01b1d
- Upstream git snapshot (for updated translations mostly).
- Used Russian translation from upstream.
- Dropped workaround with xvfb-run.

* Thu Mar 17 2022 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt1
- Used xvfb-run.
- Added gtk4 subpackage.
- Dropped libnm_glib support.
- Updated to 1.2.8.

* Thu Jan 20 2022 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt2
- Disable -Werror on e2k.
- Set enable-more-warnings to error.
- Update Url tag.
- Add Vcs tag.
- Don't use rpm-build-licenses.
- Use our own Russian translation (closes: #37827).

* Wed Aug 01 2018 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1
- Disable libnm-glib-* support.
- Fix build without libnm-glib-*.
- Updated to 1.2.6 (fixes CVE-2018-10900).

* Mon Oct 03 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Fri May 13 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Fri Apr 22 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Mar 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.92-alt1
- Updated to 1.1.92 (1.2-beta3).

* Wed Mar 02 2016 Mikhail Efremov <sem@altlinux.org> 1.1.91-alt1
- Updated to 1.1.91 (1.2-beta2).

* Thu Jan 21 2016 Mikhail Efremov <sem@altlinux.org> 1.1.90-alt1
- Updated to 1.1.90.

* Mon Nov 30 2015 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Updated to 1.0.8.

* Mon Aug 31 2015 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1
- Minor spec cleanup.
- Updated to 1.0.6.

* Fri May 08 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Fri Feb 13 2015 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Updated to 1.0.0.

* Wed Jul 09 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.0-alt1
- Spec updated for new version.
- Updated to 0.9.10.0.

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.6-alt3
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.6-alt2
- Temporary don't treat warrnings as errors.
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.6-alt1
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.
- Updated to 0.9.8.6.

* Thu Jul 18 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt1
- From upstream git:
  + Fix path to connection-editor plugin in service file.
- Updated to 0.9.8.2.

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt1
- Treat warrnings as errors again.
- Updated to 0.9.8.0.

* Mon Oct 08 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt2
- Fix build: temporary don't treat warrnings as errors.

* Wed Aug 08 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt1
- Updated to 0.9.6.0.

* Wed Jul 04 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Updated from upstream git (9fb8461cc0).
- Updated to 0.9.5.95 (0.9.6-rc1).

* Thu Apr 05 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt1
- Updated from upstream git (3658221c15).
- 0.9.4.0.

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1
- 0.9.1.95 (0.9.2-rc1).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- 0.9.0 release.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2.git20110510
- Build with GTK+3.
- Rename src.rpm package.
- Package nm-vpnc-auth-dialog.desktop for gnome-shell (tnx aris).

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1.git20110510
- Enable tests.
- Minor spec cleanup.
- upstream git snapshot (master branch).

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.996-alt1.git20110314
- Changed libexecdir to %%_libexecdir/NetworkManager.
- upstream git snapshot (master branch).

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Fix source tarball and general patch packaging.

* Mon Nov 08 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100914
- upstream git snapshot (master branch).

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100628
- upstream git snapshot

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- rename NMVpnPluginUiInterface fields.
- upstream git snapshot

* Wed Apr 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- Don't package ChangeLog.
- upstream git snapshot

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091124
- upstream git snapshot

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091028
- upstream git snapshot
- fix gnome subpackage requires.

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20091005
- upstream git snapshot (NETWORKMANAGER_0_7 branch)

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Tue Mar 03 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt2
- GNOME stuff moved to NetworkManager-vpnc-gnome

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3
- Release NetworkManager 0.7

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r4326
- BuildRequires fixed

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r4326
- new svn snapshot
- removed obsolete post/postun macros calls
- update summary

* Tue Nov 11 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r4229
- new svn snapshot

* Wed Aug 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r3930
- new svn snapshot
- BuildRequires updated
- %post updated: D-Bus config reload

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080722
- new svn snapshot (3842)

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080527
- initial build

