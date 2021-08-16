# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/unzip
# END SourceDeps(oneline)
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global shortname looks

Name:           jgoodies-looks
Version:        2.7.0
Release:        alt1_1jpp11
Summary:        Free high-fidelity Windows and multi-platform appearance

License:        BSD
URL:            http://www.jgoodies.com/freeware/libraries/looks/
# Upstream no longer distributes the library under an Open Source license. Latest
# Open Source release is taken from Maven Central
Source0:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}.pom
# Fix build with JDK 11
Patch0:         %{name}-2.7.0-jdk11.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-common)
BuildArch:      noarch
Source44: import.info

%description
The JGoodies look&feels make your Swing applications and applets look better.
They have been optimized for readability, precise micro-design and usability.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -c
%patch0

mkdir -p src/main/java/
mv com/ src/main/java/

cp %{SOURCE1} pom.xml

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove useless dependency on JUnit (no test available)
%pom_remove_dep junit:junit

%mvn_file :%{name} %{name} %{name}

# Drop Windows L&F support files (unsupported on JDK 11)
rm -r src/main/java/com/jgoodies/looks/windows/


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles


%files javadoc -f .mfiles-javadoc


%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 2.7.0-alt1_1jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.6.0-alt1_16jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.6.0-alt1_14jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_11jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_5jpp8
- new jpp release

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_3jpp8
- new version

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt2
- NMU: BR: maven-local

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1
- update to 2.5.2

* Wed Sep 23 2009 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21517)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt2
- Added java-devel-default

* Wed Apr 30 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt1
- Initial RPM.

