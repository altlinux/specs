%define alt_name userpasswd

Name:    userpasswd-gnome
Version: 0.0.1
Release: alt1

Summary: Graphical utility for changing user password
License: GPLv3
Group:   Other
Url:     https://github.com/alxvmr/userpasswd-gnome

BuildRequires(pre): rpm-macros-cmake rpm-macros-alternatives
BuildRequires: ccmake gcc-c++
BuildRequires: pkgconfig(gobject-2.0) pkgconfig(gio-2.0) pkgconfig(pam) pkgconfig(pam_misc) pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk4) pkgconfig(libadwaita-1)
Requires: userpasswd-common

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
mv %buildroot/%_bindir/%alt_name %buildroot/%_bindir/%name

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/%alt_name    %_bindir/%name    50
EOF

%post
chown :shadow %_libexecdir/userpasswd/helper
chmod g+s %_libexecdir/userpasswd/helper

%files
%_bindir/%name
%_altdir/%name
%_libexecdir/userpasswd/helper
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/%name.mo

%changelog
* Fri Feb 21 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus
