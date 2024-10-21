%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 47
%define beta %nil
%define xdg_name org.gnome.RemoteDesktop

%def_enable vnc
%def_enable rdp
%def_enable man

Name: gnome-remote-desktop
Version: %ver_major.1
Release: alt1%beta

Summary: GNOME Remote Desktop
License: GPL-2.0-or-later
Group: Networking/Remote access
Url: https://gitlab.gnome.org/GNOME/gnome-remote-desktop

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/gnome-remote-desktop.git
Source: %name-%version.tar
%endif

%define glib_ver 2.76
%define pw_api_ver 0.3
%define pw_ver 0.3.49
%define vnc_ver 0.9.11
%define freerdp_ver 3.1.0
%define fuse_ver 3.9.1
%define xkbc_ver 1.0.0
%define nvenc_ver 11.1.5.0
%define ei_ver 1.2.0
%define polkit_ver 122

Requires: pipewire >= %pw_ver
Requires: fuse3 >= %fuse_ver
Requires: polkit >= %polkit_ver
%{?_enable_rdp:Requires: freerdp3 >= %freerdp_ver}

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson libgio-devel >= %glib_ver libgudev-devel
BuildRequires: pkgconfig(libpipewire-%pw_api_ver) >= %pw_ver
BuildRequires: pkgconfig(opus)
BuildRequires: libtpm2-tss-devel libfdk-aac-devel
BuildRequires: libfuse3-devel >= %fuse_ver
BuildRequires: libxkbcommon-devel >= %xkbc_ver
BuildRequires: libsecret-devel libnotify-devel libcairo-devel
BuildRequires: libepoxy-devel libdrm-devel libgbm-devel
BuildRequires: pkgconfig(ffnvcodec) >= %nvenc_ver
BuildRequires: libei-devel >= %ei_ver
BuildRequires: libdbus-devel libpolkit-devel >= %polkit_ver
BuildRequires: /bin/dbus-run-session /usr/bin/openssl
BuildRequires: pipewire wireplumber mutter-gnome
%{?_enable_vnc:BuildRequires: libvncserver-devel >= %vnc_ver}
%{?_enable_rdp:BuildRequires: pkgconfig(freerdp3) >= %freerdp_ver}
%{?_enable_man:BuildRequires: /usr/bin/a2x xmllint}

%description
Remote desktop daemon for GNOME using pipewire.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{subst_enable_meson_bool rdp rdp} \
    %{subst_enable_meson_bool vnc vnc} \
    %{subst_enable_meson_bool man man} \
    -Dsystemd_user_unit_dir=%_userunitdir
%nil
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/grdctl
%_libexecdir/%name-daemon
%_libexecdir/%name-enable-service
%_libexecdir/%name-configuration-daemon
%_unitdir/%name.service
%_unitdir/%name-configuration.service
%_sysusersdir/%name-sysusers.conf
%_tmpfilesdir/%name-tmpfiles.conf
%_userunitdir/%name.service
%_userunitdir/%name-handover.service
%_userunitdir/%name-headless.service
%_desktopdir/%xdg_name.Handover.desktop
%_datadir/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%{?_enable_man:%_man1dir/grdctl.1*}
%dir %_datadir/%name
%_datadir/%name/grd-cuda-damage-utils_30.ptx
%_datadir/%name/grd-cuda-avc-utils_30.ptx
%_datadir/%name/grd.conf
%_datadir/dbus-1/system-services/%xdg_name.Configuration.service
%_datadir/dbus-1/system.d/%xdg_name.conf
%_datadir/polkit-1/actions/org.gnome.remotedesktop.configure-system-daemon.policy
%_datadir/polkit-1/actions/org.gnome.remotedesktop.enable-system-daemon.policy
%_datadir/polkit-1/rules.d/20-%name.rules
%doc README*

%changelog
* Mon Oct 21 2024 Yuri N. Sedunov <aris@altlinux.org> 47.1-alt1
- 47.1

* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Tue Aug 06 2024 Yuri N. Sedunov <aris@altlinux.org> 46.4-alt1
- 46.4

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt1
- 46.3

* Tue May 21 2024 Yuri N. Sedunov <aris@altlinux.org> 46.2-alt1
- 46.2 (fixed CVE-2024-5148)

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Sun Oct 22 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1

* Thu Sep 28 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Mon Sep 04 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt0.9.rc
- 45.rc

* Sun May 28 2023 Yuri N. Sedunov <aris@altlinux.org> 44.2-alt1
- 44.2

* Sat Apr 22 2023 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Mon Jan 09 2023 Yuri N. Sedunov <aris@altlinux.org> 43.3-alt1
- 43.3

* Sat Dec 03 2022 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Sun Oct 23 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.5-alt1
- 42.5

* Sun Aug 07 2022 Yuri N. Sedunov <aris@altlinux.org> 42.4-alt1
- 42.4

* Sun Jul 03 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Sun May 29 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Tue Apr 26 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1.1-alt1
- 42.1.1

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Mon Mar 07 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc

* Wed Dec 08 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Sat Oct 30 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Wed Sep 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sun May 02 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Fri Feb 22 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Sun Jun 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- fixed build with meson-0.43

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

