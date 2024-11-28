%define exID runcat@kolesnikov.se

Name: gnome-shell-extension-gnome-runcat
Version: 28
Release: alt1

Summary: RunCat for GNOME Shell
Summary(ru_RU.UTF-8): Бегущий кот для GNOME Shell 

BuildArch: noarch

License: GPL-3.0 license
Group:  Graphical desktop/GNOME
Url: https://github.com/win0err/gnome-runcat
VCS: https://github.com/win0err/gnome-runcat

Source: %name-%version.tar

BuildRequires: unzip %_bindir/glib-compile-schemas %_bindir/gnome-extensions
Requires: gnome-shell >= 47

%description
RunCat provides a key-frame animation to the GNOME Shell top bar.
Animation speed changes depending on CPU usage.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
unzip dist/%exID.shell-extension.zip -d %buildroot%_datadir/gnome-shell/extensions/%exID/
glib-compile-schemas %buildroot%_datadir/gnome-shell/extensions/%exID/schemas/

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc *.md LICENSE 

%changelog
* Sun Nov 24 2024 Aleksandr Shamaraev <shad@altlinux.org> 28-alt1
- Initial build for Sisyphus.
