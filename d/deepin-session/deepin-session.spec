%def_without clang

%define repo dde-session
%define _libexecdir %_prefix/libexec

Name: deepin-session
Version: 2.0.10
Release: alt1

Summary: Launching DDE components systemd service

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session
Vcs: https://github.com/linuxdeepin/dde-session

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/linuxdeepin/dde-session/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-session-2.0.6-alt-uos-version.patch

# We don't use deepin-keyring-whitebox now.
%filter_from_requires /\/usr\/bin\/deepin-keyring-whitebox/d

# Prevent bytes written limit by hasher-privd.
%filter_from_requires /\/usr\/bin\/kwin_x11/d
# Recommends: kwin

BuildRequires(pre): rpm-build-ninja rpm-build-systemd rpm-macros-dqt6
BuildRequires: cmake libXcursor-devel libXfixes-devel dtk6-common-devel libdtk6core-devel libsecret-devel libsystemd-devel dqt6-base-devel
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
export LC_ALL=C.UTF-8
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build

%install
%DQ6install
chmod +x %buildroot%_sysconfdir/X11/Xsession.d/00deepin-dde-env
chmod +x %buildroot%_sysconfdir/X11/Xsession.d/97deepin-keyring-wb

%files
%config(noreplace) %_sysconfdir/X11/Xsession.d/00deepin-dde-env
%config(noreplace) %_sysconfdir/X11/Xsession.d/01deepin-profile
%config(noreplace) %_sysconfdir/X11/Xsession.d/97deepin-keyring-wb
%exclude %_sysconfdir/profile.d/deepin-xdg-dir.sh
%_bindir/dde-session
%_bindir/dde-login-reminder
%_bindir/dde-keyring-checker
%_bindir/dde-version-checker
%_bindir/dde-xsettings-checker
%_bindir/dde-quick-login
%_libexecdir/dde-session-ctl
%_datadir/dbus-1/services/org.deepin.dde.Session1.service
%_datadir/xsessions/deepin.desktop
%_userunitdir/dde-session*
%_userunitdir/dde-shell-plugin@org.deepin.ds.desktop.service
%_userunitdir/dde-shell@DDE.service
%_userunitdir/dde-quick-login@x11.service
%_userunitdir/dde-lock.service
%_userunitdir/dde-polkit-agent.service
%_userunitdir/dde-login-reminder.service
%dir %_userunitdir/dde-osd.target.wants/
%_userunitdir/dde-osd.target.wants/dde-login-reminder.service
%_userunitdir/dde-keyring-checker.service
%_userunitdir/dde-version-checker.service
%_userunitdir/dde-xsettings-checker.service
%_userunitdir/dde-version-checker@quick-login.service

%changelog
* Tue Dec 02 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.10-alt1
- New version 2.0.10.
- Fixed non-executable scripts.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.9-alt1
- New version 2.0.9.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.8-alt1
- New version 2.0.8.

* Thu Oct 23 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.7-alt1
- New version 2.0.7.
- Fixed overlinked libraries.

* Thu Jul 17 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.6-alt1
- New version 2.0.6.
- Added vcs tag.
- Built via separate qt6 instead system (ALT #48138).

* Mon Apr 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.6-alt1
- New version 1.2.6.

* Thu Feb 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.5-alt1
- New version 1.2.5.

* Thu Dec 21 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.1-alt1
- Initial build for ALT Sisyphus.
