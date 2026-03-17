%define _unpackaged_files_terminate_build 1

Name: kanshi
Version: 1.9.0
Release: alt2

Summary: Dynamic display configuration
License: MIT
Group: Graphical desktop/Other

Url: https://wayland.emersion.fr/kanshi
VCS: https://gitlab.freedesktop.org/emersion/kanshi

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: meson ninja-build
BuildRequires: libwayland-client-devel libscfg-devel libvali-devel
BuildRequires: scdoc vali

%description
kanshi allows you to define output profiles that are automatically
enabled and disabled on hotplug. For instance, this can be used to
turn a laptop's internal screen off when docked.

This is a Wayland equivalent for tools like autorandr. kanshi can be
used on Wayland compositors supporting the wlr-output-management
protocol.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md
%_bindir/kanshi
%_bindir/kanshictl
%_man1dir/kanshi.1.xz
%_man1dir/kanshictl.1.xz
%_man5dir/kanshi.5.xz

%changelog
* Tue Mar 17 2026 Andrey Kovalev <ded@altlinux.org> 1.9.0-alt2
- Rebuilt kanshi with kanshictl.

* Tue Feb 03 2026 Andrey Kovalev <ded@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Jul 29 2025 Andrey Kovalev <ded@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Oct 09 2024 Andrey Kovalev <ded@altlinux.org> 1.7.0-alt1
- 1.7.0

* Tue Feb 06 2024 Egor Ignatov <egori@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 31 2023 Egor Ignatov <egori@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Nov 27 2023 Egor Ignatov <egori@altlinux.org> 1.4.0-alt1
- First build for ALT
