Name: grsync
Version: 1.2.1
Release: alt1

Summary: Grsync is a GUI for rsync
License: GPLv2
Group: Networking/Other

Url: http://www.opbyte.it/grsync
Source: http://www.opbyte.it/release/grsync-%version.tar.gz
# Made from upstream grsync.png by ImageMagick's convert with -unsharp 0x1
Source1: grsync16.png
Source2: grsync32.png
Source3: grsync48.png
Patch1: grsync-1.0.0-desktop.patch

Requires: rsync

# Automatically added by buildreq on Sun Jan 15 2012
BuildRequires: intltool libgtk+2-devel

%description
Grsync is a GUI (Graphical User Interface) for rsync, the command line file and
directory synchronization tool.

%prep
%setup
%patch1 -p1

%build
# Tiny fix for Icon= line in desktop file (make validator happy)
subst 's/grsync.png/grsync/' configure
%configure --disable-unity
%make_build

%install
%makeinstall_std

install -pD -m644 %_sourcedir/grsync48.png %buildroot%_liconsdir/grsync.png
install -pD -m644 %_sourcedir/grsync32.png %buildroot%_niconsdir/grsync.png
install -pD -m644 %_sourcedir/grsync16.png %buildroot%_miconsdir/grsync.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_datadir/grsync
%_xdgmimedir/packages/*
%_desktopdir/grsync.desktop
%_pixmapsdir/*.png
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/48x48/mimetypes/*

%changelog
* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 1.1.0-alt1
- 1.1.0

* Fri Feb 05 2010 Victor Forsiuk <force@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Nov 26 2009 Victor Forsyuk <force@altlinux.org> 0.9.3-alt1
- 0.9.3
- Fixed all repocop warnings.

* Sun Jul 27 2008 Terechkov Evgenii <evg@altlinux.ru> 0.6.1-alt1
- 0.6.1
- Packager tag added to spec

* Fri Aug 24 2007 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt1
- 0.6

* Fri Feb 16 2007 Terechkov Evgenii <evg@altlinux.ru> 0.5.2-alt1
- 0.5.2
- Obsolete Patch1 droped (fixed in upstream)

* Sun Jan 14 2007 Terechkov Evgenii <evg@altlinux.ru> 0.5.1-alt1
- 0.5.1
- Obsoleted patch1 and source1 dropped
- New patch1 enhances russian translation

* Thu Jan 11 2007 Terechkov Evgenii <evg@altlinux.ru> 0.5-alt2
- Russian translation added
- Spec cleanups
- Some docs added
- Patch1 replaced (fixed in upstream) by new (to enable Russian tranlation)

* Wed Aug 09 2006 Igor Zubkov <icesik@altlinux.ru> 0.5-alt1
- 0.4.3 -> 0.5
- add rsync to Requires

* Wed Jun 28 2006 Igor Zubkov <icesik@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Fri May 19 2006 Igor Zubkov <icesik@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Sat May 06 2006 Igor Zubkov <icesik@altlinux.ru> 0.4.1-alt1
- Initial build for Sisyphus
