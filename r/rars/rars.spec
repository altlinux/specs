Name: rars
Version: 1.6
Release: alt4

Summary: RISC-V Assembler and Runtime Simulator

License: MIT
Group: Emulators
Url: https://github.com/TheThirdOne/rars

Source: %name-%version.tar
Source1: jsoftfloat.tar
Patch0001: .gear/0001-Update-pseudo-op-test.patch
Patch0002: .gear/0002-fix-some-typos.patch
Patch0003: .gear/0003-MessagesPane-Force-black-text-color-on-yellow-select.patch
Patch0101: .gear/0101-Made-commandline-memory-accessible-to-observers.patch
Patch0102: .gear/0102-Provide-a-headless-timer-tool.patch
Patch0103: .gear/0103-Provide-command-line-parameter-for-HeadlessTimer.patch
Patch0201: .gear/0201-Fix-64bit-CSR-loading-into-32bit-register.patch
Patch: %name-%version.patch

BuildRequires: java-devel-default ImageMagick-tools
BuildArch: noarch
Obsoletes: %name-javadoc
Requires: java

%description
RARS, the RISC-V Assembler, Simulator, and Runtime, will assemble and
simulate the execution of RISC-V assembly language programs. Its
primary goal is to be an effective development environment for people
getting started with RISC-V.

%prep
%setup -a1
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0201 -p1
%patch -p1

cat > %name.desktop <<@@@
[Desktop Entry]
Name=RARS
GenericName=RISC-V Assembly Language Programming Environment
Comment=Develop in assembly language for the RISC-V family of processors
Exec=%name
Terminal=false
Type=Application
Categories=Development;IDE;Emulator;
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
* Tue Jun 25 2024 Fr. Br. George <george@altlinux.ru> 1.6-alt4
- Fix CSR32 bugfix (quick and dirty)

* Sat Apr 13 2024 Fr. Br. George <george@altlinux.org> 1.6-alt3
- Apply CSR32 bugfix patch

* Wed Apr 03 2024 Fr. Br. George <george@altlinux.org> 1.6-alt2
- Update to master
- Apply headless timer patch

* Sat Feb 10 2024 Fr. Br. George <george@altlinux.org> 1.6-alt1
- Update to release
- Update JSoftFloat to bugfix

* Fri Jun 16 2023 Anton Midyukov <antohami@altlinux.org> 1.5.20220215-alt2
- add 'Requires: java'

* Tue Feb 15 2022 Fr. Br. George <george@altlinux.ru> 1.5.20220215-alt1
- Update co continous branch

* Sun Jan 23 2022 Fr. Br. George <george@altlinux.ru> 1.5-alt3
- Obsolete javadoc package

* Tue Jan 18 2022 Fr. Br. George <george@altlinux.ru> 1.5-alt2
- Provide desktop file

* Wed Dec 15 2021 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Version up
- Import JSoftFloat submodule

* Tue Sep 24 2019 Nikita Ermakov <arei@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus.
