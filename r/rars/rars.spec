Name: rars
Version: 1.5
Release: alt2

Summary: RISC-V Assembler and Runtime Simulator

License: MIT
Group: Emulators
Url: https://github.com/TheThirdOne/rars

Source: %name-%version.tar
Source1: jsoftfloat.tar
Patch: %name-%version.patch

BuildRequires: java-devel-default ImageMagick-tools
BuildArch: noarch
Requires: java-openjdk

%description
RARS, the RISC-V Assembler, Simulator, and Runtime, will assemble and
simulate the execution of RISC-V assembly language programs. Its
primary goal is to be an effective development environment for people
getting started with RISC-V.

%package javadoc
Group: Documentation
Summary: Javadoc for %name

%description javadoc
Documentation and license for %name.

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
# jar and launcher
install -d -m 755 %{buildroot}%{_javadir}/
install -d -m 755 %{buildroot}%{_bindir}/
cp -p %name.jar %{buildroot}%{_javadir}/%name-%version.jar
ln -s %name-%version.jar %{buildroot}%{_javadir}/%name.jar
cp -p rars.sh %{buildroot}%{_bindir}/rars

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr License.txt README.md %{buildroot}%{_javadocdir}/%{name}/
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop
for i in 16 32 48 64 128; do
    install -D $i.png %buildroot/%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

%files
%_javadir/*
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/apps/*

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
* Tue Jan 18 2022 Fr. Br. George <george@altlinux.ru> 1.5-alt2
- Provide desktop file

* Wed Dec 15 2021 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Version up
- Import JSoftFloat submodule

* Tue Sep 24 2019 Nikita Ermakov <arei@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus.
