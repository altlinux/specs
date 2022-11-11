%define __name sopwith
%define _name sdl-%__name

Name: sdl_%__name
Version: 2.1.1
Release: alt1

Summary: Classic scrolling shoot'em
License: GPLv2+
Group: Games/Arcade
Url: https://github.com/fragglet/sdl-sopwith

Vcs: https://github.com/fragglet/sdl-sopwith.git
Source: %url/releases/download/%_name-%version/%_name-%version.tar.gz
Source1: sopwith.png
Source2: sopwith.desktop

BuildRequires: libSDL2-devel >= 2.0.7 /usr/bin/convert

%description
This is a port of the classic computer game "Sopwith".

%prep
%setup -n %_name-%version

%build
export orig_CFLAGS="%(getconf LFS_CFLAGS)"
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pD -m644 icon.png %buildroot%_pixmapsdir/%__name.png
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%__name.desktop

%files
%_bindir/%__name
%_man5dir/%__name.cfg.*
%_man6dir/%__name.*
%_pixmapsdir/%__name.png
%_desktopdir/%__name.desktop
%doc NEWS* README* doc/origdoc.txt

%exclude %_docdir/%_name

%changelog
* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Fri Sep 02 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0 (new github homepage, ported to SDL2)

* Thu Dec 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.7.4-alt2.qa1
- NMU: rebuilt for debuginfo.

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
