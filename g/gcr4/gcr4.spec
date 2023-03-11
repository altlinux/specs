%def_disable snapshot

%define _name gcr
%define _libexecdir %_prefix/libexec
%define ver_major 4.1
%define gcr_api_ver 4
%define gck_api_ver 2

%def_enable gtk4
%def_enable ssh_agent
%def_enable introspection
%def_enable gtk_doc
%def_enable check

Name: gcr%gcr_api_ver
Version: %ver_major.0
Release: alt1

Summary: A GNOME crypto viewer and prompter
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/GnomeKeyring

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Requires: %name-libs = %EVR
Requires: libtasn1-utils
%{?_enable_ssh_agent:Requires: %_bindir/ssh-agent %_bindir/ssh-add}
%{?_disable_ssh_agent:Conflicts: gcr < 3.41.1-alt2}

%define meson_ver 0.59
%define glib_ver 2.44.0
%define gtk_ver 3.22
%define p11kit_ver 0.19.0
%define vala_ver 0.18.1
%define gcrypt_ver 1.4.5
%define secret_ver 0.20

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-systemd
BuildRequires: meson >= %meson_ver glib2-devel >= %glib_ver
BuildRequires: libp11-kit-devel >= %p11kit_ver
%{?_enable_gtk4:BuildRequires: libgtk4-devel}
BuildRequires: libgcrypt-devel >= %gcrypt_ver libtasn1-devel libtasn1-utils libtasn1-utils gnupg2-gpg
BuildRequires: libvala-devel >= %vala_ver vala-tools
BuildRequires: libsecret-devel >= %secret_ver %_bindir/ssh-agent %_bindir/ssh-add
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
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
Requires: %name-libs = %EVR

%description libs-devel
The gcr-devel package includes the header files for the GCR libraries.

%package libs-gir
Summary: GObject introspection data for GCR libraries
Group: System/Libraries
Requires: %name-libs = %EVR

%description libs-gir
GObject introspection data for GCR libraries.

%package libs-gir-devel
Summary: GObject introspection devel data for the GCR libraries
Group: System/Libraries
BuildArch: noarch
Requires: %name-libs-gir = %EVR
Requires: %name-libs-devel = %EVR

%description libs-gir-devel
GObject introspection devel data for the GCR libraries.

%package libs-vala
Summary: Vala language bindings for the GCR libraries
Group: Development/Other
BuildArch: noarch
Requires: %name-libs = %EVR

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
%setup -n %_name-%version

%build
%meson \
    %{?_disable_ssh_agent:-Dssh_agent=false} \
    %{?_disable_introspection:-Dintrospection=false} \
    %{?_disable_gtk_doc:-Dgtk_doc=false}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-%gcr_api_ver

%check
xvfb-run %__meson_test -t 3

%files -f %_name-%gcr_api_ver.lang
%{?_enable_gtk4:%_bindir/%_name-viewer-gtk4}
%_libexecdir/%name-ssh-askpass
%{?_enable_ssh_agent:
%_libexecdir/%_name-ssh-agent
%_userunitdir/%_name-ssh-agent.service
%_userunitdir/%_name-ssh-agent.socket}

%files libs
%_libdir/libgck-%gck_api_ver.so.*
%_libdir/lib%_name-%gcr_api_ver.so.*

%files libs-devel
%_includedir/gck-%gck_api_ver
%_includedir/%_name-%gcr_api_ver
%_libdir/libgck-%gck_api_ver.so
%_libdir/lib%_name-%gcr_api_ver.so
%_pkgconfigdir/gck-%gck_api_ver.pc
%_pkgconfigdir/%_name-%gcr_api_ver.pc

%if_enabled gtk_doc
%files libs-devel-doc
%_datadir/doc/%_name-%gcr_api_ver
%_datadir/doc/gck-%gck_api_ver
%endif

%if_enabled introspection
%files libs-gir
%_typelibdir/Gck-%gck_api_ver.typelib
%_typelibdir/Gcr-%gcr_api_ver.typelib

%files libs-gir-devel
%_girdir/Gck-%gck_api_ver.gir
%_girdir/Gcr-%gcr_api_ver.gir
%endif

%files libs-vala
%_vapidir/gck-%gck_api_ver.deps
%_vapidir/gck-%gck_api_ver.vapi
%_vapidir/%_name-%gcr_api_ver.deps
%_vapidir/%_name-%gcr_api_ver.vapi

%changelog
* Wed Mar 08 2023 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0

* Wed Oct 12 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Mon Sep 05 2022 Yuri N. Sedunov <aris@altlinux.org> 3.92.0-alt1
- 3.92.0
- enabled ssh-agent binary

* Sun Jul 10 2022 Yuri N. Sedunov <aris@altlinux.org> 3.90.0-alt1
- 3.90.0 (gcr-4, gck-2)
- temporarily disabled ssh-agent binary

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

