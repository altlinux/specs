%define _unpackaged_files_terminate_build 1
%define _peainstalldir %_libdir/peazip
%define _peasrc peazip-sources

Name: peazip
Version: 11.1.0
Release: alt1

Summary: File and archive manager
License: LGPL-3.0-only
Group: File tools
Url: https://peazip.github.io/
Vcs: https://github.com/peazip/PeaZip.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: altconf.txt
Patch: %name-%version-alt-add-debuginfo.patch
Patch1: %name-%version-alt-fix-folders-path-ru.patch
Patch2: %name-%version-alt-fix-desktop-files-ru.patch
Patch3: %name-%version-alt-add-PIE.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: dos2unix
BuildRequires: lazarus
BuildRequires: qt6pas-devel
BuildRequires: brotli
BuildRequires: 7-zip
BuildRequires: zstd
BuildRequires: upx
BuildRequires: /proc

%description
PeaZip is a free cross-platform file archiver that provides a unified
portable GUI for many Open Source technologies like 7-Zip, FreeArc, PAQ,
UPX...

%package kf6
Summary: KF6 servicemenu for peazip
Group: Graphical desktop/KDE
BuildArch: noarch

%description kf6
PeaZip is a file and archive manager GUI for many formats.
This subpackage contains the KF6 integration.

%prep
%setup
%autopatch -p1
chmod +w %_peasrc/res/share/lang
dos2unix %_peasrc/readme*
mv -v %_peasrc/res/share/copying/copying.txt .

%build
cd %_peasrc/dev
lazbuild --add-package metadarkstyle/metadarkstyle.lpk
#add additional packages to vanilla lazarus
lazbuild \
 --lazarusdir=%_libdir/lazarus \
%ifarch x86_64
 --cpu=x86_64 \
%endif
 --widgetset=qt6 \
 --max-process-count=1 \
 -B --add-package metadarkstyle/metadarkstyle.lpk
#build peazip
lazbuild \
 --lazarusdir=%_libdir/lazarus \
%ifarch x86_64
 --cpu=x86_64 \
%endif
 --widgetset=qt6 \
 --max-process-count=1 \
 -B project_pea.lpi project_peach.lpi

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_peainstalldir/res/share
cp -v %SOURCE1 %buildroot%_peainstalldir/res/

#install helper apps
mkdir -p %buildroot%_peainstalldir/res/bin/{7z,upx,brotli,zstd}
ln -sf %_bindir/7zz  %buildroot%_peainstalldir/res/bin/7z/7z
ln -sf %_bindir/upx  %buildroot%_peainstalldir/res/bin/upx/upx
ln -sf %_bindir/brotli  %buildroot%_peainstalldir/res/bin/brotli/brotli
ln -sf %_bindir/zstd  %buildroot%_peainstalldir/res/bin/zstd/zstd

#binaries
install %_peasrc/dev/peazip %buildroot%_peainstalldir
ln -sf %_peainstalldir/peazip %buildroot%_bindir/peazip
install %_peasrc/dev/pea %buildroot%_peainstalldir

#icons
mkdir -p %buildroot%_iconsdir/hicolor/256x256/mimetypes
install %_peasrc/res/share/icons/peazip_{7z,rar,zip}.png %buildroot%_iconsdir/hicolor/256x256/mimetypes/
mkdir -p %buildroot%_iconsdir/hicolor/256x256/actions
install %_peasrc/res/share/icons/peazip_{add,extract,browse,convert}.png %buildroot%_iconsdir/hicolor/256x256/actions/
mkdir -p %buildroot%_iconsdir/hicolor/256x256/apps
install %_peasrc/res/share/batch/freedesktop_integration/peazip.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png

#desktop
mkdir -p %buildroot%_datadir/applications
install %_peasrc/res/share/batch/freedesktop_integration/peazip.desktop %buildroot%_datadir/applications/

#help & res
install %_peasrc/res/share/peazip_help.pdf %buildroot%_peainstalldir/res/share/peazip_help.pdf
cp -rv %_peasrc/res/share/{icons,lang,themes,presets} %buildroot%_peainstalldir/res/share/

#kde-servicemenus
mkdir -p %buildroot%_datadir/kio/servicemenus
install %_peasrc/res/share/batch/freedesktop_integration/KDE-servicemenus/KDE6-dolphin/*minimal.desktop %buildroot%_datadir/kio/servicemenus/

%files
%doc %_peasrc/readme.* copying.*
%_bindir/%name
%_iconsdir/hicolor/*/*/*.png
%_datadir/applications/*.desktop
%_peainstalldir

%files kf6
%_datadir/kio/servicemenus/*.desktop

%changelog
* Sat May 16 2026 Anton Kurachenko <srebrov@altlinux.org> 11.1.0-alt1
- New version 11.1.0.

* Sat Dec 27 2025 Anton Kurachenko <srebrov@altlinux.org> 10.8.0-alt1
- New version 10.8.0.

* Tue Nov 18 2025 Anton Kurachenko <srebrov@altlinux.org> 10.7.0-alt3
- BuildRequires: p7zip -> 7-zip.
- PIE enabled.
- Dropped i586 build.

* Fri Nov 14 2025 Anton Kurachenko <srebrov@altlinux.org> 10.7.0-alt2
- Fixed the drop-down menus (Closes: #56862).

* Sat Nov 08 2025 Anton Kurachenko <srebrov@altlinux.org> 10.7.0-alt1
- New version 10.7.0.

* Sat Aug 23 2025 Anton Kurachenko <srebrov@altlinux.org> 10.6.1-alt1
- New version 10.6.1.

* Sat Apr 26 2025 Anton Kurachenko <srebrov@altlinux.org> 10.4.0-alt1.gita1017bc
- New version 10.4.0.

* Sun Feb 23 2025 Anton Kurachenko <srebrov@altlinux.org> 10.3.0-alt1
- New version 10.3.0.

* Sun Jan 19 2025 Anton Kurachenko <srebrov@altlinux.org> 10.2.0-alt1
- New version 10.2.0.

* Sat Nov 23 2024 Anton Kurachenko <srebrov@altlinux.org> 10.1.0-alt2
- Corrected BuildReqs.

* Thu Nov 21 2024 Anton Kurachenko <srebrov@altlinux.org> 10.1.0-alt1
- Initial build for Sisyphus.
