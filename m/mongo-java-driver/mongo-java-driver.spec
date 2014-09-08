# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		mongo-java-driver
Version:	2.11.3
Release:	alt1_1jpp7
Summary:	A Java driver for MongoDB

Group:		Development/Java
BuildArch:	noarch
License:	ASL 2.0
URL:		http://www.mongodb.org/display/DOCS/Java+Language+Center
Source0:	https://github.com/mongodb/%{name}/archive/r%{version}.tar.gz

BuildRequires:	jpackage-utils

BuildRequires:	ant
BuildRequires:	ant-contrib
BuildRequires:	testng
BuildRequires:	git

Requires:	jpackage-utils
Source44: import.info

%description
This is the Java driver for MongoDB.

%package bson
Summary:	A Java-based BSON implementation
Group:		Development/Java
Requires:	jpackage-utils

%description bson
This is the Java implementation of BSON that the Java driver for
MongoDB ships with.  It can be used separately by Java applications
that require BSON.
# Upstream has hinted that eventually, their bson implementation will
# be better separated out: http://bsonspec.org/#/implementation
# To make things easier for when that does happen, for now the jar
# and javadocs for this are in separate subpackages.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package bson-javadoc
Summary:	Javadoc for %{name}-bson
Group:		Development/Java
Requires:	jpackage-utils

%description bson-javadoc
This package contains the API documentation for %{name}-bson.

%prep
%setup -qn %{name}-r%{version}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
(
  ln -s $(build-classpath testng) lib/testng-6.3.1.jar
  ant -Dfile.encoding=UTF-8 -Denv.JAVA_HOME=/usr/lib/jvm/java -Dplatforms.JDK_1.5.home=/usr/lib/jvm/java jar javadocs
)
sed -i -e "s|\$VERSION|%{version}|g" maven/maven-bson.xml maven/maven-mongo-java-driver.xml

%install
# Jars
mkdir -p %{buildroot}%{_javadir}
cp -p *.jar %{buildroot}%{_javadir}/

# poms
install -Dpm 644 maven/maven-mongo-java-driver.xml %{buildroot}%{_mavenpomdir}/JPP-mongo.pom
install -Dpm 644 maven/maven-bson.xml %{buildroot}%{_mavenpomdir}/JPP-bson.pom
%add_maven_depmap JPP-mongo.pom mongo.jar
%add_maven_depmap JPP-bson.pom bson.jar

# Java-docs
mkdir -p %{buildroot}%{_javadocdir}
cp -rp docs/mongo-java-driver %{buildroot}%{_javadocdir}/${name}
cp -rp docs/bson %{buildroot}%{_javadocdir}/%{name}-bson

%files
%{_javadir}/mongo.jar
%doc README.md LICENSE.txt
%{_mavenpomdir}/JPP-mongo.pom
%{_mavendepmapfragdir}/mongo-java-driver

%files bson
%{_javadir}/bson.jar
%doc README.md LICENSE.txt
%{_mavenpomdir}/JPP-bson.pom
#%{_mavendepmapfragdir}/bson

%files javadoc
%{_javadocdir}/%{name}
%doc README.md LICENSE.txt

%files bson-javadoc
%{_javadocdir}/%{name}-bson
%doc README.md LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.11.3-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt1_2jpp7
- full version

