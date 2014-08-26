# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          josql
Version:       2.2
Release:       alt1_1jpp7
Summary:       Library to apply SQL-like syntax to Java objects
Group:         Development/Java
License:       ASL 2.0
Url:           http://josql.sourceforge.net/
Source0:       http://sourceforge.net/projects/%{name}/files/%{name}/stable-%{version}/JoSQL-src-stable-%{version}.tar.gz
Source1:       josql-pom-template.xml
# use system javacc gentlyweb-utils and java apis
# fix javac target/source 1.5
Patch0:        %{name}-%{version}-build.patch

BuildRequires: java-javadoc
BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: gentlyweb-utils
BuildRequires: javacc

# contrib-jar deps
# jasperreports
# velocity-tools
# gui-jar deps
# gentlyWEB
# jgoodies-looks -all -plastic -win
# jgoodies-forms
Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
JoSQL (SQL for Java Objects) provides the ability for a developer to apply
a SQL statement to a collection of Java Objects. JoSQL provides the ability
to search, order and group ANY Java objects and should be applied when you
want to perform SQL-like queries on a collection of Java Objects.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n JoSQL-%{version}
find -name '*.jar' -delete
find -name '*.class' -delete

%patch0 -p0

rm -rf 3rd-party-jars/*
# regenerate
rm src/org/josql/parser/TokenMgrError.java
rm src/org/josql/parser/ParseException.java
rm src/org/josql/parser/Token.java
rm src/org/josql/parser/JavaCharStream.java

sed -i 's/\r//' data/javadocsStyle.css

%build

%ant javacc createJar javadoc

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 JoSQL-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/JoSQL.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i "s|@version@|%{version}|" %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "net.sourceforge.%{name}:%{name}"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/JoSQL.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1jpp7
- new release

