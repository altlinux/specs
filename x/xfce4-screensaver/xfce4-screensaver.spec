Name: xfce4-screensaver
Version: 4.20.2
Release: alt2

Summary: Screen saver and locker for Xfce
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/XFce
Url: https://git.xfce.org/apps/xfce4-screensaver/about/

Vcs: https://gitlab.xfce.org/apps/xfce4-screensaver.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

# Wayland support disabled for now: this requires libwlembed
# (https://gitlab.xfce.org/kelnos/libwlembed) which is not released yet.
%def_disable wayland

BuildRequires(pre): meson rpm-macros-meson >= 1.3.1-alt1
BuildRequires(pre): rpm-build-xfce4 >= 0.3.0 xfce4-dev-tools >= 4.17.1
BuildRequires(pre): rpm-build-xdg
BuildRequires: libxfconf-devel libgarcon-gtk3-devel libxfce4ui-gtk3-devel >= 4.18.4 libxfce4util-devel
BuildRequires: glib2-devel libgtk+3-devel libgio-devel
BuildRequires: libdbus-glib-devel libdbus-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: libXScrnSaver-devel libxklavier-devel
BuildRequires: libwnck3-devel
BuildRequires: libsystemd-devel libpam0-devel libwnck3-devel
%{?_enable_wayland:Buildrequires: wayland-devel libwlembed-gtk3-devel libwayland-client-devel wayland-protocols libxfce4windowing-devel}
BuildRequires: xmlto
# For xfce4-screensaver-configure
BuildRequires: rpm-build-python3

Requires: xfce4-common

%define _unpackaged_files_terminate_build 1

%description
%name is a screen saver and locker that aims to have simple, sane,
secure defaults and be well integrated with the desktop.

This project is a port of MATE Screensaver, itself a port of GNOME Screensaver.
It has been tightly integrated with the Xfce desktop, utilizing Xfce libraries
and the Xfconf configuration backend.

%prep
%setup
%patch -p1

%build
%meson \
	-Dx11=enabled \
	%{subst_enable_meson_feature wayland wayland} \
	-Dauthentication-scheme=pam \
	-Dpam-auth-type=system \
	-Dsession-manager=systemd \
	-Ddocs=enabled

%meson_build -v

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README.md
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/%name
%_xdgconfigdir/autostart/%name.desktop
%_xdgmenusdir/*.menu
%_bindir/%{name}*
%_libexecdir/%{name}*
%attr(2711,root,chkpwd) %_libexecdir/%name-dialog
%_desktopdir/screensavers/*.desktop
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*.service
%_datadir/desktop-directories/*.directory
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_pixmapsdir/*.svg

%changelog
* Tue Jun 16 2026 Mikhail Efremov <sem@altlinux.org> 4.20.2-alt2
- Fixed searching xscreensaver .xml config files.

* Mon Mar 02 2026 Mikhail Efremov <sem@altlinux.org> 4.20.2-alt1
- 4.20.1 -> 4.20.2.

* Fri Nov 21 2025 Mikhail Efremov <sem@altlinux.org> 4.20.1-alt2
- Show distro-logo instead of default avatar.

* Fri Aug 15 2025 Mikhail Efremov <sem@altlinux.org> 4.20.1-alt1
- 4.20.0 -> 4.20.1.

* Mon Jul 14 2025 Mikhail Efremov <sem@altlinux.org> 4.20.0-alt1
- Switched to meson build.
- 4.18.4 -> 4.20.0.

* Fri Mar 07 2025 Mikhail Efremov <sem@altlinux.org> 4.18.4-alt2
- Use ALT default background.

* Sun Dec 22 2024 Mikhail Efremov <sem@altlinux.org> 4.18.4-alt1
- 4.18.3 -> 4.18.4.

* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 4.18.3-alt2
- Fixed build: added intltool to BR.

* Mon Mar 04 2024 Mikhail Efremov <sem@altlinux.org> 4.18.3-alt1
- 4.18.2 -> 4.18.3.

* Tue May 30 2023 Mikhail Efremov <sem@altlinux.org> 4.18.2-alt1
- 4.18.1 -> 4.18.2.

* Mon Mar 27 2023 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt1
- 4.18.0 -> 4.18.1.

* Sat Mar 18 2023 Mikhail Efremov <sem@altlinux.org> 4.18.0-alt1
- Fixed setresgid()/setresuid() implicit declaration warning.
- 4.16.0 -> 4.18.0.

* Tue May 11 2021 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt2
- Fixed build: added rpm-build-python3 to BR.

* Sun Jan 03 2021 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt1
- 0.1.11 -> 4.16.0.

* Mon Nov 09 2020 Mikhail Efremov <sem@altlinux.org> 0.1.11-alt1
- Update Vcs tag.
- Drop exo-csource from BR.
- 0.1.10 -> 0.1.11.

* Mon Mar 30 2020 Mikhail Efremov <sem@altlinux.org> 0.1.10-alt1
- 0.1.9 -> 0.1.10.

* Mon Mar 23 2020 Mikhail Efremov <sem@altlinux.org> 0.1.9-alt1
- Use Vcs tag.
- Don't use rpm-build-licenses.
- 0.1.8 -> 0.1.9.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt1
- 0.1.7 -> 0.1.8.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1
- 0.1.6 -> 0.1.7.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- 0.1.5 -> 0.1.6.

* Thu Jun 13 2019 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5.

* Fri Mar 22 2019 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4.

* Wed Jan 30 2019 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Add pam_deny.so to PAM stack.
- It's OK if pam_gnome_keyring.so is absent.
- Install dialog as sgid program.
- Workaround for sgid GTK dialog.
- 0.1.2 -> 0.1.3.

* Mon Nov 19 2018 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- 0.1.0 -> 0.1.2.

* Mon Oct 15 2018 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.
