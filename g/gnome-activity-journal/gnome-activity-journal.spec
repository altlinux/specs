%define major 0.8

Name: gnome-activity-journal
Version: %major.0
Release: alt1

Summary: Browse and search your Zeitgeist activities

Group: Office
License: GPLv3+
Url: https://launchpad.net/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://launchpad.net/%name/%major/%version/+download/%name-%version.tar

# Simple patch to get rid of rpmlint error about non-executable script
Patch1: %name-non-executable-script-fix.patch

BuildArch: noarch

Requires: zeitgeist >= 0.5.0

PreReq: GConf

# required by zeitgeist extension (internal requirement)
%add_python_req_skip _zeitgeist

# Automatically added by buildreq on Sun Oct 24 2010
BuildRequires: intltool python-module-distutils-extra python-module-paste python-module-peak
BuildRequires: libGConf-devel

%description
GNOME Activity Journal is a tool for easily
browsing and finding files on your computer.
It shows a chronological journal of all file
activity.

%prep
%setup
%patch1 -p1

%build
%python_build

%install
%python_install

%find_lang %name

# FIXME: why do no install?
install -m644 -D build/share/gconf/schemas/%name.schemas %buildroot%_sysconfdir/gconf/schemas/%name.schemas
install -m644 -D build/share/applications/%name.desktop %buildroot/%_desktopdir/%name.desktop

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
   %gconf2_uninstall %name
fi

%files -f %name.lang
%doc README AUTHORS
%_bindir/*
%_datadir/gnome-activity-journal
%_iconsdir/hicolor/*/*/*
%_pixmapsdir/*
%_desktopdir/*
%_man1dir/*
%python_sitelibdir/*
%_datadir/zeitgeist/_zeitgeist/engine/extensions/gnome_activity_journal.*
%_sysconfdir/gconf/schemas/%name.schemas

%changelog
* Tue Jan 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script) (ALT bug #26820)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0.1-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.0.1-alt1
- initial build for ALT Linux Sisyphus

* Tue Sep 28 2010 Mads Villadsen <maxx@krakoa.dk> - 0.5.0.1-1
- Update to 0.5.0.1
- Fixes issues with hamster-applet
- Removes some debug output
- Minor bugfixes

* Mon Aug 23 2010 Mads Villadsen <maxx@krakoa.dk> - 0.5.0-1
- Update to latest release
- Add minor patch to make the version check work with zeitgeist 0.5.0

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4.1-2.20100721bzr1010
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 21 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.4.1-1.20100721bzr1010
- Use a bzr version to get g-a-j working with new hamster-applet

* Sun May  9 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.4-1
- Update to latest release
- Fixes bugs #579024, #579148, #579144, #580740, #580309, #591444
- Don't use --skip-build in install target as it breaks various part of the installation
- Removed the install patch as the installation is better behaved now
- Removed the startup shell script as it is no longer needed

* Sun Feb 21 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.3-1
- Update to new release
- Added a patch for better installation
- spec file updated to handle GConf schema, icons, languages, more
- Add intltool to BuildRequires

* Fri Jan 22 2010 Mads Villadsen <maxx@krakoa.dk> - 0.3.2-1
- Initial package

