%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 3.41
%define gcr_api_ver 3
%define gck_api_ver 1

%def_enable ssh_agent
%def_enable introspection
%def_enable gtk_doc
%def_enable check

Name: gcr
Version: %ver_major.0
Release: alt2

Summary: A GNOME crypto viewer and prompter
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/GnomeKeyring

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: %name-libs = %version-%release
Requires: libtasn1-utils
%{?_enable_ssh_agent:Requires: %_bindir/ssh-agent %_bindir/ssh-add}

%define glib_ver 2.44.0
%define gtk_ver 3.22
%define p11kit_ver 0.19.0
%define vala_ver 0.18.1
%define gcrypt_ver 1.4.5
%define secret_ver 0.20

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-systemd
BuildRequires: meson python3 glib2-devel >= %glib_ver
BuildRequires: libp11-kit-devel >= %p11kit_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgcrypt-devel >= %gcrypt_ver libtasn1-devel libtasn1-utils libtasn1-utils gnupg2-gpg
BuildRequires: libvala-devel >= %vala_ver vala-tools
%{?_enable_ssh_agent:BuildRequires: libsecret-devel >= %secret_ver %_bindir/ssh-agent %_bindir/ssh-add}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: /proc xvfb-run dbus-tools-gui %_bindir/ssh-keygen}

%description
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package libs
Summary: Development files for GCR
Group: System/Libraries

%description libs
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package libs-devel
Summary: Development files for GCR
Group: Development/C
Requires: %name-libs = %version-%release

%description libs-devel
The gcr-devel package includes the header files for the GCR libraries.

%package libs-gir
Summary: GObject introspection data for GCR libraries
Group: System/Libraries
Requires: %name-libs = %version-%release

%description libs-gir
GObject introspection data for GCR libraries.

%package libs-gir-devel
Summary: GObject introspection devel data for the GCR libraries
Group: System/Libraries
BuildArch: noarch
Requires: %name-libs-gir = %version-%release
Requires: %name-libs-devel = %version-%release

%description libs-gir-devel
GObject introspection devel data for the GCR libraries.

%package libs-vala
Summary: Vala language bindings for the GCR libraries
Group: Development/Other
BuildArch: noarch
Requires: %name-libs = %version-%release

%description libs-vala
This package provides Vala language bindings for the GCR libraries.

%package libs-devel-doc
Summary: Development documentation for GCR libraries
Group: Development/Documentation
Conflicts: %name-libs < %version-%release
BuildArch: noarch

%description libs-devel-doc
This package contains development documentation for GCR libraries.


%prep
%setup

%build
%meson \
    %{?_disable_ssh_agent:-Dssh_agent=false} \
    %{?_disable_introspection:-Dintrospection=false} \
    %{?_disable_gtk_doc:-Dgtk_doc=false}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run %__meson_test -t 2

%files -f %name.lang
%_bindir/%name-viewer
%_libexecdir/%name-prompter
%_libexecdir/%name-ssh-askpass
%{?_enable_ssh_agent:
%_libexecdir/%name-ssh-agent
%_userunitdir/%name-ssh-agent.service
%_userunitdir/%name-ssh-agent.socket}
%_datadir/applications/%name-viewer.desktop
%_datadir/applications/%name-prompter.desktop
%dir %_datadir/GConf
%dir %_datadir/GConf/gsettings
%_datadir/GConf/gsettings/org.gnome.crypto.pgp.convert
%_datadir/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
%_datadir/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml
%_datadir/icons/hicolor/*/apps/*
%_datadir/mime/packages/%name-crypto-types.xml
%_datadir/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%_datadir/dbus-1/services/org.gnome.keyring.SystemPrompter.service

%files libs
%_libdir/libgck-%gck_api_ver.so.*
%_libdir/lib%name-base-%gcr_api_ver.so.*
%_libdir/lib%name-ui-%gcr_api_ver.so.*

%files libs-devel
%_includedir/gck-%gck_api_ver
%_includedir/%name-%gcr_api_ver
%_libdir/libgck-%gck_api_ver.so
%_libdir/lib%name-base-%gcr_api_ver.so
%_libdir/lib%name-ui-%gcr_api_ver.so
%_pkgconfigdir/gck-%gck_api_ver.pc
%_pkgconfigdir/%name-%gcr_api_ver.pc
%_pkgconfigdir/%name-base-%gcr_api_ver.pc
%_pkgconfigdir/%name-ui-%gcr_api_ver.pc

%if_enabled gtk_doc
%files libs-devel-doc
%_datadir/doc/%name-%gcr_api_ver
%_datadir/doc/%name-ui-%gcr_api_ver
%_datadir/doc/gck-%gck_api_ver
%endif

%if_enabled introspection
%files libs-gir
%_typelibdir/Gck-%gck_api_ver.typelib
%_typelibdir/Gcr-%gcr_api_ver.typelib
%_typelibdir/GcrUi-%gcr_api_ver.typelib

%files libs-gir-devel
%_girdir/Gck-%gck_api_ver.gir
%_girdir/Gcr-%gcr_api_ver.gir
%_girdir/GcrUi-%gcr_api_ver.gir
%endif

%files libs-vala
%_vapidir/gck-%gck_api_ver.deps
%_vapidir/gck-%gck_api_ver.vapi
%_vapidir/%name-%gcr_api_ver.deps
%_vapidir/%name-%gcr_api_ver.vapi
%_vapidir/%name-ui-%gcr_api_ver.deps
%_vapidir/%name-ui-%gcr_api_ver.vapi
%_vapidir/pkcs11.vapi


%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.41.0-alt2
- updated to 3.41.0-27-g31bc9eb from gcr-3-41 branch (fixed build
  with meson >= 0.61)

* Thu Sep 30 2021 Yuri N. Sedunov <aris@altlinux.org> 3.41.0-alt1
- 3.41.0

* Sat Mar 27 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Wed Jan 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Mon Sep 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0 (ported to Meson build system)

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Oct 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue Oct 01 2019 Yuri N. Sedunov <aris@altlinux.org> 3.33.4-alt1
- updated to 3.33.4-15-ge060252

* Fri Jan 18 2019 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Mar 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.4-alt1
- 3.17.4

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Mar 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.92-alt1
- 3.15.92

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Thu Oct 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sun May 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Thu Mar 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.90-alt1
- 3.3.90

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.3.1-alt1
- first build for Sisyphus.

