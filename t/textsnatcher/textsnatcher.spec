%define oname TextSnatcher

Name: textsnatcher
Version: 2.0.0
Release: alt1

Summary: Copy Text from Images with ease, perform OCR operations in seconds

License: GPLv3
Group: Text tools
Url: https://github.com/RajSolai/TextSnatcher

# Source-url: https://github.com/RajSolai/TextSnatcher/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: vala

#BuildRequires: granite-vala
BuildRequires: vapi(granite)

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(tesseract)

Requires: scrot
Requires: tesseract

Requires: tesseract-langpack-ru tesseract-langpack-en

%description
Copy Text from Images with ease, perform OCR operations in seconds.

Install tesseract-langpack-* to get support other languages.

%files
%_bindir/%name
%_bindir/com.github.rajsolai.%name
%_datadir/metainfo/com.github.rajsolai.%name.appdata.xml
%_desktopdir/com.github.rajsolai.%name.desktop
%_iconsdir/hicolor/*/apps/*

#------------------------------------------------------------------

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
ln -s %_bindir/com.github.rajsolai.%name %buildroot%_bindir/%name

%changelog
* Sun Mar 17 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Sisyphus

