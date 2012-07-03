Name:		synkron
Version:	1.6.1
Release:	alt1
Summary:	Is a simple Qt application that allows you to sync folders
License:	GPLv2
Group:		File tools
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://synkron.sourceforge.net/
Source0:	http://kent.dl.sourceforge.net/sourceforge/synkron/Synkron-%version-src.tar.gz

# Automatically added by buildreq on Sun Feb 10 2008 (-bi)
# Manually removed linux-libc-headers packages-info-i18n-common
BuildRequires: ImageMagick gcc-c++ libqt4-devel libqt4-network

%description
Synkron is a simple Qt application that allows you to sync folders,
for example a flash disk with a folder on your hard disk.

Main goals of Synkron:
- Tabs allow you to have more synchronisations running at once.
- Periodical synchronisations automatically sync your folders in selected intervals.
- Restore files, which were overwritten during the synchronisation.
- Add files and folders to black list to make sure they won't be synchronised in the future.
- Make schedules and backup using multisync
- Synkron is Free Software

%prep
%setup -q -n Synkron-%version-src

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" Synkron.pro
lrelease Synkron.pro
%make_build

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name

#Menu
install -d %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Name=Synkron
Comment=Easy folder synchronizer
Comment[ru]=Легкий синхронизатор каталогов
Comment[uk]=Легкий синхронізатор каталогів
Exec=%name
Icon=%name
Terminal=false
Categories=QT;System;FileTools;

EOF

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 images/Synkron128.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 images/Synkron128.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 images/Synkron128.png %buildroot%_miconsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sat Jan 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Sun Sep 27 2009 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt2
- fix Russian translation (closed #21605)

* Fri Jul 17 2009 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sun Dec 21 2008 Motsyo Gennadi <drool@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt2
- delete post/postun scripts (new rpm)

* Wed Oct 01 2008 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Apr 24 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Feb 24 2008 Motsyo Gennadi <drool@altlinux.ru> 1.2.0-alt2
- make and added Russian translation

* Mon Feb 18 2008 Motsyo Gennadi <drool@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Mon Feb 11 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1.0-alt2
- fix crash sheduler (thanks to author for help)

* Sun Feb 10 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux
