Name: seven-gnomes
Version: 0.3
Release: alt3.2

Summary: Seven Gnomes is the helper utility for Cinelerra.
License: GPL
Group: Video
Url: http://www.roxton.kiev.ua/sevengnomes.html
Packager: Igor Vlasenko <viy@altlinux.org>

Source: http://www.roxton.kiev.ua/linux/%name-%version.tar.bz2

# hack!!!
BuildPreReq: libgtk+2-devel >= 2.4
#BuildPreReq: libgtk+2-devel >= 2.6
#Dependencies are: Gtk+2.6 or higher. 

# Automatically added by buildreq on Mon Oct 31 2005
BuildRequires: glib2-devel hostinfo libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
Seven Gnomes is the helper utility for Cinelerra non-linear video editing program. Seven Gnomes is written to speed up some routine actions such as the video indexing or converting. Seven Gnomes acts like a front-end for mpeg3toc and mencoder.


%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Seven Gnomes
GenericName=Seven Gnomes
Comment=%{summary}
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=AudioVideo;Video;AudioVideoEditing;
EOF

%files
%_bindir/*
#%_man1dir/*
%doc AUTHORS ChangeLog README NEWS
%doc doc/en
%_desktopdir/%{name}.desktop

%changelog
* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3.2
- converted debian menu to freedesktop

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3.1
- NMU (by repocop): the following fixes applied:
 * update_menus for seven-gnomes

* Tue Mar 04 2008 Igor Vlasenko <viy@altlinux.ru> 0.3-alt3
- added missing update_menus to pass repocop tests

* Tue Nov 15 2005 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2
- added menu entry

* Mon Oct 31 2005 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- first build for Sisyphus
