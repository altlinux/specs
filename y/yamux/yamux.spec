Name: yamux
Version: 60
Release: alt1

Summary: Yandex Music Client

License: GPLv3
Url: https://gitlab.com/KirMozor/Yamux
Group: Sound

# Source-url: https://gitlab.com/KirMozor/Yamux/-/archive/Yamux-v60/Yamux-Yamux-v60.tar.bz2
Source: %name-%version.tar

Source1: %name-nuget_packages-%version.tar

#ExclusiveArch: %_dotnet_archlist
ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-dotnet >= 6.0

Requires: dotnet-6.0

#BuildRequires: gstreamer1.0-devel libgtk4-devel
BuildRequires: dotnet-sdk-6.0

BuildRequires: /proc
Requires: libgtk+3 gstreamer1.0

AutoReq: no
AutoProv: no

%description
Yandex Music Client written in C#.

%prep
%setup -a1

%build
#export NUGET_FALLBACK_PACKAGES="$(pwd)/nuget_packages;/usr/lib/nuget"
export NUGET_FALLBACK_PACKAGES="$(pwd)/nuget_packages"
dotnet publish --output bin --runtime "%_dotnet_rid"  --self-contained false -c Release


%install
mkdir -p %buildroot%_bindir/
#cat <<EOF >%buildroot%_bindir/%name
##!/bin/sh
#exec dotnet %_libdir/%name/Yamux "\$@"
#EOF
ln -s %_libdir/%name/Yamux %buildroot%_bindir/%name

mkdir -p %buildroot%_libdir/%name/
cp -a bin/* %buildroot%_libdir/%name/

cd Yamux

mkdir -p %buildroot%_datadir/%name/
cp -a Svg %buildroot%_datadir/%name/svg

mkdir -p %buildroot%_desktopdir/
cp -a AUR/Yamux.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_pixmapsdir/
cp -a Svg/icon.svg %buildroot%_pixmapsdir/%name.svg

%files
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.svg
%doc Yamux/Docs/technical_requirements.md

%changelog
* Sun Mar 05 2023 Vitaly Lipatov <lav@altlinux.ru> 60-alt1
- initial release for ALT Sisyphus
