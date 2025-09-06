%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: lomiri-session
Version: 0.3
Release: alt2

Summary: Integrate Lomiri Desktop Session into Display Managers
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-session

Source: %name-%version.tar

# sync with version 0.3-10 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-qt5-webengine

BuildRequires: cmake
BuildRequires: lomiri
BuildRequires: pkgconfig(libsystemd)
BuildRequires: /usr/bin/inotifywait

Requires: lomiri
Requires: lomiri-content-hub
Requires: xdg-user-dirs
Requires: lomiri-app-launch-tools
Requires: lomiri-schemas
Requires: inotify-tools

Requires: lomiri-terminal-app
Requires: lomiri-filemanager-app

%ifarch %qt5_qtwebengine_arches
Requires: morph-browser
%endif

BuildArch: noarch

%description
Lomiri is an operating environment optimized for touch based
human-machine interaction, but also supporting convergence (i.e.
switching between tablet/phone and desktop mode). Lomiri is the user
shell driving Ubuntu Touch based mobile devices.

This package provides the display manager / session manager integration
so that you can launch a Lomiri (Desktop) Session using your favourite
display manager.

%prep
%setup

%build
%cmake \
       -Wno-dev \
       -DENABLE_TOUCH_SESSION=off
%cmake_build

%install
%cmake_install

%post
%systemd_user_post lomiri.service

%preun
%systemd_user_preun lomiri.service

%postun
%systemd_user_postun lomiri.service

%files
%doc AUTHORS ChangeLog LICENSE
%_bindir/dm-lomiri-session
%_bindir/lomiri-session
%_datadir/wayland-sessions/lomiri.desktop
%_userunitdir/lomiri.service
%_libexecdir/lomiri-session/run-systemd-session

%changelog
* Thu Sep 04 2025 Nikolay Strelkov <snk@altlinux.org> 0.3-alt2
- Enabled install on systems without qt5-webengine

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
