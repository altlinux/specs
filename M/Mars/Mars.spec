Group: Emulators

BuildRequires(pre): rpm-macros-java
# Automatically added by buildreq on Sun Jan 23 2022
# optimized out: ant-lib javapackages-tools javazi libgpg-error python3-base sh4
BuildRequires: ant java-headless unzip ImageMagick-tools
BuildRequires: /proc rpm-build-java

Name: Mars
Version: 4.5
Release: alt6
Summary: An interactive development environment for programming in MIPS assembly language

License: MIT
Url: http://courses.missouristate.edu/KenVollmar/MARS/
Source0: http://courses.missouristate.edu/KenVollmar/mars/MARS_4_5_Aug2014/Mars4_5.jar
Source3: build.xml
BuildArch: noarch

%description
MARS is a lightweight interactive development environment (IDE) for
programming in MIPS assembly language, intended for educational-level
use with Patterson and Hennessy's Computer Organization and Design.

%prep
%setup -c %name-%version
rm *.class

cat > %name.desktop <<@@@
[Desktop Entry]
Name=MARS
GenericName=MIPS Assembly Language Programming Environment
Comment=Develop in assembly language for the MIPS family of processors
Exec=%name
Terminal=false
Type=Application
Icon=%name
Categories=Development;IDE;Emulator
@@@

cat > %name.sh <<@@@
#!/bin/sh
#
# Mars script
# JPackage Project <http://www.jpackage.org/>

# Source functions library
_prefer_jre="true"
. /usr/share/java-utils/java-functions

# Configuration
MAIN_CLASS="Mars"
BASE_FLAGS="-Dswing.aatext=true -Dawt.useSystemAAFontSettings=on"
BASE_OPTIONS=""
BASE_JARS="Mars"

# Set parameters
set_jvm
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS

# Let's start
run "\$@"
@@@

%build
sed -i 's/\r//' MARSlicense.txt

cp -p %SOURCE3 build.xml
ant

for i in 16 24 32 48 64; do
    convert images/RedMars50.gif $i.png
done

%install
install -D %name.jar %buildroot%_javadir/%name.jar
install -D %name.sh %buildroot%_bindir/%name
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for i in 16 24 32 48 64; do
    install -D $i.png %buildroot%_iconsdir/${i}x${x}/apps/%name.png
done

%files
%doc *.txt docs/*
%_javadir/%name.jar
%_bindir/%name
%_datadir/applications/Mars.desktop
%_iconsdir/*/apps/*
%_desktopdir/*

%changelog
* Sun Jan 23 2022 Fr. Br. George <george@altlinux.ru> 4.5-alt6
- Update for new java and repackage
- Add icons

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 4.5-alt5_14jpp8
- really added unzip BR

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 4.5-alt4_14jpp11
- jvm11 build, added unzip BR

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 4.5-alt3_14jpp11
- rebuild with java11

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 4.5-alt3_10jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.5-alt3_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 4.5-alt3_7jpp8
- restored jpp patches

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 4.5-alt2_7jpp8
- java update

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 4.5-alt2_6jpp8
- java update

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 4.5-alt2_5jpp8
- merged manual bugfix for #33076; added IDE to .desktop

* Mon Apr 03 2017 Fr. Br. George <george@altlinux.ru> 4.5-alt2
- Add .xml descriptions (Closes: #33076)

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_5jpp7
- new version

