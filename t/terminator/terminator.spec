Name: terminator
Version: 0.97
Release: alt1

Summary: Store and run multiple GNOME terminals in one window
Group: Terminals
License: GPLv2
Url: http://gnometerminator.blogspot.com/p/introduction.html

Source: https://launchpad.net/terminator/trunk/%version/+download/terminator-%version.tar.gz
# fc patches
Patch: terminator-0.97-fc-fix-desktop-file.patch
Patch1: terminator-0.97-fc-fix-inactive-colour.patch

BuildArch: noarch

%py_requires vte gconf pynotify keybinder

BuildRequires: python-devel intltool

%description
Multiple GNOME terminals in one window. This is a project to produce an
efficient way of filling a large area of screen space with terminals.
This is done by splitting the window into a resizeable grid of terminals.
As such, you can  produce a very flexible arrangements of terminals for
different tasks.

%prep
%setup
sed -i '/#! \?\/usr.*/d' terminatorlib/*.py
%patch
%patch1

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/remotinator
%python_sitelibdir_noarch/terminatorlib/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_datadir/pixmaps/%name.png
%_man1dir/%name.*
%_man5dir/%{name}_config.*
%doc README ChangeLog

%changelog
* Mon Nov 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.97-alt1
- first build for Sisyphus

