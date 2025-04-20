%define gradle_version 8.10

Name: mindustry
Version: 147.1
Release: alt1
License: GPL-3.0

Summary: The automation tower defense RTS

Group: Games/Strategy

Url: https://github.com/Anuken/Mindustry

# Source-url: https://github.com/Anuken/Mindustry/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# Source1-url: https://github.com/Anuken/Arc/archive/refs/tags/v%version.tar.gz
Source1: %name-arc-%version.tar
Source2: gradle-cache.tar
# Source3-url: https://services.gradle.org/distributions/gradle-%gradle_version-bin.zip
Source3: gradle-bin.zip
Source4: %name.desktop

ExclusiveArch: x86_64 

BuildRequires(pre): /proc rpm-build-java

BuildRequires: java-17-openjdk-devel
BuildRequires: unzip libicns-utils

%description
Create elaborate supply chains of conveyor belts to feed ammo
into your turrets, produce materials to use for building,
and defend your structures from waves of enemies.

Play with your friends in cross-platform multiplayer co-op games,
or challenge them in team-based PvP matches.

%package server
Summary: Server tool for Mindustry
Group: Games/Strategy

%description server 
%summary.

%prep
%setup -a1
unzip %SOURCE3
test -d ~/.gradle && rm -rf ~/.gradle
tar xf %SOURCE2 -C ~

%build
./gradlew pack -Pbuildversion="%version"
./gradlew  --no-daemon dist -Pbuildversion="%version" desktop:dist server:dist

cd core/assets/icons
icns2png --extract icon.icns

%install
install -d %buildroot%_javadir/%name
install -m644 desktop/build/libs/Mindustry.jar %buildroot%_javadir/%name/%name.jar
install -m644 server/build/libs/server-release.jar %buildroot%_javadir/%name/%name-server.jar

install -D %SOURCE4 %buildroot%_desktopdir/%name.desktop

install -d %buildroot%_bindir
cat <<EOF >> %buildroot%_bindir/%name
#!/bin/bash
java -jar %_javadir/%name/%name.jar "\$@"
EOF

cat <<EOF >> %buildroot%_bindir/%name-server
#!/bin/bash
java -jar %_javadir/%name/%name-server.jar "\$@"
EOF

for size in 256 512 1024; do
install -Dm644 "core/assets/icons/icon_${size}x${size}x32.png" \
"%buildroot%_iconsdir/hicolor/${size}x${size}/apps/%name.png"
done

%files
%attr(755,root,root) %_bindir/%name
%_javadir/%name/%name.jar
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/%name.desktop

%files server
%attr(755,root,root) %_bindir/%name-server
%_javadir/%name/%name-server.jar

%changelog
* Sun Apr 20 2025 Kirill Unitsaev <fiersik@altlinux.org> 147.1-alt1
- Initial build
