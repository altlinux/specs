%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.datetime

Name: wingpanel-indicator-datetime
Version: 2.4.2
Release: alt1.git.b2cd175

Summary: Wingpanel Date & Time Indicator
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/panel-datetime

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(libecal-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: vapi(libedataserver-1.2)
BuildRequires: vapi(granite)

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_libdir/wingpanel-9/libdatetime.so
%_datadir/glib-2.0/schemas/io.elementary.panel.datetime.gschema.xml
%_datadir/metainfo/io.elementary.panel.datetime.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 2.4.2-alt1.git.b2cd175
- Initial build for Sisyphus
