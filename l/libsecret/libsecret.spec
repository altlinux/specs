%define ver_major 0.18
%define api_ver 1

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable vala
%def_disable check

Name: libsecret
Version: %ver_major.5
Release: alt1.1

Summary: A client library for the Secret Service DBus API
Group: System/Libraries
License: LGPLv2
Url: http://www.gnome.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#ource: %name-%version.tar

%define glib_ver 2.38.0
%define vala_ver 0.17.2.12
%define gcrypt_ver 1.4.5

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgcrypt-devel >= %gcrypt_ver
BuildRequires: gtk-doc intltool xsltproc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools >= %vala_ver}

# for check
%{?_enable_check:BuildRequires: /proc xvfb-run dbus-tools-gui python-module-dbus python-module-pygobject libgjs}

%description
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

This package provides development documentations for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
%{?_enable_gtk_doc:--enable-gtk-doc} \
%{subst_enable introspection}

%make_build

%install
%makeinstall_std

%find_lang %name

%check
# required X11
#xvfb-run %make check

%files -f %name.lang
%_bindir/secret-tool
%_libdir/%name-%api_ver.so.*
%_man1dir/secret-tool.1.*
%doc AUTHORS README NEWS

%files devel
%_includedir/%name-%api_ver
%_libdir/%name-%api_ver.so
%_libdir/pkgconfig/%name-%api_ver.pc
%_libdir/pkgconfig/%name-unstable.pc
%if_enabled vala
%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-%api_ver.deps
%endif

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/Secret-%api_ver.typelib

%files gir-devel
%_girdir/Secret-%api_ver.gir
%endif


%changelog
* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 0.18.5-alt1.1
- BOOTSTRAP: introduce check knob (*off* by default
  as %%check section is apparently disabled by now)

* Fri Mar 25 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18.5-alt1
- 0.18.5

* Tue Jan 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18.4-alt1
- 0.18.4

* Mon Aug 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- after 0.18.1 snapshot (bfe9f3514)

* Fri Mar 07 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Mon Aug 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Fri Apr 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt2
- added vala bindigs to -devel subpackage  (ALT #28841)

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13
- made %%check using xvfb-run

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Mon Jun 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

