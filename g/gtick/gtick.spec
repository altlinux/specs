Name: gtick
Version: 0.5.1
Release: alt1

Summary: GTick is a GTK+ 2 metronome
License: GPLv3
Group: Sound
Url: http://www.antcom.de/%name

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://savannah.nongnu.org/download/%name/default.pkg/%version/%name-%version.tar.gz
Source1: %name-48x48.xpm
Source2: %name-32x32.xpm
Source3: %name-16x16.xpm

# Automatically added by buildreq on Sat Feb 17 2007
BuildRequires: flex libgtk+2-devel libsndfile-devel libpulseaudio-devel glib2-devel

%description
GTick is a metronome application written for GNU/Linux and other
UN*X-like operting systems supporting different meters (Even, 2/4, 3/4,
4/4 and more) and speeds ranging from 30 to 250 bpm. It utilizes GTK+ 2
and OSS (ALSA compatible).

%prep
%setup -q

%build
%configure --disable-rpath

%make_build

%install
%makeinstall

# menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=GTick
GenericName=A Metronome Application
Comment=%{summary}
Icon=%{name}
Exec=%name
Terminal=false
Categories=AudioVideo;Audio;Music;
EOF

%__install -pD -m644 %SOURCE1 %buildroot%_liconsdir/%name.xpm
%__install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
%__install -pD -m644 %SOURCE3 %buildroot%_miconsdir/%name.xpm

%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_liconsdir/*.xpm
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_desktopdir/%{name}.desktop

%doc AUTHORS ChangeLog NEWS THANKS README TODO

%changelog
* Thu Apr 12 2012 Ilya Mashkin <oddity@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1.qa2
NMU: polished desktop file

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for gtick
  * update_menus for gtick
  * postclean-05-filetriggers for spec file

* Wed Jan 16 2008 Alex V. Myltsev <avm@altlinux.ru> 0.4.1-alt1
- New version: GPLv3, translations update, segfault fix.

* Wed May 09 2007 Alex V. Myltsev <avm@altlinux.ru> 0.3.15-alt1
- 0.3.15: translations update.

* Sat Feb 17 2007 Alex V. Myltsev <avm@altlinux.ru> 0.3.13-alt1
- 0.3.13.

* Sat May 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Tue Dec 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.10-alt1
- 2.0.10

* Tue Oct 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.6-alt1
- 2.0.6

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.4-alt1
- new version.

* Sat Aug 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt1
- First build for Sisyphus.
- summary, description by avp.
