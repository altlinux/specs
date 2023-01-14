Name: xsnow
Version: 3.6.0
Release: alt1

Summary: An X Window System based dose of Christmas cheer
License: GPLv3+
Group: Toys

Url: https://www.ratrabbit.nl/ratrabbit/xsnow/index.html
Source: xsnow-%version.tar.gz
Packager: Alexei Mezin <alexvm@altlinux.org>

Summary(ru_RU.UTF8):  Немножко новогоднего настроения на рабочий стол

# Automatically added by buildreq on Wed Jan 01 2020
# optimized out: at-spi2-atk fontconfig glib2-devel glibc-kernheaders-generic libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python-modules python2-base python3 python3-base python3-dev sh4 xorg-proto-devel
###BuildRequires: i586-libxcb libXpm-devel libXt-devel libdb4-devel libdbus-devel libgtk+3-devel libxml2-devel python3-module-mpl_toolkits python3-module-yieldfrom selinux-policy
BuildRequires: libXpm-devel libXt-devel libgtk+3-devel libxml2-devel libdbus-devel gcc-c++ ImageMagick-tools desktop-file-utils libgsl-devel libgsl-devel libXinerama-devel libxkbcommon-devel libXtst-devel

###BuildRequires: gccmakedep imake libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
The Xsnow toy provides a continual gentle snowfall, trees, and Santa
Claus flying his sleigh around the screen.  Xsnow is only for the X
Window System, though; consoles just get coal.

%description -l ru_RU.UTF8
Xsnow добавляет анимированные снежинки и Санту на оленях на рабочий стол.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# create 48x48 pixmap and put icons according to the Policy, see https://www.altlinux.org/Icon_Paths_Policy
convert -resize 48x48 src/Pixmaps/%name.xpm %name.png
install -m 755 -d %buildroot/%_liconsdir/
install -m 755 -d %buildroot/%_iconsdir/hicolor/256x256/apps
install -m 755 -d %buildroot/%_iconsdir/hicolor/scalable/apps
install -m 644 %name.png %buildroot/%_liconsdir/
install -m 644 src/Pixmaps/%name.xpm %buildroot/%_iconsdir/hicolor/256x256/apps
install -m 644 src/Pixmaps/%name.svg %buildroot/%_iconsdir/hicolor/scalable/apps
# fix Category
desktop-file-install --dir %buildroot/%_desktopdir \
    --add-category=Amusement  \
    --set-key=Version --set-value=1.0 \
    %buildroot/%_desktopdir/%name.desktop
    
    
%files
%doc README.md
%_gamesbindir/*
%_man6dir/*
%_liconsdir/%name.*
%_iconsdir/hicolor/256x256/apps/%name.*
%_iconsdir/hicolor/scalable/apps/%name.*
%_desktopdir/*
%_datadir/metainfo/*
%_datadir/pixmaps/xsnow.svg

%changelog
* Sat Jan 14 2023 Alexei Mezin <alexvm@altlinux.org> 3.6.0-alt1
- New version

* Wed Sep 14 2022 Ilya Mashkin <oddity@altlinux.ru> 3.5.2-alt1
- 3.5.2

* Sun Jan 16 2022 Michael Shigorin <mike@altlinux.org> 3.4.3-alt2
- Added explicit BR: desktop-file-utils (older libgio didn't pull it in)

* Sat Jan 15 2022 Alexei Mezin <alexvm@altlinux.org> 3.4.3-alt1
- New version

* Sat Dec 04 2021 Alexei Mezin <alexvm@altlinux.org> 3.3.6-alt1
- New version
- Fix repocop warnings:
 + ALT icons dir policy
 + Freedesktop categories fix

* Sat Nov 20 2021 Alexei Mezin <alexvm@altlinux.org> 3.3.2-alt1
- New version

* Mon Jul 12 2021 Alexei Mezin <alexvm@altlinux.org> 3.3.0-alt1
- New version

* Tue Feb 23 2021 Alexei Mezin <alexvm@altlinux.org> 3.2.2-alt1
- New version

* Fri Sep 04 2020 Alexei Mezin <alexvm@altlinux.org> 3.0.7-alt1
- New version

* Wed Jan 01 2020 Alexei Mezin <alexvm@altlinux.org> 2.0.15-alt1
- New version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.42-alt4.qa1
- NMU: rebuilt for debuginfo.

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.42-alt4
- an icon is now correctly placed 48x48 one (thx repocop)

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 1.42-alt3
- buildreq per repocop proposal
- updated an Url:
- minor spec cleanup

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 1.42-alt2.1
- rebuild (x86_64)

* Mon Feb 28 2005 Victor Forsyuk <force@altlinux.ru> 1.42-alt2
- Updated build deps and patch.

* Thu Dec 26 2002 Michael Shigorin <mike@altlinux.ru> 1.42-alt1
- built for ALT Linux
- based on Red Hat spec; credits:
  Donnie Barnes <djb@redhat.com>
  Erik Troan <ewt@redhat.com>
  Michael Maher <mike@redhat.com>
  Than Ngo <than@redhat.com>
  Tim Powers <timp@redhat.com>
