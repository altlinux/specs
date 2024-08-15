%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define libname libfeedback
%define ver_major 0.4
%define namespace Lfb
%define api_ver 0.0

%def_enable introspection
%def_enable vala
%def_enable man
%def_disable gtk_doc
%def_enable check

Name: feedbackd
Version: %ver_major.1
Release: alt1

Summary: Feedback library for GNOME
Group: System/Servers
License: GPL-3.0-or-later and LGPL-2.1-or-later
Url: https://source.puri.sm/Librem5/feedbackd

%if_disabled snapshot
Source: https://source.puri.sm/Librem5/%name/-/archive/v%version/%name-v%version.tar.gz
%else
Vcs: https://source.puri.sm/Librem5/feedbackd.git
Source: %name-%version.tar
%endif

Requires: %libname = %EVR
#Requires: feedbackd-device-themes

%define glib_ver 2.66
%define gudev_ver 232
%define gmobile_ver 0.2.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gsound)
BuildRequires: pkgconfig(gudev-1.0) >= %gudev_ver
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(gmobile) >= %gmobile_ver
BuildRequires: pkgconfig(umockdev-1.0)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: dbus-tools-gui}

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

%package -n %libname
Summary: Library for %name
License: LGPL-2.1-or-later
Group: System/Libraries

%description -n %libname
The lib%name package contains libraries for %name

%package -n %libname-devel
Summary: Development files for %libname
License: LGPL-2.1-or-later
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
The %name-devel package contains libraries and header files for
developing applications that use %libname.

%package -n %libname-gir
Summary: GObject introspection data for %libname
Group: System/Libraries
Requires: %libname = %EVR

%description -n %libname-gir
GObject introspection data for %libname

%package -n %libname-gir-devel
Summary: GObject introspection devel data for %libname
Group: Development/Other
BuildArch: noarch
Requires: %libname-gir = %EVR
Requires: %libname-devel = %EVR

%description -n %libname-gir-devel
GObject introspection devel data for %libname

%prep
%setup -n %name-%{?_disable_snapshot:v}%version
# ALT #47557
sed -i 's|-G %name|-G users|' data/90-feedbackd.rules

%build
%meson \
    %{?_disable_introspection:-Dintrospection=disabled} \
    %{?_disable_vala:-Dvapi=false} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_man:-Dman=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/fbcli
%_bindir/fbd-theme-validate
%_libexecdir/%name
%_libexecdir/fbd-ledctrl
%_udevrulesdir/90-%name.rules
%_datadir/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%_datadir/dbus-1/services/org.sigxcpu.Feedback.service
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml
%{?_enable_man:%_man1dir/fbcli.1.*
%_man1dir/fbd-theme-validate.1.*
%_man5dir/feedback-themes.5.*
%_man8dir/%name.8.*}

%files -n %libname
%_libdir/%libname-%api_ver.so.*

%files -n %libname-devel
%_includedir/%libname-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%libname-%api_ver.pc
%{?_enable_vala:%_datadir/vala/vapi/%libname-%api_ver.*}

%if_enabled introspection
%files -n %libname-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n %libname-gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%changelog
* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Jun 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue May 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0
- build against shared gmobile-0.1.0 library

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- updated to v0.2.1-15-g7588eca

* Wed Sep 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1.1
- 90-feedbackd.rules: use "-G users" instead of "-G feedbackd"
  as argument for fbd-ledctrl (ALT #47557)
- packaged lost man 5 feedback-themes

* Mon Sep 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon May 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Mar 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Mon Mar 27 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt2
- updated to v0.1.0-10-g1dbad7e (fixed crash exposed by glib 2.76)

* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- 0.0.3

* Tue Dec 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt1
- v0.0.2-2-gaa5e5e4

* Tue Nov 15 2022 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt1
- 0.0.1

* Fri Jul 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.0.0-alt0.1.git20210426
- first build for Sisyphus

