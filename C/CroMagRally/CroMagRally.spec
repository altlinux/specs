Name:    CroMagRally
Version: 3.0.0
Release: alt1

Summary: The wildest racing game since man invented the wheel!
License: Creative Commons Attribution-NonCommercialShare Alike 4.0
Group:   Games/Arcade
Url:     https://github.com/jorio/Nanosaur

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: cromagrally_wrapper.sh

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake libSDL2-devel libGLES-devel ImageMagick-tools

%description
%summary

%prep
%setup

%build

%cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install

install -D -m0755 %_cmake__builddir/%name %{buildroot}/%{_libexecdir}/%name/%name
install -D -m0755 %{SOURCE1} %{buildroot}/%{_bindir}/%name
cp -arv Data/ %{buildroot}/%{_libexecdir}/%name/
install -D -m0644 ./packaging/cromagrally.desktop %{buildroot}%_desktopdir/cromagrally.desktop

for N in 16 32 48 64 128;
do
convert ./packaging/cromagrally-desktopicon.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files 
%doc CHANGELOG.md README.md LICENSE.md
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%_libexecdir/%name/Data/
%_datadir/applications/cromagrally.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Tue Nov 28 2023 Artyom Bystrov <arbars@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
