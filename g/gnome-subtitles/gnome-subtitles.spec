Name: gnome-subtitles
Version: 1.3
Release: alt1
Summary: subtitle editor
License: GPL2
Group: Video
Url: http://gnome-subtitles.sf.net/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.tar
#git://git.gnome.org/gnome-subtitles

# Automatically added by buildreq on Thu Jun 20 2013 (-bi)
# optimized out: GConf docbook-dtds elfutils glib2-devel gnome-doc-utils-xslt gstreamer1.0-devel libdbus-glib libgpg-error libgst-plugins1.0 libgtk-sharp2 mono mono-csharp mono-mcs mono-mscorlib monodis perl-XML-Parser pkg-config python-base python-module-distribute python-module-libxml2 python-module-zope python-modules python-modules-compiler python-modules-encodings rpm-build-mono xml-common xml-utils xsltproc
BuildRequires: gnome-doc-utils gst-plugins1.0-devel gtk-doc intltool libgnome-sharp mono-devel mono-web time
BuildRequires: libgnome-sharp-devel mono-devel libGConf-devel libgtk+3-devel gnome-common

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It supports the
most common text-based subtitle formats and allows for subtitle editing,
translation and synchronization.

%prep
%setup -n %name
ln -s %_datadir/gnome-doc-utils/gnome-doc-utils.make . ||:

%build
%autoreconf
%configure
# FIXME: -j 1
make

%install
#chmod -x build/*.dll build/*.exe
%makeinstall_std
# desktop menu and icons
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps/
mv %buildroot%_pixmapsdir/*.svg %buildroot%_iconsdir/hicolor/scalable/apps/
%__subst '/sublibdir/d' %buildroot%_bindir/%name

%find_lang --with-gnome %name

%files -f %name.lang
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/gnome/help/%name
%_man1dir/%name.*
%doc AUTHORS ChangeLog* MAINTAINERS NEWS README

%changelog
* Thu Jun 20 2013 Ildar Mulyukov <ildar@altlinux.ru> 1.3-alt1
- new version with gtk+3 interface

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.git.75.gcf1c9d0.qa1
- NMU: rebuilt for debuginfo.

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
