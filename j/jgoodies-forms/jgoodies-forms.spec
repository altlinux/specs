# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/unzip
# END SourceDeps(oneline)
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define shortname forms

Name:           jgoodies-forms
Version:        1.9.0
Release:        alt1_1jpp11
Summary:        Framework to lay out and implement elegant Swing panels in Java

License:        BSD
URL:            https://www.jgoodies.com/freeware/libraries/forms/
# Upstream no longer distributes the library under an Open Source license. Latest
# Open Source release is taken from Maven Central
Source0:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/jgoodies/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-common)
BuildArch:      noarch
Source44: import.info

%description
The JGoodies Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the hard stuff
possible, the good design easy and the bad difficult.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -c

mkdir -p src/main/java/
mv com/ src/main/java/

cp %{SOURCE1} pom.xml

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove useless dependency on JUnit (no test available)
%pom_remove_dep junit:junit

%mvn_file :%{name} %{name} %{name}


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles


%files javadoc -f .mfiles-javadoc


%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 1.9.0-alt1_1jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.8.0-alt1_15jpp11
- fc34 update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_11jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1jpp8
- java8 mass update

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2
- NMU: BR: maven-local

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- update to 1.6.0

* Sun Sep 20 2009 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21516)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt2
- Added java-devel-default

* Tue Apr 29 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt1
- Initial RPM
