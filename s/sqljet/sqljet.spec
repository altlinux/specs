BuildRequires: javapackages-local
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip hamcrest-core
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           sqljet
Version:        1.1.10
Release:        alt3_6jpp8
Summary:        Pure Java SQLite

Group:          Development/Other
License:        GPLv2
URL:            http://sqljet.com/
Source0:        http://sqljet.com/files/%{name}-%{version}-src.zip

Source4:        %{name}-build.xml
Source5:        %{name}-pom.xml

BuildRequires:  ant
BuildRequires:  antlr-tool
BuildRequires:  antlr3-java
BuildRequires:  antlr3-tool
BuildRequires:  easymock3
BuildRequires:  junit
BuildRequires:  stringtemplate4
Requires:       antlr3-java
BuildArch: noarch

# subpackage dropped in F23
Obsoletes:      sqljet-browser < 1.1.10-5
Source44: import.info

%description
SQLJet is an independent pure Java implementation of a popular SQLite database
management system. SQLJet is a software library that provides API that enables
Java application to read and modify SQLite databases.

%package        javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}

find \( -name '*.class' -o -name '*.jar' \) -delete

rm -rf gradlew.bat gradlew gradle

cp %{SOURCE4} build.xml

cat > sqljet.build.properties <<EOF
sqljet.version.major=1
sqljet.version.minor=1
sqljet.version.micro=10
sqljet.version.build=local

antlr.version=3.4
sqlite.version=3.8.3
EOF


%build
export CLASSPATH=$(build-classpath antlr3-runtime antlr3 antlr hamcrest/core stringtemplate4 easymock3 junit)

ant jars osgi javadoc


%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 755  build/sqljet.jar %{buildroot}%{_javadir}/%{name}.jar

# maven metadata
cp %{SOURCE5} pom.xml
ant pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc LICENSE.txt README.txt CHANGES.txt

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/*

%changelog
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

