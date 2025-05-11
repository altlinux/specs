%define _unpackaged_files_terminate_build 1

Name: gtklock-userinfo-module
Version: 4.0.1
Release: alt1

Summary: gtklock module adding user info to the lockscreen
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/jovanlanik/gtklock-userinfo-module

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gtk+-3.0)

%description
Adds a user image and user name to the lockscreen. Based on code from
Erik Reider's gtklock fork.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_libdir/gtklock/userinfo-module.so

%changelog
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus
