%define dotnetver 10.0
%define _appdir %_libexecdir/%name

%def_with prebuild

Name:    naps2
Version: 8.6.0
Release: alt2

Summary: Scan documents to PDF and more, as simply as possible
License: GPL-2.0+
Group:   Graphics
Url:     https://github.com/cyanfish/naps2

Source: %name-%version.tar
Patch0: %name-8.2.0-alt-fix-for-libpdfium-soname.patch
Patch1: %name-8.2.1-alt-pdfium-optional.patch
Patch2: %name-8.6.0-alt-framework-dependent.patch
Patch3: %name-8.6.0-alt-narrow-tfm.patch

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: dotnet-sdk-%dotnetver
BuildRequires: /proc
Requires: dotnet-%dotnetver
Requires: libgtk+3
Requires: tesseract
#Recommends: libpdfium0

ExclusiveArch: x86_64

%description
NAPS2 is a document scanning application with a focus on simplicity and ease of
use. Scan your documents from WIA, TWAIN, SANE, and ESCL scanners, organize the
pages as you like, and save them as PDF, TIFF, JPEG, or PNG. Optical character
recognition (OCR) is available using Tesseract.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%if_without prebuild
rm -rf nuget-sources
dotnet restore NAPS2.App.Gtk \
	-p:SelfContained=false \
	-p:DistroTfm=net%dotnetver \
	-p:RestorePackagesPath=./nuget-sources \
	--source ./nuget-sources
%endif

export DOTNET_CLI_TELEMETRY_OPTOUT=true
dotnet publish NAPS2.App.Gtk \
	-c Release-Linux \
	--self-contained false \
	-p:DistroTfm=net%dotnetver \
	--output bin \
	--source ./nuget-sources

%install
install -d %buildroot%_appdir
cp -a bin/. %buildroot%_appdir/
rm -rf %buildroot%_appdir/_win32 %buildroot%_appdir/_win64 %buildroot%_appdir/_winarm \
	%buildroot%_appdir/_mac %buildroot%_appdir/_macarm %buildroot%_appdir/_linuxarm
rm -f %buildroot%_appdir/_linux/libpdfium.so %buildroot%_appdir/_linux/tesseract
find %buildroot%_appdir -name '*.pdb' -delete
install -pDm644 NAPS2.Setup/config/linux/com.naps2.Naps2.desktop \
		%buildroot%_datadir/applications/%name.desktop
install -pDm644 NAPS2.Lib/Icons/scanner_128.png \
		%buildroot%_datadir/icons/hicolor/128x128/apps/com.naps2.Naps2.png
install -pDm644 NAPS2.Setup/config/linux/com.naps2.Naps2.metainfo.xml \
		%buildroot%_datadir/metainfo/com.naps2.Naps2.metainfo.xml
install -pDm644 bin/appsettings.xml %buildroot%_appdir/appsettings.xml

install -d %buildroot%_bindir
ln -sf %_appdir/%name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml
%_appdir

%changelog
* Sun Nov 01 2026 Nikolay Burykin <bne@altlinux.org> 8.6.0-alt2
- use the system .NET runtime instead of bundled self-contained
  (thanks to @lav; closes: #61282)
- narrow TargetFrameworks to the only TFM built
- prune non-Linux natives and pdbs from the package
- add missing Requires: libgtk+3
- use system tesseract for OCR

* Tue Oct 27 2026 Nikolay Burykin <bne@altlinux.org> 8.6.0-alt1
- 8.6.0

* Mon Oct 05 2026 Nikolay Burykin <bne@altlinux.org> 8.4.1-alt1
- 8.4.1

* Mon Sep 07 2026 Nikolay Burykin <bne@altlinux.org> 8.3.2-alt1
- 8.3.2

* Sat Feb 21 2026 Nikolay Burykin <bne@altlinux.org> 8.2.1-alt1
- 8.2.1

* Mon Feb 16 2026 Nikolay Burykin <bne@altlinux.org> 8.2.0-alt4
- fix soname to allow runtime dependency on libpdfium0 instead
  of libpdfium-devel

* Mon Dec 08 2025 Nikolay Burykin <bne@altlinux.org> 8.2.0-alt3
- added missing runtime dependency on libpdfium-devel (Closes: #57042)

* Fri Nov 14 2025 Nikolay Burykin <bne@altlinux.org> 8.2.0-alt2
- fix ftbfs

* Tue Aug 12 2025 Nikolay Burykin <bne@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus (Closes: #51167)
