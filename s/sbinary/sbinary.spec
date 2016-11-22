Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global sbinary_version 0.4.2
%global scala_version 2.10
%global scala_long_version 2.10.3
%global build_with_sbt 0
%global want_scalacheck 0

Name:           sbinary
Version:        %{sbinary_version}
Release:        alt1_5jpp8
Summary:        Library for describing binary formats for Scala types

License:        MIT
URL:            https://github.com/harrah/sbinary
Source0:        https://github.com/harrah/sbinary/archive/v%{sbinary_version}.tar.gz
Source1:	https://raw.github.com/willb/climbing-nemesis/master/climbing-nemesis.py

BuildArch:	noarch
%if %{build_with_sbt}
BuildRequires:  sbt
BuildRequires:	python
%else
%endif
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:	mvn(net.sourceforge.fmpp:fmpp)
BuildRequires:	mvn(org.beanshell:bsh)
BuildRequires:	mvn(xml-resolver:xml-resolver)
BuildRequires:	mvn(org.freemarker:freemarker)
BuildRequires:	maven-local
BuildRequires:	maven-local
Requires:       scala
Source44: import.info

%description

SBinary is a library for describing binary protocols, in the form of
mappings between Scala types and binary formats. It can be used as a
robust serialization mechanism for Scala objects or a way of dealing
with existing binary formats found in the wild.

It started out life as a loose port of Haskell's Data.Binary. It's
since evolved a bit from there to take advantage of the features Scala
implicits offer over Haskell type classes, but the core idea has
remained the same.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%if %{build_with_sbt}
sed -i -e 's/2[.]10[.]2/2.10.3/g' project/SBinaryProject.scala

sed -i -e 's|"scalacheck" % "1[.]10[.]0"|"scalacheck" % "1.11.0"|g' project/SBinaryProject.scala
sed -i -e 's|[.]identity||g' project/SBinaryProject.scala
sed -i -e 's/0[.]13[.]0/0.13.1/g' project/build.properties || echo sbt.version=0.13.1 > project/build.properties

cp -r /usr/share/java/sbt/ivy-local .
mkdir boot

cp %{SOURCE1} .

chmod 755 climbing-nemesis.py

%if %{want_scalacheck}
./climbing-nemesis.py --jarfile /usr/share/java/scalacheck.jar org.scalacheck scalacheck ivy-local --version 1.11.0 --scala %{scala_version}
%endif

./climbing-nemesis.py net.sourceforge.fmpp fmpp ivy-local
./climbing-nemesis.py org.freemarker freemarker ivy-local
./climbing-nemesis.py org.beanshell bsh ivy-local --override org.beanshell:bsh
./climbing-nemesis.py xml-resolver xml-resolver ivy-local
%endif

%build

%if %{build_with_sbt}

export SBT_BOOT_DIR=boot
export SBT_IVY_DIR=ivy-local
sbt package deliverLocal publishM2Configuration

%else # build without sbt

mkdir -p core/target/scala-%{scala_version}/src_managed
mkdir -p core/target/scala-%{scala_version}/classes
mkdir -p core/target/scala-%{scala_version}/api

java -cp $(build-classpath fmpp freemarker bsh oro) fmpp.tools.CommandLine -S core/src -O core/target/scala-%{scala_version}/src_managed

scalac core/target/scala-%{scala_version}/src_managed/*.scala -d core/target/scala-%{scala_version}/classes
jar -cvf core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar -C core/target/scala-%{scala_version}/classes .

scaladoc core/target/scala-2.10/src_managed/*.scala -d core/target/scala-2.10/api

cat << EOF > core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom
<?xml version='1.0' encoding='UTF-8'?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.scala-tools.sbinary</groupId>
    <artifactId>sbinary_%{scala_version}</artifactId>
    <packaging>jar</packaging>
    <description>SBinary</description>
    <version>%{version}</version>
    <name>SBinary</name>
    <organization>
        <name>org.scala-tools.sbinary</name>
    </organization>
    <dependencies>
        <dependency>
            <groupId>org.scala-lang</groupId>
            <artifactId>scala-library</artifactId>
            <version>%{scala_long_version}</version>
        </dependency>
    </dependencies>
</project>
EOF

%endif

%install
mkdir -p %{buildroot}/%{_javadir}
mkdir -p %{buildroot}/%{_mavenpomdir}

mkdir -p %{buildroot}/%{_javadocdir}/%{name}

install -pm 644 core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar %{buildroot}/%{_javadir}/%{name}.jar
install -pm 644 core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom

cp -rp core/target/scala-%{scala_version}/api/* %{buildroot}/%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_4jpp8
- new version

