Group: Emulators
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install /usr/bin/unzip ImageMagick-tools
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           Mars
Version:        4.5
Release:        alt6_17jpp11
Summary:        An interactive development environment for programming in MIPS assembly language

License:        MIT
URL:            http://courses.missouristate.edu/KenVollmar/MARS/
Source0:        http://courses.missouristate.edu/KenVollmar//mars/MARS_4_5_Aug2014/Mars4_5.jar
Source1:        Mars
Source2:        Mars.desktop
Source3:        build.xml
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  jpackage-utils
BuildRequires:  desktop-file-utils

Requires:       java-1.8.0-openjdk
Requires:       jpackage-utils
Source44: import.info

%description
MARS is a lightweight interactive development environment (IDE) for
programming in MIPS assembly language, intended for educational-level
use with Patterson and Hennessy's Computer Organization and Design.

%prep
%setup -q -c %{name}-%{version}

find . -name '*.jar'   -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

%build
sed -i 's/\r//' MARSlicense.txt

cp -p %{SOURCE3} build.xml
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 

%install
install -Dpm 644 %{name}.jar ${RPM_BUILD_ROOT}%{_javadir}/%{name}.jar
install -Dpm 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
desktop-file-install                                \
    --add-category="Development" --add-category="IDE" --add-category="Emulator"                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE2}
 # icons
for i in 16 24 32 48 64; do
    convert images/RedMars50.gif $i.png
    install -D $i.png %buildroot%_iconsdir/${i}x${i}/apps/%name.png
done

%files
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/applications/Mars.desktop
%doc MARSlicense.txt

%changelog
* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 4.5-alt6_17jpp11
- update and merged george@ -alt6 changes

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

