Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          josql
Version:       2.2
Release:       alt1_12jpp8
Summary:       Library to apply SQL-like syntax to Java objects
License:       ASL 2.0
Url:           http://josql.sourceforge.net/
Source0:       http://sourceforge.net/projects/%{name}/files/%{name}/stable-%{version}/JoSQL-src-stable-%{version}.tar.gz
Source1:       josql-pom-template.xml
Source2:       josql.bnd
# use system javacc gentlyweb-utils and java apis
# fix javac target/source 1.5
Patch0:        %{name}-%{version}-build.patch
Patch1:        josql-2.2-doclint.patch

BuildRequires: java-devel
BuildRequires: java-javadoc
BuildRequires: javapackages-local

BuildRequires: ant
BuildRequires: aqute-bnd
BuildRequires: gentlyweb-utils
BuildRequires: javacc

# contrib-jar deps
# jasperreports
# velocity-tools
# gui-jar deps
# gentlyWEB
# jgoodies-looks -all -plastic -win
# jgoodies-forms

BuildArch:     noarch
Source44: import.info

%description
JoSQL (SQL for Java Objects) provides the ability for a developer to apply
a SQL statement to a collection of Java Objects. JoSQL provides the ability
to search, order and group ANY Java objects and should be applied when you
want to perform SQL-like queries on a collection of Java Objects.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n JoSQL-%{version}
find -name '*.jar' -delete
find -name '*.class' -delete

%patch0 -p0
%patch1 -p0

rm -rf 3rd-party-jars/*
# regenerate
#rm src/org/josql/parser/TokenMgrError.java
#rm src/org/josql/parser/ParseException.java
#rm src/org/josql/parser/Token.java
#rm src/org/josql/parser/JavaCharStream.java

sed -i 's/\r//' data/javadocsStyle.css

cp -p %{SOURCE1} pom.xml
sed -i "s|@version@|%{version}|" pom.xml

%build
# javacc (task) 6.x generate broken java files 
%ant createJar javadoc

bnd wrap -p %{SOURCE2} -o %{name}.jar -v %{version} JoSQL-%{version}.jar

%install
%mvn_file net.sf.%{name}:%{name} %{name} JoSQL
%mvn_artifact pom.xml %{name}.jar
%mvn_alias net.sf.%{name}:%{name} net.sourceforge.%{name}:%{name}
%mvn_install -J docs

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_12jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_10jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_6jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1jpp7
- new release

