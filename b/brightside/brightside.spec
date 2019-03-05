Name: brightside
Version: 1.4.0
Release: alt1

Summary: Add reactivity to the corners and edges of your GNOME desktop

Group: System/X11
License: GPL
Url: http://catmur.co.uk/~ed/main/brightside/
Source0: http://home.jesus.ox.ac.uk/~ecatmur/brightside/download/brightside-1.4.0.tar.gz
Patch0: %name-gconf-mouse-speed.patch
Patch1: %name-libwnck.patch

# Automatically added by buildreq on Tue Mar 05 2019
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libdbus-glib libgpg-error perl pkg-config python-base python-modules sh4
BuildRequires: GConf libgtk+3-devel perl-XML-Parser

BuildRequires:	libwnck-devel libglade-devel libgnomeui-devel

%description
Brightside provides "edge flipping" to allow you to switch to the adjacent
workspace simply by pressing your mouse against the edge of the screen.

Besides that Brightside also allows you to assign configurable actions to
occur while you rest the mouse in a corner of the screen.

%prep
%setup
#patch0 -b .patch0
#patch1 -b .libwnck
sed  "s/AdvancedSettings;//
s/[.]png//
" < src/brightside.desktop > brightside.desktop

%build
%configure
%make_build

%install
# For GConf apps: prevent schemas from being installed at this stage
#export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
install -D brightside.desktop %buildroot%_datadir/applications/brightside.desktop
install -D src/brightside-48.png %buildroot%_liconsdir/%name.png
%find_lang Brightside

%files -f Brightside.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_datadir/%name
%_datadir/gconf/schemas/brightside.schemas
%_datadir/pixmaps/brightside-48.png
%_datadir/applications/*.desktop
%_liconsdir/*
%exclude %_datadir/control-center-2.0

%changelog
* Tue Mar 05 2019 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Initial build for ALT

* Sun Apr 02 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.4.0-11
- Update URL
- Use desktop-file-install

* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.4.0-10
- Rebuild for Fedora Extras 5

* Wed Aug 17 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 1.4.0-9
- rebuild

* Thu Jul 21 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 1.4.0-8
- rebuild

* Mon May 23 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 1.4.0-7
- ExcludeArch: ppc ppc64 for now (#158560)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.4.0-6
- rebuild on all arches

* Wed Apr 13 2005 Adrian Reber <adrian@lisas.de> - 1.4.0-5
- added patch from freebsd to compile against newer libwnck:
  http://www.freebsd.org/cgi/cvsweb.cgi/ports/x11/brightside/files/patch-src_brightside.c

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Dec 08 2004 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 0:1.4.0-3
- BR intltool

* Sun Dec 05 2004 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 0:1.4.0-0.fdr.2
- Applied gconf-patch from Adrian Reber

* Tue Nov 30 2004 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> - 0:1.4.0-0.fdr.1
- Initial RPM release.
