%define nm_version 1.1.90
%define nm_applet_version 1.2.0
%define nm_applet_name NetworkManager-applet-gtk
%def_with gtk4
%def_without libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-openconnect
Version: 1.2.10
Release: alt2
License: GPLv2+
Group: System/Configuration/Networking
Summary: NetworkManager VPN integration for openconnect

Url: http://www.gnome.org/projects/NetworkManager/

# https://gitlab.gnome.org/GNOME/NetworkManager-openconnect.git
Source: %name-%version.tar
Patch1: %name-%version-%release.patch
Requires: NetworkManager-daemon >= %nm_version
Requires: openconnect

BuildRequires: pkgconfig(glib-2.0) >= 2.34 pkgconfig(gmodule-2.0)
BuildRequires: libopenconnect-devel >= 3.02
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
%if_with gtk4
BuildRequires: libgtk4-devel
BuildRequires: libnma-gtk4-devel
%else
BuildRequires: libgtk+3-devel
%endif
BuildRequires: gcr-libs-devel >= 3.4
BuildRequires: libsecret-devel >= 0.18
BuildRequires: intltool gettext
BuildRequires: libxml2-devel

%description
This package contains software for integrating the openconnect VPN software
with NetworkManager and the GNOME desktop

%package gtk
License: GPLv2+
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-openconnect = %version-%release

Obsoletes: %name-gnome < 0.9.8.4
Provides: %name-gnome = %version-%release

%description gtk
This package contains applications for use with
NetworkManager panel applet.

%package gtk4
License: GPLv2+
Summary: Files for GTK4 applications to use %name
Group: Graphical desktop/GNOME
Requires: NetworkManager-openconnect = %version-%release

%description gtk4
This package contains files for GTK4 applications to use %name.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
    --disable-static \
    --libexecdir=%_libexecdir/NetworkManager \
    --localstatedir=%_var \
%if_without libnm_glib
    --without-libnm-glib \
%endif
    %{subst_with gtk4} \
    --disable-silent-rules \
    --enable-more-warnings=error

%make_build

%install
%makeinstall_std
install -d -m 0750 %buildroot%_sharedstatedir/nm-openconnect
%find_lang %name

%pre
groupadd -r -f nm-openconnect 2>/dev/null ||:
useradd  -r -s /sbin/nologin -d %_sharedstatedir/nm-openconnect -M \
         -c 'NetworkManager user for OpenConnect' \
         -g nm-openconnect nm-openconnect 2>/dev/null ||:

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING
%_libdir/NetworkManager/libnm-vpn-plugin-openconnect.so
%_datadir/dbus-1/system.d/nm-openconnect-service.conf
%_libexecdir/NetworkManager/nm-openconnect-service
%_libexecdir/NetworkManager/nm-openconnect-service-openconnect-helper
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-openconnect-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-openconnect-service.name
%attr(0770,nm-openconnect,nm-openconnect) %dir %_sharedstatedir/nm-openconnect

%files gtk
%if_with libnm_glib
%_libdir/NetworkManager/libnm-openconnect-properties.so
%endif
%_libexecdir/NetworkManager/nm-openconnect-auth-dialog
%_libdir/NetworkManager/libnm-vpn-plugin-openconnect-editor.so
%_datadir/metainfo/network-manager-openconnect.metainfo.xml

%if_with gtk4
%files gtk4
%_libdir/NetworkManager/libnm-gtk4-vpn-plugin-openconnect-editor.so
%endif

%exclude %_libdir/NetworkManager/lib*.la

%changelog
* Wed Nov 29 2023 Anton Midyukov <antohami@altlinux.org> 1.2.10-alt2
- NMU:
  + gtk4: Remove dependency on NetworkManager-applet-gtk (ALT#48620).
  + gtk4: Update summary, descriptions.

* Mon Sep 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.2.10-alt1
- New version 1.2.10.
- Add gtk4 package.
- Add nm-openconnect user in %%pre (ALT#47321).

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.8-alt1
- new version 1.2.8

* Wed Aug 21 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.6-alt1
- new version 1.2.6

* Wed Aug 01 2018 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt3
- Disable libnm-glib-* support.
- Fix build without libnm-glib-*.

* Wed Jan 10 2018 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt2
- Fix build.

* Mon Dec 05 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Mon Oct 10 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt2
- Rebuild with openconnect-7.06

* Fri May 13 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Fri Apr 22 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Mar 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.92-alt1
- Updated to 1.1.92 (1.2-beta3).

* Wed Mar 02 2016 Mikhail Efremov <sem@altlinux.org> 1.1.91-alt1
- Updated to 1.1.91 (1.2-beta2).

* Thu Jan 21 2016 Mikhail Efremov <sem@altlinux.org> 1.1.90-alt1
- Updated BR.
- 1.1.90.

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt5.git.2e653d
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt4.git.2e653d
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Wed Mar 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.9.8.4-alt3.git.2e653d
- rebuild with openconnect-5.99
- nm-0-9-8 branch snapshot (2e653d7b7636f67a25c084ab095907484ab85208)

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt2
- Fix build: Avoid deprecation warnings.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt1
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.
- 0.9.8.4

* Tue Feb 26 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.8.0-alt1
- 0.9.8.0

* Thu Oct 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.6.2-alt1
- 0.9.6.2

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.5.95-alt1
- 0.9.5.95

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt2
- upstream snapshot 12e173e93b1fc2559c24d870bcf1d0aba41e3d32

* Wed Apr 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt1
- 0.9.4.0

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Sep 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.999-alt1
- 0.8.999

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 0.8.3.995-alt1
- Minor spec cleanup.
- Changed libexecdir to %%_libexecdir/NetworkManager.
- 0.8.3.995 (0.8.4-beta1).

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Tue Oct 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.0.997-alt1
- 0.8.0.997 (0.8.1-beta1)

* Wed Mar 03 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- 0.8

* Sun Jan 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.997-alt1
- initial build
