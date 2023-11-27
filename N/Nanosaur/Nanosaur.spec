Name:    Nanosaur
Version: 1.4.4
Release: alt1

Summary: Nanosaur source port
License: Creative Commons Attribution-NonCommercialShare Alike 4.0
Group:   Games/Arcade
Url:     https://github.com/jorio/Nanosaur

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: nanosaur_wrapper.sh

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
install -D -m0644 ./packaging/io.jor.nanosaur.desktop %{buildroot}%_desktopdir/io.jor.nanosaur.desktop
install -D -m0644 ./packaging/io.jor.nanosaur.appdata.xml  %buildroot%_datadir/appdata/io.jor.nanosaur.appdata.xml

for N in 16 32 48 64 128;
do
convert ./packaging/Nanosaur.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files 
%doc CHANGELOG.md README.md LICENSE.md
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%_libexecdir/%name/Data/
%_datadir/applications/io.jor.nanosaur.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/appdata/io.jor.nanosaur.appdata.xml

%changelog
* Mon Nov 27 2023 Artyom Bystrov <arbars@altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus
