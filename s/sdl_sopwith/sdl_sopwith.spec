Name: sdl_sopwith
Version: 1.7.4
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Classic scrolling shoot'em
License: GPLv2+
Group: Games/Arcade

URL: http://sdl-sopwith.sourceforge.net/
Source: http://download.sourceforge.net/sdl-sopwith/sopwith-%version.tar.gz
Source1: sopwith.png
Source2: sopwith.desktop

# Automatically added by buildreq on Wed Sep 08 2010
BuildRequires: libSDL-devel
# Not detected by buildreq:
BuildRequires: libgtk+2-devel

%description
This is a port of the classic computer game "Sopwith".

%prep
%setup -n sopwith-%version

%build

%configure
%make_build

%install
%makeinstall_std
install -pD -m644 %SOURCE1 %buildroot%_pixmapsdir/sopwith.png
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/sopwith.desktop
# remove to avoid warnings about unpackaged files
rm -rf %buildroot/%_docdir/sopwith

%files
%_bindir/*
%_man6dir/*
%_pixmapsdir/*
%_desktopdir/*
# NEWS and ChangeLog now identical
%doc NEWS doc/keys.txt

%changelog
* Sun Oct 31 2010 Victor Forsiuk <force@altlinux.org> 1.7.4-alt2
- Executable name was wrong in desktop file, fix it (closes: #24439).

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 1.7.4-alt1
- 1.7.4

* Mon Feb 02 2009 Victor Forsyuk <force@altlinux.org> 1.7.1-alt4
- Remove obsolete install time scripts.

* Mon Apr 14 2008 Victor Forsyuk <force@altlinux.org> 1.7.1-alt3
- Update menus after package installation.

* Thu May 18 2006 Victor Forsyuk <force@altlinux.ru> 1.7.1-alt2
- Fix FTBFS with gcc4.
- Add desktop file.

* Fri May 13 2005 Victor Forsyuk <force@altlinux.ru> 1.7.1-alt1
- Fix URL.
- Updated buildreqs.

* Mon Oct 07 2002 Kachalov Anton <mouse@altlinux.ru> 1.5.0-alt1
- build for Sisyphus
