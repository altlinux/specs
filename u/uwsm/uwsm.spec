%define _unpackaged_files_terminate_build 1

Name: uwsm
Version: 0.26.6
Release: alt1

Summary: Universal Wayland Session Manager
License: MIT
Group: Graphical desktop/Other
BuildArch: noarch

VCS: https://github.com/Vladimir-csp/uwsm
Url: https://github.com/Vladimir-csp/uwsm
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: meson
BuildRequires: scdoc

BuildRequires: rpm-build-python3
BuildRequires: python3-module-pyxdg
BuildRequires: python3-module-dbus

# Filter dmenu candidates:
%filter_from_requires /^\(vicinae\|walker\|fuzzel\|wofi\|rofi\)$/d
%filter_from_requires /^\(hyprlauncher\|tofi\|bemenu\|wmenu\|dmenu\)$/d

%add_python3_path %_datadir/uwsm
%filter_from_provides /^python3(modules\.uwsm\(\..*\)\?)/d

%description
Wraps standalone  Wayland compositors into  a set of Systemd  units on
the   fly.  This   provides   robust   session  management   including
environment, XDG autostart support,  bi-directional binding with login
session, and clean shutdown.

%prep
%setup
%patch0 -p1

%build
%meson -Duuctl=enabled -Dfumon=enabled -Duwsm-app=enabled
%meson_build

%install
%meson_install

# Package using %%doc macro
rm %buildroot%_datadir/licenses/uwsm/LICENSE
rm -rf %buildroot%_docdir/uwsm/

%files
%doc LICENSE README.md example-units/
%_bindir/fumon
%_bindir/uuctl
%_bindir/uwsm*
%_datadir/uwsm
%_user_unitdir/app-graphical.slice
%_user_unitdir/background-graphical.slice
%_user_unitdir/session-graphical.slice
%_user_unitdir/wayland-*
%_user_unitdir/fumon.service
%_user_presetdir/80-fumon.preset
%_libexecdir/uwsm/
%_desktopdir/uuctl.desktop
%_man1dir/fumon.1.*
%_man1dir/uuctl.1.*
%_man1dir/uwsm.1.*
%_man1dir/uwsm-app.1.*
%_man3dir/uwsm-plugins.3.*

%changelog
* Tue Jun 30 2026 Egor Ignatov <egori@altlinux.org> 0.26.6-alt1
- New version 0.26.6.

* Mon Jun 15 2026 Egor Ignatov <egori@altlinux.org> 0.26.5-alt1
- New version 0.26.5.

* Tue Mar 10 2026 Egor Ignatov <egori@altlinux.org> 0.26.4-alt1
- New version 0.26.4.

* Thu Nov 27 2025 Egor Ignatov <egori@altlinux.org> 0.24.3-alt2
- Remove optional runtime dependencies (closes: #57047)

* Fri Nov 21 2025 Egor Ignatov <egori@altlinux.org> 0.24.3-alt1
- New version 0.24.3.

* Wed Nov 12 2025 Egor Ignatov <egori@altlinux.org> 0.24.2-alt1
- New version 0.24.2.

* Wed Oct 15 2025 Egor Ignatov <egori@altlinux.org> 0.24.1-alt1
- New version 0.24.1.

* Thu Aug 28 2025 Egor Ignatov <egori@altlinux.org> 0.23.3-alt1
- New version 0.23.3.

* Mon Aug 25 2025 Egor Ignatov <egori@altlinux.org> 0.23.2-alt1
- New version 0.23.2.

* Fri Jun 27 2025 Egor Ignatov <egori@altlinux.org> 0.23.0-alt1
- New version 0.23.0.

* Wed Jun 25 2025 Egor Ignatov <egori@altlinux.org> 0.22.0-alt1
- New version 0.22.0.

* Mon Jun 09 2025 Egor Ignatov <egori@altlinux.org> 0.21.8-alt1
- New version 0.21.8.

* Thu May 15 2025 Egor Ignatov <egori@altlinux.org> 0.21.4-alt1
- New version 0.21.4.

* Sun May 04 2025 Egor Ignatov <egori@altlinux.org> 0.21.3-alt1
- First build for ALT.
