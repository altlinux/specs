%def_disable snapshot

%define _name chrono
%define ver_major 1.0
%define api_ver 1.0
%define rdn_name io.github.alainm23.chrono

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A natural language date and time parser library for Vala/GLib applications
Group: System/Libraries
License: GPL-3.0-or-later
Url: https://github.com/alainm23/chrono.git

Vcs: https://github.com/alainm23/chrono.git

%if_disabled snapshot
Source: https://github.com/alainm23/chrono/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.70.0

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(glib-2.0) >= %glib_ver
BuildRequires: pkgconfig(gee-0.8)

%description
%{summary}.

chrono parses natural language date and time strings such as "tomorrow",
"next Monday", or "in 3 days" into GLib.DateTime objects. It supports
recurrence rules and multiple languages.

Originally developed as part of [Planify](https://github.com/alainm23/planify).

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%check
%meson_test

%files -f %_name.lang
#%_libdir/*.so.*
%_libdir/*.so
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%files devel
%_includedir/%_name.h
#%_libdir/*.so
%_pkgconfigdir/%_name.pc
%_vapidir/%_name.vapi


%changelog
* Sun Jul 19 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

