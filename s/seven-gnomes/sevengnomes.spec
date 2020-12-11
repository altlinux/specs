# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize
# END SourceDeps(oneline)
Name: seven-gnomes
Version: 0.5
Release: alt3

Summary: Seven Gnomes is the helper utility for Cinelerra.
License: GPL
Group: Video
Url: http://semiletov.org/sevengnomes.html
Packager: Igor Vlasenko <viy@altlinux.org>

Source: http://semiletov.org/sources/%name-%version.tar

BuildRequires: glib2-devel hostinfo libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
Seven Gnomes is the helper utility for Cinelerra non-linear video editing program. Seven Gnomes is written to speed up some routine actions such as the video indexing or converting. Seven Gnomes acts like a front-end for mpeg3toc and mencoder.


%prep
%setup -q

%build
%add_optflags -fcommon
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

rm -rf %buildroot/usr/share/seven-gnomes/doc/en

%files
%_bindir/*
#%_man1dir/*
%doc AUTHORS ChangeLog README NEWS
%doc doc/en
%_desktopdir/%{name}.desktop

%changelog
* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3
- fixed build

* Sat Jun 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2
- fixed unpackaged files

* Fri May 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- new version

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
