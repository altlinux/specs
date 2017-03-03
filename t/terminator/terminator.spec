%add_typelib_req_skiplist typelib(Gnome)
%define ver_major 1.9

Name: terminator
Version: %{ver_major}1
Release: alt1

Summary: Store and run multiple GNOME terminals in one window
Group: Terminals
License: GPLv2
Url: https://launchpad.net/%name

Source: %url/gtk3/%version/+download/%name-%version.tar.gz

# fc patches
Patch: terminator-1.91-fc-fix-desktop-file.patch

BuildArch: noarch

BuildRequires: python-devel intltool rpm-build-gir

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

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name.wrapper
%_bindir/remotinator
%python_sitelibdir_noarch/terminatorlib/
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.*
%_iconsdir/HighContrast/*/*/*.*
%_datadir/pixmaps/%name.png
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.*
%_man5dir/%{name}_config.*
%doc README ChangeLog

%exclude %python_sitelibdir_noarch/%name-%version-py*.egg-info

%changelog
* Fri Mar 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.91-alt1
- 1.91

* Mon Nov 28 2016 Yuri N. Sedunov <aris@altlinux.org> 1.90-alt1
- 1.90

* Sun Sep 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt1
- 0.98

* Mon Nov 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.97-alt1
- first build for Sisyphus

