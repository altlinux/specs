Name: vqcc-gtk
Version: 0.5
Release: alt1.qa3
Summary: quickChat/Vypress Chat clone for GTK+
License: GPL
Group: Networking/Chat
Url: http://vqcc-gtk.sf.net
Source0: %name-%version.tar.gz
Patch0: vqcc-gtk-0.5-alt-DSO.patch


# Automatically added by buildreq on Tue Jan 11 2005
BuildRequires: libgtk+2-devel libstartup-notification-devel 
# fontconfig freetype2

%description
Vqcc-gtk is a chat application written in C for the GTK+ toolkit, primarily
used in small LAN's. Based on quickChat/Vypress Chat (TM) for Windows
(from Vypress Research) and is licensed under the GPL.

The application supports both quickChat and Vypress Chat(TM) protocols and
hopefully is compatible enough to substitute those applications when using
Linux, FreeBSD or any other *NIX desktop. You need no server to run, however
it is not possible to communicate outside your LAN (or subnet).

%prep
%setup
%patch0 -p2

%build
%configure 
%make_build

%install
%makeinstall 

# NOTE: old desktop is rewritten; if upgrade versions,
# make sure to merge desktop as well!
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=vqcc-gtk Chat Client
Comment=quickChat/Vypress Chat clone for GTK+
Icon=%{name}
Exec=%name
Terminal=false
Categories=Network;Chat;
StartupNotify=true
EOF


%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%{name}.desktop
%_datadir/pixmaps/*

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.qa3
- Fixed build

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1.qa2
- NMU: converted debian menu to freedesktop

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for vqcc-gtk
  * postclean-05-filetriggers for spec file

* Tue Jan 11 2005 Alexander Borovsky <partizan@altlinux.ru> 0.5-alt1
- First build for Sisyphus

