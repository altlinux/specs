%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: freefilesync
Version: 14.10
Release: alt1

Summary: Cross-platform file sync utility with GUI (GPL release)
License: GPL-3.0
Group: File tools
Url: https://www.freefilesync.org
VCS: https://github.com/hkneptune/FreeFileSync

Source: %name-%version.tar

# Use patch from AUR https://aur.archlinux.org/packages/freefilesync
Source1: aur-gui.patch
# Use desktop and mime files from Debian testing
Source2: FreeFileSync.desktop
Source3: RealTimeSync.desktop
Source4: FreeFileSync-edit-with.desktop
Source5: freefilesync.xml

# patches from Debian
Patch1: ffs_no_check_updates.patch
Patch2: ffs_allow_parallel_ops.patch

# final local patch with parts from ffs_devuan.patch
Patch100: %name-%version-%release.patch

# fix C++23 deducing this for older GCC (p11)
Patch101: freefilesync-14.8-fix-cxx23-deducing-this.patch

BuildRequires: gcc-c++
BuildRequires: libwxBase3.2-devel
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libidn2)
BuildRequires: /usr/bin/unzip
BuildRequires: /usr/bin/magick

%description
FreeFileSync is a folder comparison and synchronization software that
creates and manages backup copies of all your important files. Instead
of copying every file every time, FreeFileSync determines the
differences between a source and a target folder and transfers only the
minimum amount of data needed. FreeFileSync is Open Source software,
available for Windows, Linux and macOS.

This is the "GPL release" which uses the sources as published by the
author, as opposed to the "FreeFileSync Donation Edition".

%prep
%setup
patch -p1 < %SOURCE1

%patch1 -p1
%patch2 -p1
%patch100 -p1
%patch101 -p1

# In-place patching from https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=freefilesync
sed -i '/DisableAutomaticBoundingBoxUpdates/s|^|//|' wx+/dc.h
sed -i '/soundLog/s|^|//|' FreeFileSync/Source/ui/{batch_status_handler,gui_status_handler,main_dlg}.cpp
sed -i '/zipLog/s|^|//|' FreeFileSync/Source/localization.cpp wx+/image_resources.cpp

echo '#undef wxUSE_EXCEPTIONS' >> zen/i18n.h
sed -i 's|::g_free|g_free|' FreeFileSync/Source/{base/icon_loader.cpp,afs/ftp.cpp} zen/zstring.cpp
sed -i -e's|const override|const|' -e'/animalImg/s|^|//|' FreeFileSync/Source/ui/small_dlgs.cpp
sed -i '/Bind\(.*onStartupUpdateCheck\)/s|^|//|' FreeFileSync/Source/ui/main_dlg.cpp

%build
export CXXFLAGS="%{optflags} -DMAX_SFTP_READ_SIZE=30000 -DMAX_SFTP_OUTGOING_SIZE=30000 \
                 -DwxInfoDC=wxClientDC -DwxReadOnlyDC=wxDC -DwxSYS_COLOUR_GRIDLINES=wxSYS_COLOUR_BTNFACE"
export LDFLAGS="$LDFLAGS `pkg-config --libs gtk+-3.0`"

# FreeFileSync
%make_build -C FreeFileSync/Source exeName=FreeFileSync
# RealTimeSync
%make_build -C FreeFileSync/Source/RealTimeSync exeName=RealTimeSync

%install
# FreeFileSync
install -d %buildroot%_bindir
install -m 0755 FreeFileSync/Build/Bin/FreeFileSync %buildroot%_bindir
install -m 0755 FreeFileSync/Build/Bin/RealTimeSync %buildroot%_bindir

# RealTimeSync
install -d %buildroot%_datadir/%name
install -m 0644 FreeFileSync/Build/Resources/* %buildroot%_datadir/%name

# icons
unzip -u FreeFileSync/Build/Resources/Icons.zip cfg_batch.png database.png start_sync.png FreeFileSync.png RealTimeSync.png
for size in 16 24 32 48 64 128 256; do
  mkdir -p %buildroot%_datadir/icons/hicolor/${size}x${size}/apps ;
  magick FreeFileSync.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/apps/FreeFileSync.png ;
  magick RealTimeSync.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/apps/RealTimeSync.png ;
  mkdir -p %buildroot%_datadir/icons/hicolor/${size}x${size}/mimetypes ;
  magick cfg_batch.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/mimetypes/application-x-freefilesync-batch.png ;
  magick database.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/mimetypes/application-x-freefilesync-db.png ;
  magick start_sync.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/mimetypes/application-x-freefilesync-gui.png ;
  magick RealTimeSync.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/mimetypes/application-x-freefilesync-real.png ;
done

# desktop files
install -d %buildroot%_desktopdir
install -m 0644 %SOURCE2 %buildroot%_desktopdir/
install -m 0644 %SOURCE3 %buildroot%_desktopdir/

install -d %buildroot%_datadir/kservices5/ServiceMenus
install -m 0644 %SOURCE4 %buildroot%_datadir/kservices5/ServiceMenus/

# mime
install -d %buildroot%_datadir/mime/packages
install -m 0644 %SOURCE5 %buildroot%_datadir/mime/packages/

%files
%doc Bugs.txt Changelog.txt License.txt
%_bindir/FreeFileSync
%_bindir/RealTimeSync
%_desktopdir/FreeFileSync.desktop
%_desktopdir/RealTimeSync.desktop
%_datadir/kservices5/ServiceMenus/FreeFileSync-edit-with.desktop
%_datadir/mime/packages/%{name}.xml
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/*/*.png

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 14.10-alt1
- New version 14.10.

* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 14.9-alt1
- New version 14.9.

* Fri Mar 20 2026 Vitaly Lipatov <lav@altlinux.ru> 14.8-alt2
- fix build with GCC 13 (p11): replace C++23 deducing this with traditional recursive lambdas

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 14.8-alt1
- New version 14.8.

* Sun Jan 25 2026 Nikolay Strelkov <snk@altlinux.org> 14.7-alt1
- New version 14.7.

* Fri Dec 05 2025 Nikolay Strelkov <snk@altlinux.org> 14.6-alt1
- New version 14.6.

* Sat Oct 18 2025 Nikolay Strelkov <snk@altlinux.org> 14.5-alt1
- New version 14.5.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 14.4-alt2
- Fixed FTBFS.

* Thu Jul 31 2025 Nikolay Strelkov <snk@altlinux.org> 14.4-alt1
- New version 14.4.

* Sat May 31 2025 Nikolay Strelkov <snk@altlinux.org> 14.3-alt1
- Initial build for Sisyphus
