Name: cellwriter
Version: 1.3.4
Release: alt4

Summary: A grid-entry natural handwriting input panel
License: GPLv2+
Group: Text tools

Url: http://risujin.org/cellwriter
Source: %url/%name-%version.tar.gz
Patch: cellwriter-1.3.4-alt-manpage.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Apr 06 2010
BuildRequires: imake libXi-devel libXtst-devel libgnome-devel libgtk+2-devel xorg-cf-files xorg-xextproto-devel

%description
CellWriter is a grid-entry natural handwriting input panel. As
you write characters into the cells, your writing is instantly
recognized at the character level. When you press Enter on the
panel, the input you entered is sent to the currently focused
application as if typed on the keyboard.

%prep
%setup
sed -ri 's,^(LDADD.*)$,\1 -lX11,' Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
install -pD %buildroot%_pixmapsdir/%name.xpm \
	%buildroot%_niconsdir/%name.xpm
rm -f %buildroot%_iconsdir/hicolor/icon-theme.cache
rm -r %buildroot%_pixmapsdir/

%files
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%_niconsdir/%name.xpm
%_iconsdir/*/*/*/*.svg
%_man1dir/*
%doc AUTHORS ChangeLog README TODO

# TODO:
# - 16x16 and 48x48? (%%_miconsdir and %%_liconsdir)

%changelog
* Tue May 29 2012 Michael Shigorin <mike@altlinux.org> 1.3.4-alt4
- fixed FTBFS with binutils-2.22

* Tue Apr 06 2010 Michael Shigorin <mike@altlinux.org> 1.3.4-alt3
- s/FTBFS/buildreq/

* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 1.3.4-alt2
- IconPathsPolicy alignment (32x32/svg only though)
- manpage one-liner fix to get it recognized as such and autocompressed

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.4-alt1.1
- NMU:
  * updated build dependencies

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- fixed BuildRequires

* Wed Feb 06 2008 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sat Nov 10 2007 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux

