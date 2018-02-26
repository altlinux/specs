Name: gnome-subtitles
Version: 1.0
Release: alt1.git.75.gcf1c9d0
Summary: subtitle editor
License: GPL2
Group: Video
Url: http://gnome-subtitles.sf.net/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.tar
#git://git.gnome.org/gnome-subtitles

# Automatically added by buildreq on Mon Feb 01 2010 (-bi)
BuildRequires: GConf gst-plugins-devel gtk-doc intltool libgnome-sharp mono-mcs python-modules-compiler time
BuildRequires: libgnome-sharp-devel gst-plugins-devel mono-devel libGConf-devel libgtk+2-devel gnome-common

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It supports the
most common text-based subtitle formats and allows for subtitle editing,
translation and synchronization.

%prep
%setup -q -n %name
ln -s /usr/share/gnome-doc-utils/gnome-doc-utils.make . ||:

%build
%autoreconf
%configure
# FIXME: -j 1
make

%install
#chmod -x build/*.dll build/*.exe
%makeinstall_std
# desktop menu and icons
mkdir -p %buildroot%_liconsdir/
mv %buildroot%_pixmapsdir/%name.png %buildroot%_liconsdir/
subst 's|\.png$||' %buildroot%_desktopdir/%name.desktop
subst '/sublibdir/d' %buildroot%_bindir/%name

%find_lang --with-gnome %name

%files -f %name.lang
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_datadir/gnome/help/%name
%_man1dir/%name.*
%doc AUTHORS ChangeLog* MAINTAINERS NEWS README

%changelog
* Fri Oct 15 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt1.git.75.gcf1c9d0
- new version
- fix CVE-2010-3357 (closes: #24316)

* Sun Jan 31 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.9.1_37_gc6041d3-alt1
- upstream switches to GIT
- SubLib adsorbed by this program
- patches merged into upstream

* Sat Mar 14 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.8.git_149_g56dc021-alt1
- new SVN version
- desktop file corrections

* Wed Nov 05 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.8-alt2
- some desktop menu and icons fixes (according to repocop)

* Sat May 17 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.8-alt1
- 1st Sisyphus release
