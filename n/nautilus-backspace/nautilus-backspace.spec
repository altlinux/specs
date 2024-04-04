Name: nautilus-backspace
Version: 0.5.0
Release: alt1

Summary: extension for configuring the backtrack combination for Gnome nautilus
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/alt-gnome-team/nautilus-backspace

BuildArch: noarch

Source: %name-%version.tar

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

%install
mkdir -p %buildroot%_datadir/nautilus-python/extensions/
cp Back.py %buildroot%_datadir/nautilus-python/extensions/
mkdir -p %buildroot%_datadir/glib-2.0/schemas/
cp io.github.alt-gnome-team.nautilus-backspace.gschema.xml %buildroot%_datadir/glib-2.0/schemas/

%post
glib-compile-schemas %_datadir/glib-2.0/schemas

%files
%_datadir/nautilus-python/extensions/Back.py
%_datadir/glib-2.0/schemas/io.github.alt-gnome-team.nautilus-backspace.gschema.xml

%changelog
* Thu Apr 4 2024 Alexey Volkov <qualimock@altlinux.org> 0.5.0-alt1
- Initial build for ALT
