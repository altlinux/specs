Name: winff
Version: 1.5.3
Release: alt2
Summary: A cross platform batch GUI for FFmpeg
Summary(ru_RU.UTF-8): Кроссплатформенный графический интерфейс для FFmpeg
License: GPLv3
Group: Video
Url: http://code.google.com/p/winff/
Packager: Anton Midyukov <antohami@altlinux.org>
Source: WinFF-%version-source.tar.gz
Source1: winff.desktop
Patch0: winff-presets.patch
Patch1: winff-lpi.patch
Requires: avplay avconv
# Automatically added by buildreq on Fri Sep 04 2015
# optimized out: alternatives cpio crontabs ed elfutils fontconfig fpc-compiler fpc-ide fpc-src fpc-units-base fpc-units-db fpc-units-fcl fpc-units-fv fpc-units-gfx fpc-units-gnome1 fpc-units-gtk fpc-units-gtk2 fpc-units-math fpc-units-misc fpc-units-multimedia fpc-units-net fpc-units-rtl fpc-utils gdb glib-devel glib2-devel gtk-builder-convert gtk-update-icon-cache hwclock libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+2-devel libncurses-devel libode-devel libpango-devel libpng12-devel libwayland-client libwayland-server logrotate makeinfo mariadb-client mkfontdir mkfontscale nfs-utils pkg-config postfix procmail python-base python-devel rpcbind sendmail-common setarch shared-mime-info strace subversion sysvinit-utils termutils texi2dvi time vim-minimal vitmp vixie-cron xauth xkbcomp xmessage xml-utils xorg-rgb xterm xz
BuildRequires: lazarus desktop-file-utils dos2unix
#rpm-utils sisyphus_check fakeroot

%description
WinFF is a GUI for the command line video converter FFMPEG or fork Libav.
It will convert most any video file that FFmpeg or fork Libav will convert.
WinFF does multiple files in multiple formats at one time.
You can for example convert mpeg's, flv's, and mov's
all into avi's all at once.

%description -l ru_RU.UTF-8
WinFF представляет собой графический интерфейс для консольного видео-конвертора
FFMPEG или его форк LibAV. Позволяет конвертивровать видео во все форматы, в
которые поддерживает FFMPEG или его форк LibAV.
WinFF может одновременно конвертировать видео в разные форматы.

%prep
%setup -n WinFF-%version-source
#%%patch0
%patch1
dos2unix *.txt
chmod 644 *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%build
lazbuild \
	--lazarusdir=%_libdir/lazarus \
	--widgetset=gtk2 \
	-B winff.lpr

%install
install -D -m755 winff %buildroot/%_bindir/winff
install -D -m644 %SOURCE1 %buildroot/%_desktopdir/winff.desktop
install -D -m644 presets.xml %buildroot/%_datadir/winff/presets.xml
install -d -m755 %buildroot%_datadir/winff/languages/
install -m644 languages/*.po %buildroot/%_datadir/winff/languages/
install -d -m755 %buildroot/%_mandir/man1/
install -m644 winff.1 %buildroot/%_mandir/man1/
install -d -m755 %buildroot/%_iconsdir/hicolor
for i in 16 24 32 48; do
  install -d -m755 %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
  install -m644 winff-icons/"$i"x"$i"/*.png %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
done
mkdir -p %buildroot/%_docdir/%name
install -m644 -t %buildroot/%_docdir/%name AUTHORS *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%files
%_bindir/winff
%_desktopdir/winff.desktop
%_iconsdir/hicolor/16x16/apps/*
%_iconsdir/hicolor/24x24/apps/*
%_iconsdir/hicolor/32x32/apps/*
%_iconsdir/hicolor/48x48/apps/*
%_datadir/winff
%_mandir/man1/*
%_docdir/%name
#doc AUTHORS *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%changelog
* Mon Jun 20 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt2
- Fixed select the target architecture

* Sun Jun 05 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- New version 1.5.3
- Disable winff-presets.patch.

* Mon Aug 24 2015 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- Initial build for ALT Linux Sisyphus (Closes: 31217).
