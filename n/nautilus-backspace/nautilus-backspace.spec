%define _unpackaged_files_terminate_build 1
%define xdg_name io.github.alt-gnome-team.nautilus-backspace

Name: nautilus-backspace
Version: 0.7.1
Release: alt1

Summary: An extension for configuring the backtrack combination for Gnome nautilus
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://altlinux.space/alt-gnome/nautilus-backspace
Vcs: https://altlinux.space/alt-gnome/nautilus-backspace

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: nautilus-python
Requires: libnautilus-gir

%description
The extension allows you to return to the previous directory in Nautilus by
pressing the backspace button or another keyboard shortcut assigned through
the GSettings.

%description -l ru_RU.UTF-8
Расширение позволяет возвращаться в предыдущую директорию в Nautilus по
нажатию кнопки backspace или иного сочетания клавиш, назначенного через
GSettings.

%prep
%setup
%autopatch -p1

%install
%makeinstall_std INSTALL_DATAROOTDIR=%buildroot%_datadir

%files
%_datadir/nautilus-python/extensions/Back.py
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml

%changelog
* Fri Jun 06 2025 Alexey Volkov <qualimock@altlinux.org> 0.7.1-alt1
- New version 0.7.1

* Sat Oct 5 2024 Alexey Volkov <qualimock@altlinux.org> 0.6.0-alt1
- New version 0.6.0 (closes: #50046)

* Thu Apr 4 2024 Alexey Volkov <qualimock@altlinux.org> 0.5.0-alt1
- Initial build for ALT
