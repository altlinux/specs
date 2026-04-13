%define exID runcat@kolesnikov.se

Name: gnome-shell-extension-gnome-runcat
Version: 32
Release: alt1

Summary: RunCat for GNOME Shell
Summary(ru_RU.UTF-8): Бегущий кот для GNOME Shell 

License: GPL-3.0-only
Group:  Graphical desktop/GNOME
Url: https://github.com/win0err/gnome-runcat
VCS: https://github.com/win0err/gnome-runcat

ExcludeArch: i586

Source: %name-%version.tar
Source1: node_modules.tar
Source2: arch64.tar

BuildRequires(Pre): rpm-build-nodejs
BuildRequires: unzip %_bindir/glib-compile-schemas %_bindir/gnome-extensions
Requires: gnome-shell >= 47

%description
RunCat provides a key-frame animation to the GNOME Shell top bar.
Animation speed changes depending on CPU usage.

%prep
%setup
%ifarch x86_64
	tar -xf %SOURCE1 -C ./
%endif
%ifarch aarch64
	tar -xf %SOURCE2 -C ./
%endif

#subst 's|"49"|"49", "50"|' src/metadata.json

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
* Tue Apr 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 32-alt1
- 31 -> 32

* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 31-alt2
- fixed for GNOME 50

* Wed Oct 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 31-alt1
- 30 -> 31

* Thu Sep 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 30-alt1
- 29 -> 30

* Fri Mar 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 29-alt1
- 28 -> 29

* Wed Mar 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 28-alt2
- fixed for GNOME 48

* Sun Nov 24 2024 Aleksandr Shamaraev <shad@altlinux.org> 28-alt1
- Initial build for Sisyphus.
