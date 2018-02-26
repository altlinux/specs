Name: bbrun
Version: 1.4
Release: alt3.2

Summary: A simple run window with dropdown history list
License: GPL
Group: File tools

Url: http://www.dwave.net/~jking/bbrun/
Source: %name-%version.tar.bz2
Patch: %name-1.4-alt-make.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: gtk+-devel libX11-devel libXext-devel libXpm-devel

%description
BBrun is a run utility for BlackBox which can be run in the slit or
in withdrawn mode so that it can be bound to a keystroke from bbkeys.
It also features a history list of the most recent commands.

%prep
%setup -q
%patch -p1

%build
%make_build -C %name

%install
install -pD -m755 %name/%name %buildroot%_bindir/%name
install -pD -m644 %name/%name.xpm %buildroot%_miconsdir/%name.xpm
ln -s -f /usr/share/license/GPL-2 COPYING
mkdir -p %buildroot%_menudir
cat <<EOF >%buildroot%_menudir/%name
?package(%name): \
	command="%_bindir/%name -w" \
	needs="x11" \
	icon="%name.xpm" \
	section="Applications/File tools" \
	title="BBrun" \
	longtitle=""
EOF

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=BBrun
GenericName=A simple run window
Comment=%{summary}
Icon=%{name}
Exec=%name -w
Terminal=false
Categories=System;FileTools;
EOF


%files
%doc Changelog README
%doc --no-dereference COPYING
%_bindir/%name
%_desktopdir/%{name}.desktop
%_miconsdir/%name.xpm

%changelog
* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3.2
- NMU: converted debian menu to freedesktop

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4-alt3.1
- NMU:
  * updated build dependencies

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.4-alt3
- apply patch from repocop
- buildreq

* Fri Apr 07 2006 Igor Zubkov <icesik@altlinux.ru> 1.4-alt2
- add packager tag
- remove common-licenses from Requires
- buildreq

* Mon Feb 24 2003 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- initial revision
