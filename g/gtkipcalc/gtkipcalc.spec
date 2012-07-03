Name: gtkipcalc
Version: 1.0
Release: alt4.1.qa1

Summary: GUI tool for network calculations
License: GPL
Group: Networking/Other

Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: ru.po

# Automatically added by buildreq on Sun May 18 2008
BuildRequires: gtk+-devel

%description
%name is a simple GUI tool, that can calculate some IP
information, such as default gateway, broadcast address and
address range, by IP and network mask.

%prep
%setup

%build
rm -f po/*.gmo
cp -fv %SOURCE2 po/
%configure
%make_build

%install
%makeinstall
mkdir %buildroot%_desktopdir
install -p -D -m644 %SOURCE1 %buildroot%_desktopdir/

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop

%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%changelog
* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt4.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gtkipcalc
  * postclean-05-filetriggers for spec file

* Sun May 18 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0-alt4.1
- Russian translation updated (Fixes #15698)

* Sun May 18 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0-alt4
- BuildRequires updated (to cleanup XFree86 reference)
- Debian menu -> .desktop
- Spec cleanup

* Mon Nov 18 2002 AEN <aen@altlinux.ru> 1.0-alt3
- rebuilt with gcc-3.2

* Thu Jan 10 2002 Sir Raorn <raorn@altlinux.ru> 1.0-alt2
- BuildRequires tag (but why?)

* Sun Dec 23 2001 Sir Raorn <raorn@altlinux.ru> 1.0-alt1
- Built for Sisyphus

