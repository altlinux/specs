Name: digger
Version: 20020314
Release: alt4.qa2

Summary: A Game of Digger
License: Distributable
Group: Games/Arcade

Url: http://www.digger.org
Source: %url/%name-%version.tar.gz
Patch: digger-20020314-alt-gcc34.patch

#Packager: Sergey Balbeko <balbeko@altlinux.org> 
#Packager: Michael Shigorin <mike@altlinux.ru>
#Packager: Dima Pashko <troll@watersport.com.ua>


# Automatically added by buildreq on Mon Mar 31 2008
BuildRequires: libSDL-devel zlib-devel libalsa libaudiofile esound

#BuildRequires: XFree86-libs esound libSDL-devel libalsa libaudiofile zlib-devel

%description
Digger is one of most popular games on IBM PC.

%prep
%setup -q
%patch -p1

%build
%make_build -f Makefile.sdl

%install
%__install -pD -m755 digger %buildroot%_gamesbindir/%name

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Digger
GenericName=The Digger
Comment=%{summary}
Icon=%{name}
Exec=%_gamesbindir/%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

echo "Please see %url/faq.html" >> FAQ

%files
%doc digger.txt FAQ
%_gamesbindir/*
%_desktopdir/*

%changelog
* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 20020314-alt4.qa2
- converted debian menu to freedesktop

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20020314-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for digger
  * postclean-05-filetriggers for spec file

* Mon Mar 31 2008 Sergey Balbeko <balbeko@altlinux.org> 20020314-alt4
- rebuilt with xorg

* Sat Feb 26 2005 Michael Shigorin <mike@altlinux.ru> 20020314-alt3
- rebuilt with gcc3.4

* Tue Mar 23 2004 Michael Shigorin <mike@altlinux.ru> 20020314-alt2
- built with gcc3.2

* Wed Sep 24 2003 Michael Shigorin <mike@altlinux.ru> 20020314-alt1
- cleaned up for Sisyphus as Dima seems to be too busy
- added menu file

* Wed Feb 12 2003 Dima Pashko <troll@watersport.com.ua> 0.0.1-alt1
- initial build

