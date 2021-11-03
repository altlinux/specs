%define        pkg_name ratpoison

Name:          %pkg_name
Version:       1.4.9
Release:       alt2

Group:         Graphical desktop/Other
Summary:       ratpoison - Simple window manager with no fat library dependencies
License:       GPL2
Url:           http://www.nongnu.org/ratpoison
# VCS:         https://git.savannah.nongnu.org/git/ratpoison.git

Source:        %name-%version.tar
Source1:       ratpoison-64.xpm
Source2:       ratpoison-16.png

# Automatically added by buildreq on Thu Apr 08 2010 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glibc-pthread libX11-devel libXrender-devel libfreetype-devel pkg-config xorg-inputproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: imake libICE-devel libXext-devel libXft-devel libXi-devel libXinerama-devel libXtst-devel libreadline-devel xorg-cf-files
BuildRequires: libXrandr-devel
BuildRequires(pre): emacs-devel
BuildRequires(pre): emacs-common
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
ratpoison is a simple Window Manager with no fat library
dependencies, no fancy graphics, no window decorations,
and no flashy wank. It is largely modelled after GNU
Screen which has done wonders in virtual terminal market.

All interaction with the window manager is done through
keystrokes. ratpoison has a prefix map to minimize the
key clobbering that cripples EMACS and other quality
pieces of software.


%package       -n emacs-%name
Summary:       The Emacs Lisp bytecode included in %name
Group:         Development/Other
Requires:      %name = %EVR
Requires:      emacs-common

%description   -n emacs-%name
%name-el contains the Emacs Lisp bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.


%package       -n emacs-%name-el
Summary:       The Emacs Lisp sources for bytecode included in %name
Group:         Development/Other
Requires:      emacs-%name = %EVR

%description   -n emacs-%name-el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.


%prep
%setup

%build
%autoreconf
%configure \
    --prefix=%_prefix \
    --infodir=%_infodir \
    --mandir=%_mandir \
		--with-x

%make_build
%byte_compile_file contrib/%pkg_name.el

%install
%makeinstall_std

# startfile
cat > %buildroot/%_bindir/start%name << EOF
#!/bin/sh
exec %_bindir/%name
EOF
chmod 755 %buildroot/%_bindir/start%name

# session file
install -d %buildroot/%_sysconfdir/X11/wmsession.d
install -D -m 644 %SOURCE1 %buildroot%_iconsdir/hicolor/64x64/apps/ratpoison.xpm
install -D -m 644 %SOURCE2 %buildroot%_iconsdir/hicolor/16x16/apps/ratpoison.png
cat > %buildroot/%_sysconfdir/X11/wmsession.d/16%name << EOF
NAME=%name
ICON=%_iconsdir/hicolor/64x64/apps/ratpoison.xpm
EXEC=%_bindir/start%name
DESC=%name window manager
SCRIPT:
exec %_bindir/start%name
EOF
install -d %buildroot/%_datadir/xsessions
cat > %buildroot%_datadir/xsessions/%name.desktop << EOF
[Desktop Entry]
Name=%name
Comment=%name window manager
Icon=%name
Exec=start%name
Type=Application
EOF

install -D -m 644 contrib/%pkg_name.elc %buildroot%_emacslispdir/%pkg_name.elc

%files
%config(noreplace) %_sysconfdir/X11/wmsession.d/16%name
%_defaultdocdir/*
%_bindir/*
%_datadir/%name
%_man1dir/%name.1*
%_infodir/%name.info*
%_miconsdir/ratpoison.png
%_iconsdir/hicolor/64x64/apps/ratpoison.xpm
%_datadir/xsessions/%name.desktop
%doc README TODO AUTHORS NEWS ChangeLog doc/sample.ratpoisonrc doc/ipaq.ratpoisonrc

%files       -n emacs-%name-el
%_emacslispdir/%name.el

%files       -n emacs-%name
%_emacslispdir/%name.elc

%changelog
* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 1.4.9-alt2
- NMU: WM packaging policy 2.0:
- added .desktop
- added 16x16 pixmap

* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.9-alt1
- Bump to version 1.4.9
- Use git repo sources to build
- New subpackages: -n emacs-ratpoison-el, emacs-ratpoison

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.4.8-alt1.git20140917.1
- NMU: added BR: texinfo

* Sun Sep 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.8-alt1.git20140917
- Version 1.4.8

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4.5-alt3.20090912.qa1
- NMU: rebuilt for debuginfo.

* Thu Apr  8 2010 Terechkov Evgenii <evg@altlinux.ru> 1.4.5-alt3.20090912
- Buildreqs updated to fix build

* Thu Nov 26 2009 Terechkov Evgenii <evg@altlinux.ru> 1.4.5-alt2.20090912
- Repocop patch applied

* Sat Sep 12 2009 Terechkov Evgenii <evg@altlinux.ru> 1.4.5-alt1.20090912
- git-20090912

* Sat May 13 2006 Evgenii Terechkov <evg@krastel.ru> 1.4.0-alt1
- 1.4.0
- remove INSTALL and add COPYING to %%doc.
- menu added

* Sun Jan 15 2006 Терешков Евгений <evg@krastel.ru> 1.3.0-alt1
- 1.3.0

* Tue Oct 07 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt2
- rebuild

* Sun Oct 05 2003 Anton V. Denisov <avd@altlinux.org> 1.2.2-alt1.1
- start%name script fixed.
- Automatically added buildreq.
- Spec file tweaks.
- ChangeLog added to %%doc.
- Requires: xvt
- Requires(post,preun): /usr/sbin/install_info
- relocated %%uninstall_info call into %%preun
  as /etc/rpm/macros.d/texinfo suggests.
- TODO: system-wide /etc/ratpoisonrc,
	find ratmenu(1), add Packager tag.

* Sat Jun 21 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt1
- build for ALT

* Sun Jun 15 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.2-1mdk
- 1.2.2
- rm -rf $RPM_BUILD_ROOT in correct stage
- cleanups
- drop lib requires, rpm will figure it out by itself
- drop useless Prefix tag
- drop useless Provides tag
- drop useless libnamifaction stuff (w00t? not a single lib, m0000h!)
- added start and session file
- fix problem with info

* Fri Jan 03 2003 Antoine Ginies <aginies@mandrakesoft.com> 1.1.1-2mdk
- rebuild for new glibc
- correct some spec file problem

* Tue Oct 15 2002 Antoine Ginies <aginies@mandrakesoft.com> 1.1.1-1mdk
- first release for mandrakesoft
