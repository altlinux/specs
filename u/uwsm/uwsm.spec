%define _unpackaged_files_terminate_build 1

Name: uwsm
Version: 0.21.3
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
%_user_unitdir/fumon.service
%_desktopdir/uuctl.desktop
%_man1dir/fumon.1.*
%_man1dir/uwsm.1.*
%_man3dir/uwsm-plugins.3.*

%changelog
* Sun May 04 2025 Egor Ignatov <egori@altlinux.org> 0.21.3-alt1
- First build for ALT.
