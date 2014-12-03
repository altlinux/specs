Name: minitube
Version: 2.3
Release: alt3
Summary: YouTube desktop client
License: LGPL
Group: Video
Url: http://flavio.tordini.org/minitube
Packager: Konstantin Artyushkin <akv@altlinux.org>
Source0: %name-%version.tar
Source1: minitube.desktop
Patch0: phononinclude.patch
Patch1: locals.patch

BuildRequires: gcc-c++ libqt4-devel phonon-devel
# have some conflict with gstremer and vlc backends
# And have conflicts pulse and alsa
#Requires: phonon-backend-3-vlc

%description
Minitube is a YouTube desktop client.

With it you can watch YouTube videos in a new way: you type a keyword,
Minitube gives you an endless video stream.

Minitube is not about cloning the original YouTube web interface, it aims
to create a new TV-like experience.

%prep
%setup
%patch0 -p1
#%%patch1 -p1

%build
for i in $(ls data| grep x); do
		mkdir data/$i/apps;
		mv -f data/$i/minitube.png data/$i/apps
		done
qmake-qt4 \
PREFIX=/usr \
INCLUDEPATH=/usr/include/kde4 \
-after QMAKE_CFLAGS='%optflags' \
-after QMAKE_CXXFLAGS='%optflags'

%make_build
%install
#ls -R 
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_desktopdir
mkdir -p %buildroot%_datadir/%name/locale
mkdir -p %buildroot%_iconsdir/hicolor/scalable

#%%makeinstall_std

install -m 0755 build/target/minitube %buildroot%_bindir
install -m 0755 build/target/locale/* %buildroot%_datadir/%name/locale
install -m 0755 %SOURCE1 %buildroot%_desktopdir

cp -rf data/* %buildroot%_iconsdir/hicolor
cp -f data/minitube.svg %buildroot%_iconsdir/hicolor/scalable

rm -f %buildroot%_iconsdir/hicolor/minitube.svg


%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/minitube.png
%_iconsdir/hicolor/scalable/minitube.svg
%_datadir/%name

%changelog
* Wed Dec 03 2014 Konstantin Artyushkin <akv@altlinux.org> 2.3-alt3
-  2.3 

* Wed Aug 13 2014 Konstantin Artyushkin <akv@altlinux.org> 2.2-alt2
- - fix icons

* Wed Aug 13 2014 Konstantin Artyushkin <akv@altlinux.org> 2.2-alt1
- update  to 2.2

* Thu Jun 03 2013 bla-bla <bla-bla@altlinux.org> 2.1.5-alt1.M70P.2
- 2.1.5

* Thu Jun 03 2013 bla-bla <bla-bla@altlinux.org> 2.1-alt1.M70P.1
- 2.1 

* Tue Mar 19 2013 bla-bla <bla-bla@altlinux.org> 2.0-alt0.M60P.1
- 2.0 

* Fri Sep 28 2012 bla-bla <bla-bla@altlinux.org> 1.9-alt0.M60P.1
- 1.9

* Mon Sep 24 2012 bla-bla <bla-bla@altlinux.org> 1.8-alt1.M60P.1
- 1.8

* Mon Feb 20 2012 Mykola Grechukh <gns@altlinux.ru> 1.7-alt1
- 1.7

* Fri Nov 25 2011 Egor Glukhov <kaman@altlinux.org> 1.6-alt1
- 1.6

* Sun Aug 21 2011 Egor Glukhov <kaman@altlinux.org> 1.5-alt1
- 1.5

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 1.4.3-alt1
- new version

* Fri Jan 14 2011 Egor Glukhov <kaman@altlinux.org> 1.3-alt1
- 1.3

* Fri Sep 10 2010 Egor Glukhov <kaman@altlinux.org> 1.1-alt1.git.da913cd7
- Initial build for Sisyphus
