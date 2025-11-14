%define dotnetver 9.0
%define _appdir %_libexecdir/%name

%def_with prebuild

Name:    naps2
Version: 8.2.0
Release: alt2

Summary: Scan documents to PDF and more, as simply as possible.
License: GPL-2.0+
Group:   Other
Url:     https://github.com/cyanfish/naps2

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: dotnet-sdk-%dotnetver
BuildRequires: /proc

ExclusiveArch: x86_64

%description
NAPS2 is a document scanning application with a focus on simplicity and ease of
use. Scan your documents from WIA, TWAIN, SANE, and ESCL scanners, organize the
pages as you like, and save them as PDF, TIFF, JPEG, or PNG. Optical character
recognition (OCR) is available using Tesseract.

%prep
%setup

%build
sed -i 's#<RuntimeIdentifiers>linux-x64;linux-arm64</RuntimeIdentifiers>#<RuntimeIdentifiers>linux-x64</RuntimeIdentifiers>#' \
    NAPS2.App.Gtk/NAPS2.App.Gtk.csproj

%if_without prebuild
dotnet restore NAPS2.App.Gtk \
	-r linux-x64 \
	-p:SelfContained=true \
	-p:RestorePackagesPath=./nuget-sources
%endif

export DOTNET_CLI_TELEMETRY_OPTOUT=true
dotnet publish NAPS2.App.Gtk \
	-c Release-Linux \
	-r linux-x64 \
	-p:SelfContained=true \
	--output bin \
	--source ./nuget-sources

%install
install -pDm755 bin/naps2 %buildroot%_appdir/%name
install -pDm644 NAPS2.Setup/config/linux/com.naps2.Naps2.desktop \
		%buildroot%_datadir/applications/%name.desktop
install -pDm644 NAPS2.Lib/Icons/scanner-128.png \
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
* Fri Nov 14 2025 Nikolay Burykin <bne@altlinux.org> 8.2.0-alt2
- fix ftbfs

* Tue Aug 12 2025 Nikolay Burykin <bne@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus (Closes: #51167)

