%define _unpackaged_files_terminate_build 0
%define alt_name userpasswd

Name:    userpasswd-gnome
Version: 0.0.2
Release: alt1

Summary: Graphical utility for changing user password
License: GPLv3
Group:   Other
Url:     https://github.com/alxvmr/userpasswd-gnome

BuildRequires(pre): rpm-macros-cmake rpm-macros-alternatives
BuildRequires: cmake gcc
BuildRequires: pkgconfig(gobject-2.0) pkgconfig(gio-2.0) pkgconfig(pam) pkgconfig(pam_misc) pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk4) pkgconfig(libadwaita-1)

# Common files with userpasswd.desktop
Requires: userpasswd-common >= 0.3.7-alt1
# Due same as passwd PAM_SERVICE - /etc/pam.d/passwd
Requires: passwd

Source0: %name-%version.tar

%description
A graphical utility to change your password in GNOME

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

# rename userpasswd -> userpasswd-gnome
mv %buildroot%_bindir/%alt_name %buildroot/%_bindir/%name

# Remove own desktop file due userpasswd-common requirement
rm -f %buildroot%_desktopdir/%alt_name.desktop

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/%alt_name    %_bindir/%name    50
EOF

%files
%_bindir/%name
%_altdir/%name
%attr(2711, root, shadow) %_libexecdir/userpasswd/helper
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/%name.mo

%changelog
* Fri Apr 18 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.2-alt1
- Update version to 0.0.2-alt1
- UI fixes

* Sun Feb 23 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt2
- Assignment of file attributes now occurs in %attr (Closes: #53207)

* Fri Feb 21 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus
