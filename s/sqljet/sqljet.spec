Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sqljet
Version:        1.1.10
Release:        alt3_25jpp11
Summary:        Pure Java SQLite

License:        GPLv2
URL:            http://sqljet.com/
Source0:        http://sqljet.com/files/%{name}-%{version}-src.zip

Source4:        %{name}-build.xml
Source5:        %{name}-pom.xml

BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  antlr32-java
BuildRequires:  antlr32-tool
BuildRequires:  easymock3
BuildRequires:  junit
BuildRequires:  stringtemplate
BuildRequires:  hamcrest
BuildRequires:  javapackages-local
BuildArch: noarch
Source44: import.info

%description
SQLJet is an independent pure Java implementation of a popular SQLite database
management system. SQLJet is a software library that provides API that enables
Java application to read and modify SQLite databases.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name} 
BuildArch: noarch
%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

find \( -name '*.class' -o -name '*.jar' \) -delete

rm -rf gradlew.bat gradlew gradle

cp %{SOURCE4} build.xml
cp %{SOURCE5} pom.xml

cat > sqljet.build.properties <<EOF
sqljet.version.major=1
sqljet.version.minor=1
sqljet.version.micro=10
sqljet.version.build=local

antlr.version=3.2
sqlite.version=3.8.3
EOF


%build
export CLASSPATH=$(build-classpath antlr32/antlr-runtime-3.2 antlr32/antlr-3.2 antlr stringtemplate easymock3 junit hamcrest-core)
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  jars osgi javadoc pom

%install
%mvn_artifact pom.xml build/sqljet.jar
%mvn_file ":sqljet" sqljet
%mvn_install -J build/javadoc

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:1.1.10-alt3_25jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.10-alt3_18jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt3_14jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt3_12jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt3_10jpp8
- java fc28+ update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt3_6jpp8
- added BR: javapackages-local for javapackages 5

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt2_6jpp8
- updated dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt1_6jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.10-alt1_5jpp8
- java8 mass update

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_4jpp7
- fc update

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_8jpp7
- fixed build with antlr3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_4_redhat_1jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp6
- new version

