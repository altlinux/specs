Name: rars
Version: 1.5
Release: alt3

Summary: RISC-V Assembler and Runtime Simulator

License: MIT
Group: Emulators
Url: https://github.com/TheThirdOne/rars

Source: %name-%version.tar
Source1: jsoftfloat.tar
Patch: %name-%version.patch

BuildRequires: java-devel-default ImageMagick-tools
BuildArch: noarch
Obsoletes: %name-javadoc

%description
RARS, the RISC-V Assembler, Simulator, and Runtime, will assemble and
simulate the execution of RISC-V assembly language programs. Its
primary goal is to be an effective development environment for people
getting started with RISC-V.

%prep
%setup -a1
%patch -p1

cat > %name.desktop <<@@@
[Desktop Entry]
Name=RARS
GenericName=RISC-V Assembly Language Programming Environment
Comment=Develop in assembly language for the RISC-V family of processors
Exec=%name
Terminal=false
Type=Application
Categories=Development;IDE;Emulator
Icon=%name
@@@

for i in 16 32 48 64 128; do convert src/images/RISC-V.png $i.png; done

%build
export LC_ALL=ru_RU.UTF-8
./build-jar.sh

%install
install -D %name.jar %buildroot%_javadir/%name-%version.jar
ln -s %name-%version.jar %buildroot%_javadir/%name.jar
install -D rars.sh %buildroot%_bindir/rars
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop
for i in 16 32 48 64 128; do
    install -D $i.png %buildroot/%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

%files
%doc *.md src/*.txt src/help/*
%_javadir/*
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/apps/*

%changelog
* Sun Jan 23 2022 Fr. Br. George <george@altlinux.ru> 1.5-alt3
- Obsolete javadoc package

* Tue Jan 18 2022 Fr. Br. George <george@altlinux.ru> 1.5-alt2
- Provide desktop file

* Wed Dec 15 2021 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Version up
- Import JSoftFloat submodule

* Tue Sep 24 2019 Nikita Ermakov <arei@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus.
