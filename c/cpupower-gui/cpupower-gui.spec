%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name cpupower_gui
%define ver_major 1.0
%define rdn_name org.rnd2.%_name
%define xdg_name org.rnd2.cpupower-gui

# online screenshots
%def_disable check

Name: cpupower-gui
Version: %ver_major.0
Release: alt1.1

Summary: A graphical program that is used to change the scaling frequency limits of the cpu, similar to cpupower.
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/vagnum08/cpupower-gui

Vcs: https://github.com/vagnum08/cpupower-gui.git

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: %url/archive/v%version/%name-%version.tar.gz
%endif

BuildArch: noarch
%add_python3_path %_datadir/%name

%define handy_ver 1.5.0

Requires: dconf polkit
Requires: typelib(Gtk) = 3.0 typelib(Handy) = 1 typelib(AyatanaAppIndicator3) = 0.1

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver typelib(Handy) = 1
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
This program is designed to allow you to change the frequency limits of
your cpu and its governor. The application is similar in functionality
to `cpupower`.

%prep
%setup -n %name-%version

%build
%meson \
    -Dsystemddir=%_systemddir \
    -Duse_libexec=true
%nil
%meson_build

%install
%meson_install
%find_lang --with-man --with-gnome %name

%check
%__meson_test

%post
if [ $1 -eq 1 ] ; then
    SYSTEMCTL=/sbin/systemctl
    $SYSTEMCTL enable %name-helper > /dev/null 2>&1 ||:
fi

%preun
if [ $1 -eq 0 ] ; then
    SYSTEMCTL=/sbin/systemctl
    $SYSTEMCTL --no-reload disable %name-helper %name > /dev/null 2>&1 ||:
fi

%files -f %name.lang
%config(noreplace) %_sysconfdir/%_name.conf
%dir %_sysconfdir/%_name.d
%_sysconfdir/%_name.d/README
%_sysconfdir/%_name.d/my_profile.profile.ex
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name-helper
%_unitdir/%name-helper.service
%_unitdir/%name.service
%_userunitdir/%name-user.service
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/system-services/%rdn_name.helper.service
%_datadir/dbus-1/system.d/%rdn_name.helper.conf
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/polkit-1/actions/%xdg_name.policy
%_datadir/polkit-1/rules.d/%xdg_name.rules
%_iconsdir/hicolor/*/*/*.svg
%_man1dir/%name.1*
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*

%changelog
* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.1
- rebuilt with new systemd macros

* Wed Feb 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus (v1.0.0-24-gb44a198) (ALT #49455)

