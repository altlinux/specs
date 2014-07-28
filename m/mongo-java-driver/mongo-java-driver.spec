# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		mongo-java-driver
Version:	2.7.3
Release:	alt2_3jpp7
Summary:	A Java driver for MongoDB

Group:		Development/Java
BuildArch:	noarch
License:	ASL 2.0
URL:		http://www.mongodb.org/display/DOCS/Java+Language+Center
Source0:	https://github.com/mongodb/mongo-java-driver/tarball/r2.7.3

BuildRequires:	jpackage-utils

BuildRequires:	ant
BuildRequires:	testng
BuildRequires:	git

Requires:	jpackage-utils

Requires:	%{name}-bson
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
%setup -q -n mongodb-mongo-java-driver-a5fae2c

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
(
  build-jar-repository -s -p lib testng
  ant -Dplatforms.JDK_1.5.home=/usr/lib/jvm/java jar javadocs
)
sed -i -e "s|\$VERSION|%{version}|g" maven/maven-bson.xml maven/maven-mongo-java-driver.xml

%install
# Jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p *.jar $RPM_BUILD_ROOT%{_javadir}/

# poms
install -Dpm 644 maven/maven-mongo-java-driver.xml %{buildroot}%{_mavenpomdir}/JPP-mongo.pom
install -Dpm 644 maven/maven-bson.xml %{buildroot}%{_mavenpomdir}/JPP-bson.pom
%add_maven_depmap JPP-mongo.pom mongo.jar
%add_maven_depmap JPP-bson.pom bson.jar

# Java-docs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-bson
cp -rp docs/mongo-java-driver/2.7.2 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{version}
cp -rp docs/bson/2.7.2 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-bson/%{version}

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt1_2jpp7
- full version

