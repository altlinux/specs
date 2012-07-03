%define pre rc1
Name: mplayerTV
Version: 0.2.1
Release: alt0.1%pre.qa3

Summary: MPlayer TV - PERL/GTK2 frontend

Url: http://www.mplayertv.tk/
License: GPL
Group: Video

Source: http://mplayertv.zer0.hu/downloads/%name-%{version}%pre.tar.bz2

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 17 2005 (-bi)
BuildRequires: fontconfig freetype2 glib2 perl-Glib perl-Gtk2 perl-MPlayer perl-threads

%description
mplayerTV is a PERL/Gtk2 frontend for mplayer. If you have a configured
version of xawtv then mplayerTV uses it's configuration file. mplayerTV
stores your configuration in ~/.mplayertv file. This configuration file
partially compatible with xawtv.


%prep
%setup -q -n %name-%{version}%pre

%install

install -D -v -m 755 mplayerTV %buildroot/%_bindir/mplayerTV
#install -D -v -m 755 mplayerTV.1 %buildroot/%_man1dir/mplayerTV.1

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Mplayer TV
Comment=%summary
Icon=%{name}
Exec=%name
Terminal=false
Categories=AudioVideo;Video;TV;
EOF

%files
%doc README AUTHORS DOCS
%_bindir/%name
%_desktopdir/%{name}.desktop

%changelog
* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt0.1rc1.qa3
NMU: polished desktop file

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt0.1rc1.qa2
- NMU: converted debian menu to freedesktop

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.1-alt0.1rc1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for mplayerTV
  * postclean-05-filetriggers for spec file

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1rc1
- new version (rc1)

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1pre8
- new version

* Sun Apr 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1pre7
- first build for ALT Linux Sisyphus

