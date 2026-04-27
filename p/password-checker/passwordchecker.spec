%define _unpackaged_files_terminate_build 1
%define build_dir_adwaita build_adwaita
%define build_dir_gtk build_gtk
%define daemon_name passwordchecker
%define app_name PasswordChecker

Name:    password-checker
Version: 0.1.1
Release: alt1

Summary: Password expiry notification application
License: GPLv3
Group:   System/Configuration/Other
Url:     https://github.com/alxvmr/passwordchecker

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc gettext-tools
BuildRequires: pkgconfig(gio-2.0) pkgconfig(wbclient) pkgconfig(gtk4)
BuildRequires: libayatana-appindicator3-devel
BuildRequires: libldap-devel libsasl2-devel libwbclient-devel
# password-checker has an option to work with 
# userpasswd (adds a button in the notification).
# By default userpasswd is not included in dependencies,
# it is left to the user's choice
Requires: %name-common

Source0: %name-%version.tar

%description
GTK4 application for customizing password expiration notification settings

%package common
Summary: Translation files, .desktop and daemon for password-checker
Group: System/Configuration/Other
Requires: samba-winbind
Requires: icon-theme-adwaita

%description common
%summary

%package gnome
Summary: A application on Adwaita to customize notification settings
Group: System/Configuration/Other
BuildRequires: pkgconfig(libadwaita-1)
Requires: %name-common

%description gnome
%summary

%prep
%setup
mkdir -p %build_dir_adwaita
mkdir -p %build_dir_gtk

%build
%cmake -B %build_dir_adwaita\
    -DUSE_ADWAITA=ON
%cmake -B %build_dir_gtk\
    -DUSE_ADWAITA=OFF

cmake --build %build_dir_adwaita -j%__nprocs
cmake --build %build_dir_gtk -j%__nprocs

%install
DESTDIR=%buildroot cmake --install %build_dir_adwaita
# rename password-checker (adwaita) -> password-checker-adwaita
mv %buildroot%_bindir/%name  %buildroot%_bindir/%name-adwaita

DESTDIR=%buildroot cmake --install %build_dir_gtk
# rename password-checker (gtk) -> password-checker-gtk
mv %buildroot%_bindir/%name  %buildroot%_bindir/%name-gtk

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name-adwaita <<EOF
%_bindir/%name    %_bindir/%name-adwaita    50
EOF

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name-gtk <<EOF
%_bindir/%name    %_bindir/%name-gtk    30
EOF

%find_lang %daemon_name

%files
%_bindir/%name-gtk
%_altdir/%name-gtk

%files gnome
%_bindir/%name-adwaita
%_altdir/%name-adwaita

%files common -f %daemon_name.lang
%_desktopdir/%app_name.desktop
%_bindir/%daemon_name
%_user_unitdir/%daemon_name-user.service
%_datadir/glib-2.0/schemas/org.altlinux.%daemon_name.gschema.xml

%changelog
* Mon Apr 27 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.1-alt1
- Fixes conflicting types error during build.

* Mon Jul 14 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- Rename package: PasswordCheckerSettings to password-checker
- Add processing if the password never expires

* Wed May 21 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Init build

