%define oname nanosaur2
Name:    Nanosaur2
Version: 2.1.0
Release: alt1

Summary: Nanosaur II source port
License: Creative Commons Attribution-NonCommercialShare Alike 4.0
Group:   Games/Arcade
Url:     https://github.com/jorio/Nanosaur2

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: nanosaur-2_wrapper.sh

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
install -D -m0644 ./packaging/io.jor.%oname.desktop %{buildroot}%_desktopdir/io.jor.%oname.desktop
install -D -m0644 ./packaging/io.jor.%oname.appdata.xml  %buildroot%_datadir/appdata/io.jor.%oname.appdata.xml

for N in 16 32 48 64 128;
do
convert ./packaging/io.jor.nanosaur2.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/io.jor.%oname.png
done

%files 
%doc CHANGELOG.md README.md LICENSE.md
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%_libexecdir/%name/Data/
%_datadir/applications/io.jor.%oname.desktop
%_iconsdir/hicolor/*/apps/io.jor.%oname.png
%_datadir/appdata/io.jor.%oname.appdata.xml

%changelog
* Mon Feb 19 2024 Artyom Bystrov <arbars@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
