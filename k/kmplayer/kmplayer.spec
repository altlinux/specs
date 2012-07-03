Summary: A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(ru_RU.KOI8-R): Графическая оболочка MPlayer/Xine/ffmpeg/ffserver/VDR для KDE
Name: kmplayer
Version: 0.10.0c
Release: alt3.2
License: GPL
Group: Video
Source0: http://kmplayer.kde.org/pkgs/%name-%version.tar.bz2
Patch0: kmplayer-0.10.0c-alt-DSO.patch
Url: http://kmplayer.kde.org/
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildPreReq: libcairo-devel libdbus-qt-devel libgtk+2-devel
BuildPreReq: libdbus-glib-devel

BuildRequires: fontconfig freetype2 gcc-c++ glib2-devel gstreamer-devel gst-plugins-devel kde-i18n-ru kde-settings kdelibs-devel koffice-devel libjpeg-devel libpng-devel libpopt-devel libqt3-devel libqt3-settings libstdc++-devel libxine-devel libxml2-devel pkg-config xml-utils  zlib-devel libtqt-devel
Requires: kdebase-common >= 3.1.90
Requires: kdelibs >= 3.4.0-4
Requires: MPlayer

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l ru_RU.KOI8-R
Отличный, тесно-интегрируемый с KDE графический интерфейс к 
MPlayer/Xine/ffmpeg/ffserver/VDR

##%package koffice
##Summary: Kmplayer integration with Koffice
##Group: X11/Applications/Multimedia
##Requires: koffice-common

##%description koffice
##Kmplayer integration with Koffice.

%prep
%setup -q -n %name-%version
%patch0 -p2

%__sed -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
        src/kmplayer.desktop \

%build
cp /usr/share/automake/config.sub admin

subst 's,\.la\>,.so,' configure
%configure \
	--disable-rpath \
	--enable-final \
	--without-arts

%__make CXXFLAGS="-I%_includedir/tqtinterface"

%install
%__make install \
	DESTDIR=$RPM_BUILD_ROOT

# menu
install -d %buildroot%_menudir
cat << EOF > %buildroot/%_menudir/%name
?package(%name):command="%_bindir/%name" icon="kmplayer.png" needs="X11" section="Multimedia/Video" title="KMPlayer" longtitle="MPlayer/Xine/ffmpeg/ffserver/VDR GUI for KDE" mimetypes="application/x-kmplayer" hints=""
EOF

# remove bogus translation
#rm -rf $RPM_BUILD_ROOT%_datadir/locale/xx
%find_lang --with-kde %name



%files  -f %name.lang
%doc AUTHORS COPYING README ChangeLog
%_bindir/*
%_libdir/kde3/*
%_libdir/lib*.so
%_menudir/%name
%_datadir/applications/*
%_datadir/apps/*
%_datadir/config/*
%_datadir/doc/*
%_datadir/locale/*/*
#%_datadir/mimelnk/* - conflicts with kaffeine package
%_datadir/mimelnk/application/x-kmplayer.desktop
%_datadir/services/*
%_iconsdir/[!l]*/*/apps/kmplayer.*

##%files koffice
##%defattr(644,root,root,755)
##%_libdir/kde3/libkmplayerkofficepart.la
##%attr(755,root,root) %_libdir/kde3/libkmplayerkofficepart.so
##%_datadir/services/kmplayer_koffice.desktop

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0c-alt3.2
- Fixed build

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0c-alt3.1
- Fixed build

* Sun Apr 17 2011 Ilya Mashkin <oddity@altlinux.ru> 0.10.0c-alt3
- fix build

* Fri Dec 24 2010 Ilya Mashkin <oddity@altlinux.ru> 0.10.0c-alt2
- update requires

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.10.0c-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * desktop-mime-entry for kmplayer
  * update_menus for kmplayer
  * postclean-05-filetriggers for spec file


* Sat Nov 08 2008 Ilya Mashkin <oddity@altlinux.ru> 0.10.0c-alt1
- 0.10.0c

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.9.4a-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for kmplayer

* Sat Apr 21 2007 Ilya Mashkin <oddity@altlinux.ru> 0.9.4a-alt1
- New version 0.9.4a

* Sun Mar 11 2007 Ilya Mashkin <oddity@altlinux.ru> 0.9.4-alt1
- New version 0.9.4

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 0.9.3a-alt2
- fix spec

* Sun Dec 31 2006 Ilya Mashkin <oddity@altlinux.ru> 0.9.3a-alt1
- New version 0.9.3a
- fix #10273, #10574

* Tue Feb 07 2006 X-Stranger <xstranger@altlinux.ru> 0.9.1a-alt2
- fixed build dependencies

* Thu Jan 12 2006 X-Stranger <xstranger@altlinux.ru> 0.9.1a-alt1
- up to new version

* Tue Oct 04 2005 X-Stranger <xstranger@altlinux.ru> 0.9.0c-alt3
- error with glibc-locales dirs including fixed

* Wed Aug 24 2005 X-Stranger <xstranger@altlinux.ru> 0.9.0c-alt2
- conflicting mimelnk-file removed

* Tue Aug 23 2005 X-Stranger <xstranger@altlinux.ru> 0.9.0c-alt1
- up to new build

* Tue Aug 09 2005 X-Stranger <xstranger@altlinux.ru> 0.9.0b-alt1
- up to new build

* Mon Jul 25 2005 X-Stranger <xstranger@altlinux.ru> 0.9.0a-alt1
- built for ALT Linux 
