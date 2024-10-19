%def_disable snapshot

%define ver_major 3.52
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.OnlineAccounts
%define namespace Goa
%define api_ver 1.0

%def_enable backend
%def_enable kerberos
%def_enable owncloud
%def_enable webdav
%def_enable exchange
%def_enable google
%def_enable imap_smtp
%def_enable windows_live
%def_enable doc
%def_enable man

Name: gnome-online-accounts
Version: %ver_major.1
Release: alt1

Summary: Provide online accounts information
Group: Graphical desktop/GNOME
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/GnomeOnlineAccounts

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%endif

Requires: lib%name = %EVR
# realmd requires /sbin/telinit provided by sysvinit or systemd-sysvinit packages
%{?_enable_kerberos:Requires: realmd systemd-sysvinit}
Requires: dconf gnome-keyring

%define glib_ver 2.68
%define gtk4_ver 4.15.2
%define adw_ver 1.4
%define gcr_ver 4.1.0
%define rest_ver 0.9.1
%define soup3_ver 3.0.7

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: pkgconfig(rest-1.0) >= %rest_ver
BuildRequires: pkgconfig(gcr-4) >= %gcr_ver
BuildRequires: pkgconfig(libsoup-3.0) >= %soup3_ver
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libjson-glib-devel
BuildRequires: libsecret-devel libdbus-devel
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: gobject-introspection-devel
%{?_enable_kerberos:BuildRequires: pkgconfig(krb5)}
%{?_enable_doc:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: xsltproc docbook-dtds docbook-style-xsl}

%description
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package -n lib%name
Summary: %name shared libraries
Group: System/Libraries

%description -n lib%name
This package contains shared %name libraries.

%package -n lib%name-devel
Summary: Development files for %name libraries
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains libraries and header files for developing
applications that use %name libraries.

%package -n lib%name-gir
Summary: GObject introspection data for the %name libraries
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the %name libraries

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name libraries
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the %name libraries

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: lib%name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the %name libraries.

%prep
%setup
# fix pkgconfig after gtk4 port
sed -i s'|gtk+-3.0|libadwaita-1|' src/goabackend/meson.build

%build
%meson \
    %{subst_enable_meson_bool man man} \
    %{subst_enable_meson_bool doc documentation} \
    %{subst_enable_meson_bool backend goabackend} \
    %{subst_enable_meson_bool exchange exchange} \
    %{subst_enable_meson_bool google google} \
    %{subst_enable_meson_bool imap_smtp imap_smtp} \
    %{subst_enable_meson_bool kerberos kerberos} \
    %{subst_enable_meson_bool owncloud owncloud} \
    %{subst_enable_meson_bool webdav webdav} \
    %{subst_enable_meson_bool windows_live windows_live}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %name %{?_enable_telepathy:%name-tpaw}

%files -f %name.lang
%if_enabled backend
%_libexecdir/goa-daemon
%_libexecdir/goa-identity-service
%_libexecdir/goa-oauth2-handler
%_desktopdir/%xdg_name.OAuth2.desktop
%_datadir/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml
%_datadir/dbus-1/services/org.gnome.Identity.service
%_datadir/dbus-1/services/%xdg_name.service
%{?_enable_man:%_man8dir/goa-daemon.*}
%endif
%_iconsdir/hicolor/*/*/*.svg
%{?_enable_telepathy:%_iconsdir/hicolor/scalable/apps/im-*.svg}
%doc README* NEWS

%files -n lib%name
%_libdir/libgoa-%api_ver.so.*
%dir %_libdir/goa-%api_ver

%if_enabled backend
%_libdir/libgoa-backend-%api_ver.so.*
%endif

%files -n lib%name-devel
%_includedir/goa-%api_ver/
%dir %_libdir/goa-%api_ver/include
%_libdir/goa-%api_ver/include/goaconfig.h
%_libdir/libgoa-%api_ver.so

%if_enabled backend
%_libdir/libgoa-backend-%api_ver.so
%_pkgconfigdir/goa-backend-%api_ver.pc
%endif

%_pkgconfigdir/goa-%api_ver.pc
%_vapidir/goa-%api_ver.deps
%_vapidir/goa-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%namespace-%api_ver.gir

%if_enabled doc
%files -n lib%name-devel-doc
%_datadir/doc/%name
%endif

%changelog
* Sat Oct 19 2024 Yuri N. Sedunov <aris@altlinux.org> 3.52.1-alt1
- 3.52.1

* Sun Sep 15 2024 Yuri N. Sedunov <aris@altlinux.org> 3.52.0-alt1
- 3.52.0

* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.50.5-alt1
- 3.50.5

* Sun Aug 04 2024 Yuri N. Sedunov <aris@altlinux.org> 3.50.4-alt1
- 3.50.4

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 3.50.3-alt1
- 3.50.3

* Sat May 25 2024 Yuri N. Sedunov <aris@altlinux.org> 3.50.2-alt1
- 3.50.2

* Fri Apr 12 2024 Yuri N. Sedunov <aris@altlinux.org> 3.50.1-alt1
- 3.50.1

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 3.50.0-alt1
- 3.50.0

* Thu Mar 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.48.1-alt1
- 3.48.1

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 3.48.0-alt1.2
- explicitly required realmd+systemd-sysvinit to prevent
  apt to resolve /sbin/telinit from sysvinit package

* Sun Dec 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.48.0-alt1.1
- fixed build with libxml2-2.12.x

* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 3.48.0-alt1
- 3.48.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Tue Aug 09 2022 Yuri N. Sedunov <aris@altlinux.org> 3.45.2-alt1
- 3.45.2 (ported to Meson build system, rest-1.0/libsoup-3.0)

* Wed Mar 30 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 3.43.1-alt1
- 3.43.1

* Mon Oct 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt1
- 3.40.1

* Wed Apr 21 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.39.92-alt1
- 3.39.92

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Wed Oct 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sat Jun 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1.1
- mike@: webkit knob (on by default)

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Feb 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.90-alt1
- 3.31.90

* Mon Feb 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sat Sep 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Thu Mar 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.92-alt1
- 3.27.92

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Wed Sep 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Thu Aug 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Fri Mar 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Wed Dec 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Thu Jul 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Fri Jul 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Thu Dec 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2.1-alt1
- 3.18.2

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Tue Jun 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Tue Jun 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt2
- updated to 3.16.2_27b0ed00

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Jan 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Thu Oct 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Jul 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt2
- Requires realmd if enabled kerberos support

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt2
- explicitly enabled some providers

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Dec 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- first build for Sisyphus

