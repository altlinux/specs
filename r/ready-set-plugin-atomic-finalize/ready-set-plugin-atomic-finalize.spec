# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/ready-set-plugin-atomic-finalize to altlinux branch 

%define _unpackaged_files_terminate_build 1

Name: ready-set-plugin-atomic-finalize
Version: 0.3
Release: alt1

Summary: ALT Atomic finalization logic baked in pageless plugin
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://altlinux.space/alt-atomic/ready-set-plugin-atomic-finalize
VCS: https://altlinux.space/alt-atomic/ready-set-plugin-atomic-finalize.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: apm
Requires: ready-set

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-ready-set
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libready-set-0.13)

%description
%summary that should be applied as final step.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%ready_set_steps_plugins_dir/*
%_datadir/polkit-1/rules.d/org.altlinux.ReadySet.Plugin.AtomicFinalize.rules

%changelog
* Tue Aug 11 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3-alt1
- New version: 0.3.

* Wed Jul 22 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2-alt1
- New version: 0.2.
- Fixed apm DBus action name.

* Mon Jul 20 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1-alt1
- Initail build.
