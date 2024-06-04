%def_enable snapshot
%def_enable installed_tests

Name: flatpak-xdg-utils
Version: 1.0.5
Release: alt1

Summary: Command-line tools for use inside Flatpak sandboxes
License: LGPL-2.1-or-later
Group: Development/Tools
Url: https://github.com/flatpak/flatpak-xdg-utils

Vcs: https://github.com/flatpak/flatpak-xdg-utils.git

%if_disabled snapshot
Source: https://github.com/flatpak/%name/releases/download/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: flatpak-spawn = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson pkgconfig(gio-2.0)

%description
This package contains a number of command-line utilities for use inside
Flatpak sandboxes. They work by talking to portals.

%package -n flatpak-spawn
Summary: Command-line frontend for the org.freedesktop.Flatpak service
Group: Development/Tools
Requires: flatpak

%description -n flatpak-spawn
This package contains the flatpak-spawn command-line utility. It can be
used to talk to the org.freedesktop.Flatpak service to spawn new sandboxes,
run commands on the host, or use one of the session or system helpers.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %EVR
Requires: flatpak-spawn = %EVR

%description tests
This package contains installed tests for %name.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool installed_tests installed_tests}
%nil
%meson_build

%install
%meson_install
%find_lang %name

mv %buildroot%_bindir/xdg-email %buildroot%_bindir/flatpak-xdg-email
mv %buildroot%_bindir/xdg-open %buildroot%_bindir/flatpak-xdg-open

%files -f %name.lang
%_bindir/flatpak-xdg-email
%_bindir/flatpak-xdg-open
%doc README.md

%files -n flatpak-spawn
%_bindir/flatpak-spawn

%if_enabled installed_tests
%files tests
%_datadir/installed-tests/%name/
%_libexecdir/installed-tests/%name/
%endif

%changelog
* Tue Jun 04 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- first build for Sisyphus (1.0.5-9-gb24e62e)

