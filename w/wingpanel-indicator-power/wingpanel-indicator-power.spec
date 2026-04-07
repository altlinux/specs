%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.power

Name: wingpanel-indicator-power
Version: 8.0.2
Release: alt1.git.65e9700

Summary: Wingpanel Power Indicator
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/panel-power

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libnotify)
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
%_libdir/wingpanel-9/libpower.so
%_datadir/glib-2.0/schemas/io.elementary.panel.power.gschema.xml
%_datadir/metainfo/io.elementary.panel.power.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1.git.65e9700
- Initial build for Sisyphus
