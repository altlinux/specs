Name:		doublecmd
Summary:	Twin-panel (commander-style) file manager (GTK2)
Version:	0.5.4
Release:	alt1
Url:		http://doublecmd.sourceforge.net

Packager:	Motsyo Gennadi <drool@altlinux.ru>

Source0:	%name-%version.tar
License:	GPLv2
Group:		File tools

BuildRequires: fpc >= 2.4.0 fpc-src glib2-devel libgtk+2-devel lazarus >= 0.9.29
BuildRequires: libncurses-devel
BuildRequires: libdbus-devel
BuildRequires: bzlib-devel
BuildRequires: gdk-pixbuf-devel
BuildRequires: xorg-proto-devel
BuildRequires: xorg-xtrans-devel

Provides: doublecmd
Obsoletes: doublecmd < 0.4.6 doublecmd-qt

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%prep
%setup

%build
./build.sh beta gtk2

# To fix ... "oblom" ... when processing install ;)
%set_verify_elf_method textrel=relaxed

%install
install/linux/install.sh --install-prefix=%buildroot

%files
%_libdir/%name
%_bindir/%name
%_datadir/%name
%_man1dir/%name.*
%_pixmapsdir/%name.*
%_desktopdir/%name.desktop

%changelog
* Wed Feb 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.4-alt1
- build for Sisyphus

* Tue Dec 11 2012 Motsyo Gennadi <drool@altlinux.ru> 0.5.4-alt0.M60T.1
- build for t6 (thank for src.rpm to Anatoly Chernov)

* Mon Oct 22 2012 - Anatoly Chernov <aichernov@umail.ru>
- New beta release 0.5.4-3.3 (beta 16.10.2012) with no problem ... :)

* Sun Jun 24 2012 - Anatoly Chernov <aichernov@umail.ru>
- Initial package, version 0.5.4 beta (with new Lazarus) and fix the problem:
- at first:... (hi!)
- /usr/bin/ld: warning: creating a DT_TEXTREL in a shared object.
- ... (skip about 3000 lines) ...
- and later on: ...
- verify-elf: ERROR: ... : TEXTREL entry found: 0x00000000
- RPM build errors: ... ;)
- ...
- assembler ... "blin"
- see http://lists.altlinux.org/pipermail/devel/2012-June/194625.html

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6
