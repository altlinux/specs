%define _unpackaged_files_terminate_build 1
%define _peainstalldir %_libdir/peazip
%define _peasrc peazip-sources

Name: peazip
Version: 10.1.0
Release: alt2

Summary: File and archive manager
License: LGPL-3.0-only
Group: File tools
Url: https://peazip.github.io/
Vcs: https://github.com/peazip/PeaZip.git

ExclusiveArch: %ix86 x86_64 aarch64

Source: %name-%version.tar
Source1: altconf.txt
Patch: %name-%version-alt-add-debuginfo.patch
Patch1: %name-%version-alt-fix-folders-path-ru.patch
Patch2: %name-%version-alt-fix-desktop-files-ru.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: dos2unix
BuildRequires: lazarus
BuildRequires: qt5pas-devel
BuildRequires: brotli
BuildRequires: p7zip
BuildRequires: zstd
BuildRequires: upx
BuildRequires: /proc

%description
PeaZip is a free cross-platform file archiver that provides a unified
portable GUI for many Open Source technologies like 7-Zip, FreeArc, PAQ,
UPX...

%package kf5
Summary: KF5 servicemenu for peazip
Group: Graphical desktop/KDE
BuildArch: noarch

%description kf5
PeaZip is a file and archive manager GUI for many formats.
This subpackage contains the KF5 integration.

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
 --widgetset=qt5 \
 --max-process-count=1 \
 -B --add-package metadarkstyle/metadarkstyle.lpk
#build peazip
lazbuild \
 --lazarusdir=%_libdir/lazarus \
%ifarch x86_64
 --cpu=x86_64 \
%endif
 --widgetset=qt5 \
 --max-process-count=1 \
 -B project_pea.lpi project_peach.lpi

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_peainstalldir/res/share
cp -v %SOURCE1 %buildroot%_peainstalldir/res/

#install helper apps
mkdir -p %buildroot%_peainstalldir/res/bin/{7z,upx,brotli,zstd}
ln -sf %_bindir/7z  %buildroot%_peainstalldir/res/bin/7z/7z
ln -sf %_bindir/upx  %buildroot%_peainstalldir/res/bin/upx/upx
ln -sf %_bindir/brotli  %buildroot%_peainstalldir/res/bin/brotli/brotli
ln -sf %_bindir/zstd  %buildroot%_peainstalldir/res/bin/zstd/zstd

#binaries
install -m 0755 %_peasrc/dev/peazip %buildroot%_peainstalldir
ln -sf %_peainstalldir/peazip %buildroot%_bindir/peazip
install -m 0755 %_peasrc/dev/pea %buildroot%_peainstalldir

#icons
mkdir -p %buildroot%_iconsdir/hicolor/256x256/mimetypes
install -m 0644 %_peasrc/res/share/icons/peazip_{7z,rar,zip}.png %buildroot%_iconsdir/hicolor/256x256/mimetypes/
mkdir -p %buildroot%_iconsdir/hicolor/256x256/actions
install -m 0644 %_peasrc/res/share/icons/peazip_{add,extract,browse,convert}.png %buildroot%_iconsdir/hicolor/256x256/actions/
mkdir -p %buildroot%_iconsdir/hicolor/256x256/apps
install -m 0644 %_peasrc/res/share/batch/freedesktop_integration/peazip.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png

#desktop
mkdir -p %buildroot%_datadir/applications
install -m 0644 %_peasrc/res/share/batch/freedesktop_integration/peazip.desktop %buildroot%_datadir/applications/

#help & res
install -m 0644 %_peasrc/res/share/peazip_help.pdf %buildroot%_peainstalldir/res/share/peazip_help.pdf
cp -rv %_peasrc/res/share/{icons,lang,themes} %buildroot%_peainstalldir/res/share/

#kde-servicemenus
mkdir -p %buildroot%_K5srv
install -m 0644 %_peasrc/res/share/batch/freedesktop_integration/KDE-servicemenus/KDE5-dolphin/*.desktop %buildroot%_K5srv

%files
%doc %_peasrc/readme.* copying.*
%_bindir/%name
%_iconsdir/hicolor/*/*/*.png
%_datadir/applications/*.desktop
%_peainstalldir

%files kf5
%_K5srv/*.desktop

%changelog
* Sat Nov 23 2024 Anton Kurachenko <srebrov@altlinux.org> 10.1.0-alt2
- Corrected BuildReqs.

* Thu Nov 21 2024 Anton Kurachenko <srebrov@altlinux.org> 10.1.0-alt1
- Initial build for Sisyphus.
