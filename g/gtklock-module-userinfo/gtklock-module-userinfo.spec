Name: gtklock-module-userinfo
Version: 4.0.1
Release: alt1
License: GPL-3.0

Summary: gtklock module adding user info to the lockscreen

Group: Graphical desktop/Other

Url: https://github.com/jovanlanik/gtklock-userinfo-module
Vcs: https://github.com/jovanlanik/gtklock-userinfo-module.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(accountsservice)

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_libdir/gtklock/userinfo-module.so

%changelog
* Thu Apr 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 4.0.1-alt1
- Initial build
