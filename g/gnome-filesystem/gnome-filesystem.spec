Name: gnome-filesystem
Version: 2.20.0
Release: alt0.1

Summary: Filesystem entries common to GNOME packages
License: %gpl3plus
Group: Graphical desktop/GNOME

BuildArch: noarch
BuildPreReq: rpm-build-gnome >= 0.7
BuildPreReq: rpm-build-licenses

%description
This package contains filesystem entries used by various GNOME packages.

%install
mkdir -p %buildroot%gnomehelpdir
mkdir -p %buildroot%_datadir/gnome/wm-properties
mkdir -p %buildroot%gnome_autostartdir

%files
%dir %_datadir/gnome
%dir %gnomehelpdir
%dir %_datadir/gnome/wm-properties
%dir %gnome_autostartdir

%changelog
* Mon Nov 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.0-alt0.1
- Added %_datadir/gnome/wm-properties (moved here from metacity) and
  %gnome_autostartdir (from gnome-session).

* Thu May 03 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt0.1
- Use macros from rpm-build-gnome package.

* Sun Sep 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- Initial Sisyphus release.
- Beginning with /usr/share/gnome and /usr/share/gnome/help directories.

