%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerMobileTweaks
%define plugin_name mobile-tweaks

Name: tuner-%plugin_name
Version: 0.2.2
Release: alt1

Summary: Extra Mobile settings
License: GPL-3.0-or-later
Group: Graphical desktop/Other

URL: https://altlinux.space/alt-mobile/TunerMobileTweaks
VCS: https://altlinux.space/alt-mobile/TunerMobileTweaks
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: gir(Tuner) = 1

Requires: tuner
Requires: phosh

%description
Unified Settings Center as a Tuner plugin.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_pluginsdir/lib%plugin_name.so
%_pluginsdir/%plugin_name.plugin
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Thu May 07 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.2-alt1
- Add Feedback settings per application.
- Remove "Show battery percentage".
- Add Screen Wakeup on categories.
- Add events sound selection.

* Fri Apr 24 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.1-alt1
- Add RU translation.

* Wed Apr 22 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.0-alt1
- Initial build.
