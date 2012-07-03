Name: atomix
Version: 2.14.0
Release: alt7

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Little mind game where you have to build molecules out of atoms lying around
License: GPLv2+
Group: Games/Puzzles

Url: http://ftp.gnome.org/pub/GNOME/sources/atomix/2.14
Source: %url/atomix-%version.tar.bz2
Source1: atomix-icon16.png
Source2: atomix-icon48.png
Patch1: atomix-2.14.0-desktop.patch

# Automatically added by buildreq on Tue Oct 19 2010
BuildRequires: libgnomeui-devel libxml2-devel perl-XML-Parser

%description
Atomix is a little game where you have to build molecules out of single atoms
laying around. The game is inspired by the orignal Amiga version.

%prep
%setup
%patch1 -p1

%build
%configure
# gnome bz#334319 -- translations don't get built; use Fedora workaround for that
subst 's!^SOURCES = !&\n'"$(grep "^CATALOGS" po/Makefile.in)"'!' po/Makefile
%make_build

%install
%makeinstall_std
install -pDm644 atomix-icon.png %buildroot%_niconsdir/atomix-icon.png
install -pDm644 %_sourcedir/atomix-icon16.png %buildroot%_miconsdir/atomix-icon.png
install -pDm644 %_sourcedir/atomix-icon48.png %buildroot%_liconsdir/atomix-icon.png

%find_lang atomix

%files -f atomix.lang
%attr(2711,root,games) %_bindir/atomix
%_datadir/atomix/
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/gnome-2.0/*
%_desktopdir/atomix.desktop
%attr(0664,games,games) %_localstatedir/games/atomix.scores

%changelog
* Tue Oct 19 2010 Victor Forsiuk <force@altlinux.org> 2.14.0-alt7
- Refresh BuildRequires.

* Fri Jan 09 2009 Victor Forsyuk <force@altlinux.org> 2.14.0-alt6
- Fixed build of translations.

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 2.14.0-alt5
- Removed obsolete %%post* scripts.

* Tue Jun 24 2008 Victor Forsyuk <force@altlinux.org> 2.14.0-alt4
- Fix additional category in desktop file.

* Tue Sep 25 2007 Victor Forsyuk <force@altlinux.ru> 2.14.0-alt3
- Add required menu updating scripts.

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 2.14.0-alt2
- Update build requirements (libSM-devel now have to be listed explicitly).

* Fri Apr 13 2007 Victor Forsyuk <force@altlinux.org> 2.14.0-alt1
- Initial build.
