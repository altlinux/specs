# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           Mars
Version:        4.5
Release:        alt1_3jpp8
Summary:        An interactive development environment for programming in MIPS assembly language

Group:          Development/Java
License:        MIT
URL:            http://courses.missouristate.edu/KenVollmar/MARS/
Source0:        http://courses.missouristate.edu/KenVollmar//mars/MARS_4_5_Aug2014/Mars4_5.jar
Source1:        Mars
Source2:        Mars.desktop
Source3:        build.xml
BuildArch:      noarch

BuildRequires:  ant
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  desktop-file-utils

Requires: javapackages-tools rpm-build-java
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
ant

%install
install -Dpm 644 %{name}.jar ${RPM_BUILD_ROOT}%{_javadir}/%{name}.jar
install -Dpm 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
desktop-file-install                                \
    --add-category="Development"                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE2}

%files
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/applications/Mars.desktop
%doc MARSlicense.txt

%changelog
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

